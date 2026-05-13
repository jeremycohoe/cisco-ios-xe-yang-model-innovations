#!/usr/bin/env python3
"""
YANG Release Comparison Script
Compares two consecutive IOS-XE releases and generates detailed markdown report

Usage:
    python3 compare_releases.py --old 1711 --new 1721
    python3 compare_releases.py --all
"""

import os
import sys
import subprocess
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime
import argparse

# Base path to release folders - relative to script location
SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PATH = SCRIPT_DIR.parent.parent  # Go up to xe/ directory

# Release order (chronological)
RELEASE_ORDER = [
    "1631", "1632", "1641", "1651", "1661", "1662", "1671", "1681", "1691", "1693",
    "16101", "16111", "16121", "1711", "1721", "1731", "1741", "1751",
    "1761", "1771", "1781", "1791", "17101", "17111", "17121", "17131",
    "17141", "17151", "17161", "17171", "17181", "2611"
]

# GitHub folder mapping (local folder → GitHub path)
GITHUB_FOLDER_MAP = {
    "apoorva-261": "2611"
}

class YANGComparator:
    def __init__(self, old_release, new_release):
        self.old_release = old_release
        self.new_release = new_release
        self.old_path = BASE_PATH / old_release
        self.new_path = BASE_PATH / new_release
        
        # Results
        self.new_files = []
        self.modified_files = []
        self.deleted_files = []
        self.file_changes = {}
        
    def get_yang_files(self, release_path):
        """Get list of .yang files in a release folder"""
        if not release_path.exists():
            print(f"ERROR: Release folder not found: {release_path}")
            sys.exit(1)
        
        yang_files = sorted([f.name for f in release_path.glob("*.yang")])
        return set(yang_files)
    
    def find_file_differences(self):
        """Identify new, modified, and deleted files"""
        old_files = self.get_yang_files(self.old_path)
        new_files = self.get_yang_files(self.new_path)
        
        self.new_files = sorted(new_files - old_files)
        self.deleted_files = sorted(old_files - new_files)
        
        # Check for modifications in common files
        common_files = old_files & new_files
        for filename in sorted(common_files):
            old_file = self.old_path / filename
            new_file = self.new_path / filename
            
            # Quick file comparison
            try:
                result = subprocess.run(
                    ["diff", "-q", str(old_file), str(new_file)],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.returncode != 0:  # Files differ
                    self.modified_files.append(filename)
            except Exception as e:
                print(f"Warning: Could not compare {filename}: {e}")
    
    def count_xpaths(self, filename, release_path):
        """Count XPaths in a YANG file using pyang tree output
        
        Method: Uses pyang tree format and counts lines with node indicators (+, |)
        that have read-write (rw), read-only (ro), or execute (x) attributes.
        
        Equivalent shell command:
        pyang -f tree --tree-depth=99 file.yang 2>/dev/null | \
            grep -E "^\s*[+|]" | grep -E "(rw|ro|x|--)" | wc -l
        """
        filepath = release_path / filename
        
        try:
            # Use pyang tree output to count nodes
            result = subprocess.run(
                ["pyang", "-f", "tree", "--tree-depth", "99", str(filepath)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                # Count lines that represent data nodes
                # Match lines starting with spaces followed by + or |
                # and containing rw, ro, x, or --
                count = 0
                for line in result.stdout.split('\n'):
                    if re.match(r'^\s*[+|]', line):
                        if any(indicator in line for indicator in ['rw', 'ro', 'x', '--']):
                            count += 1
                return count
            else:
                return 0
                
        except subprocess.TimeoutExpired:
            print(f"  Timeout counting XPaths for {filename}")
            return 0
        except FileNotFoundError:
            print(f"  ERROR: pyang not found. Install with: pip install pyang")
            return 0
        except Exception as e:
            print(f"  Warning: Could not count XPaths for {filename}: {e}")
            return 0
    
    def analyze_diff(self, filename):
        """Analyze differences between old and new versions"""
        old_file = self.old_path / filename
        new_file = self.new_path / filename
        
        try:
            result = subprocess.run(
                ["diff", "-u", str(old_file), str(new_file)],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            diff_output = result.stdout
            if not diff_output:
                return {"summary": "No changes detected", "added": 0, "removed": 0}
            
            # Parse diff
            changes = {
                'added_nodes': [],
                'removed_nodes': [],
                'added_imports': [],
                'added_enums': [],
                'must_statements': 0,
                'description_changes': 0
            }
            
            for line in diff_output.split('\n'):
                if line.startswith('+') and not line.startswith('+++'):
                    content = line[1:].strip()
                    
                    # Count different types of changes
                    if re.search(r'(leaf|container|list)\s+\S+', content):
                        match = re.search(r'(leaf|container|list)\s+(\S+)', content)
                        if match:
                            changes['added_nodes'].append(match.group(2))
                    
                    if 'import' in content:
                        match = re.search(r'import\s+(\S+)', content)
                        if match:
                            changes['added_imports'].append(match.group(1))
                    
                    if 'enum' in content:
                        changes['added_enums'].append(content)
                    
                    if 'must' in content:
                        changes['must_statements'] += 1
                    
                    if 'description' in content:
                        changes['description_changes'] += 1
                
                elif line.startswith('-') and not line.startswith('---'):
                    content = line[1:].strip()
                    if re.search(r'(leaf|container|list)\s+\S+', content):
                        match = re.search(r'(leaf|container|list)\s+(\S+)', content)
                        if match:
                            changes['removed_nodes'].append(match.group(2))
            
            # Generate summary
            summary_parts = []
            
            if changes['added_nodes']:
                count = len(changes['added_nodes'])
                summary_parts.append(f"Added {count} new data node{'s' if count != 1 else ''}")
            
            if changes['added_imports']:
                if len(changes['added_imports']) <= 2:
                    summary_parts.append(f"imported {', '.join(changes['added_imports'])}")
                else:
                    summary_parts.append(f"added {len(changes['added_imports'])} new imports")
            
            if changes['added_enums']:
                summary_parts.append(f"new enum values added")
            
            if changes['must_statements'] > 0:
                summary_parts.append("enhanced validation constraints")
            
            if changes['removed_nodes']:
                summary_parts.append(f"deprecated {len(changes['removed_nodes'])} node{'s' if len(changes['removed_nodes']) != 1 else ''}")
            
            if not summary_parts and changes['description_changes'] > 0:
                summary_parts.append("updated descriptions")
            
            if not summary_parts:
                added = len([l for l in diff_output.split('\n') if l.startswith('+') and not l.startswith('+++')])
                removed = len([l for l in diff_output.split('\n') if l.startswith('-') and not l.startswith('---')])
                summary = f"Minor refinements ({added} additions, {removed} deletions)"
            else:
                summary = '; '.join(summary_parts[:3])  # Limit to 3 main points
            
            return {
                'summary': summary,
                'added': len(changes['added_nodes']),
                'removed': len(changes['removed_nodes']),
                'details': changes
            }
            
        except Exception as e:
            return {"summary": f"Error analyzing: {str(e)}", "added": 0, "removed": 0}
    
    def categorize_model(self, filename):
        """Categorize YANG model by type"""
        name_lower = filename.lower()
        
        if '-oper.yang' in name_lower:
            return 'Operational'
        elif '-rpc.yang' in name_lower:
            return 'RPC'
        elif '-events.yang' in name_lower:
            return 'Events'
        elif '-cfg.yang' in name_lower:
            return 'Configuration'
        elif '-types.yang' in name_lower or '-deviation.yang' in name_lower:
            return 'Types/Deviation'
        elif filename.startswith('openconfig-'):
            return 'OpenConfig'
        elif filename.startswith('ietf-'):
            return 'IETF'
        elif 'native' in name_lower or 'Cisco-IOS-XE-' in filename:
            return 'Native/Configuration'
        else:
            return 'Other'
    
    def run_analysis(self):
        """Run complete analysis"""
        print(f"\n{'='*80}")
        print(f"Comparing: {self.old_release} → {self.new_release}")
        print(f"{'='*80}\n")
        
        # Find file differences
        print("📁 Analyzing file differences...")
        self.find_file_differences()
        
        print(f"   New files: {len(self.new_files)}")
        print(f"   Modified files: {len(self.modified_files)}")
        print(f"   Deleted files: {len(self.deleted_files)}")
        
        # Analyze new files
        print(f"\n📊 Analyzing new files ({len(self.new_files)})...")
        for i, filename in enumerate(self.new_files, 1):
            print(f"   [{i}/{len(self.new_files)}] {filename}")
            xpaths = self.count_xpaths(filename, self.new_path)
            category = self.categorize_model(filename)
            
            self.file_changes[filename] = {
                'status': 'new',
                'category': category,
                'xpaths_new': xpaths,
                'xpaths_old': 0,
                'xpaths_delta': xpaths,
                'summary': 'New model introduced in this release'
            }
        
        # Analyze modified files
        print(f"\n📊 Analyzing modified files ({len(self.modified_files)})...")
        for i, filename in enumerate(self.modified_files, 1):
            print(f"   [{i}/{len(self.modified_files)}] {filename}")
            
            # Count XPaths
            old_xpaths = self.count_xpaths(filename, self.old_path)
            new_xpaths = self.count_xpaths(filename, self.new_path)
            delta = new_xpaths - old_xpaths
            
            # Analyze changes
            analysis = self.analyze_diff(filename)
            category = self.categorize_model(filename)
            
            self.file_changes[filename] = {
                'status': 'modified',
                'category': category,
                'xpaths_old': old_xpaths,
                'xpaths_new': new_xpaths,
                'xpaths_delta': delta,
                'summary': analysis['summary']
            }
        
        # Track deleted files
        for filename in self.deleted_files:
            category = self.categorize_model(filename)
            self.file_changes[filename] = {
                'status': 'deleted',
                'category': category,
                'summary': 'Removed in this release'
            }
        
        print(f"\n✅ Analysis complete!")
        return self.file_changes

def main():
    parser = argparse.ArgumentParser(description='Compare YANG models between releases')
    parser.add_argument('--old', help='Old release version (e.g., 1711)')
    parser.add_argument('--new', help='New release version (e.g., 1721)')
    parser.add_argument('--all', action='store_true', help='Process all releases')
    
    args = parser.parse_args()
    
    if args.all:
        print("Processing all release comparisons...")
        # This will be implemented in Phase 2
        print("TODO: Implement batch processing")
        sys.exit(0)
    
    if not args.old or not args.new:
        parser.print_help()
        sys.exit(1)
    
    # Run comparison
    comparator = YANGComparator(args.old, args.new)
    results = comparator.run_analysis()
    
    # Save results
    output_file = f"analysis_{args.new}.json"
    print(f"\n💾 Results saved to: {output_file}")
    print(f"   Use generate_markdown.py to create the .md file")

if __name__ == "__main__":
    main()
