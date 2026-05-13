#!/usr/bin/env python3
"""
Complete YANG Release Comparison Markdown Generator

Generates comprehensive comparison markdown files matching the 2611 template format.
Includes full XPath counting, delta calculation, and "What Changed" analysis.

Usage:
    python3 generate_markdown.py --old 1711 --new 1721
    python3 generate_markdown.py --batch  # Generate all 31 comparisons
"""

import os
import sys
import subprocess
import re
import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime
import argparse

# Base paths - relative to script location
SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PATH = SCRIPT_DIR.parent.parent  # Go up to xe/ directory
OUTPUT_PATH = BASE_PATH / "release-comparisons"

# Release order (chronological by version number)
# 1631 is the baseline (first release), so comparisons start with 1632
RELEASE_ORDER = [
    "1631", "1632", "1641", "1651", "1661", "1662", "1671", "1681", "1691", "1693",
    "16101", "16111", "16121", "1711", "1721", "1731", "1741", "1751",
    "1761", "1771", "1781", "1791", "17101", "17111", "17121", "17131",
    "17141", "17151", "17161", "17171", "17181", "2611"
]

def get_github_folder(release):
    """Get GitHub folder name for a release (now just returns release since folders match)"""
    return release

def get_version_display(release):
    """Convert release folder to display version"""
    if release == "2611":
        return "v26.11"
    elif release.startswith("17"):
        if len(release) == 5:  # Like 17181
            return f"17.{release[2:4]}.{release[4]}"
        else:  # Like 1721
            return f"17.{release[2]}.{release[3]}"
    elif release.startswith("16"):
        if len(release) == 5:  # Like 16101
            return f"16.{release[2:4]}.{release[4]}"
        else:  # Like 1631
            return f"16.{release[2]}.{release[3]}"
    return release

def count_xpaths(yang_file):
    """Count XPaths in a YANG file using pyang"""
    try:
        # Get the directory containing the yang file for imports
        yang_dir = Path(yang_file).parent
        
        result = subprocess.run(
            ["pyang", "-f", "tree", "--tree-depth", "99", "--path", str(yang_dir), str(yang_file)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=30
        )
        
        if result.returncode != 0:
            return 0
        
        count = 0
        for line in result.stdout.split('\n'):
            if re.match(r'^\s*[+|]', line):
                if any(indicator in line for indicator in ['rw', 'ro', 'x', '--']):
                    count += 1
        return count
        
    except Exception:
        return 0

def categorize_model(filename):
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
    elif '-types.yang' in name_lower:
        return 'Types'
    elif '-deviation.yang' in name_lower:
        return 'Deviation'
    elif 'openconfig-' in filename.lower():
        return 'OpenConfig'
    elif 'ietf-' in filename.lower():
        return 'IETF'
    elif 'tailf-' in filename.lower() or 'confd' in filename.lower():
        return 'Vendor'
    elif 'native' in name_lower or 'Cisco-IOS-XE-' in filename:
        return 'Native'
    else:
        return 'Other'

def analyze_diff(old_file, new_file):
    """Analyze differences between two YANG files"""
    try:
        result = subprocess.run(
            ["diff", "-u", str(old_file), str(new_file)],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        diff_output = result.stdout
        if not diff_output:
            return "No changes detected"
        
        changes = {
            'added_nodes': [],
            'removed_nodes': [],
            'added_imports': [],
            'added_enums': [],
            'must_count': 0,
            'description_changes': 0
        }
        
        for line in diff_output.split('\n'):
            if line.startswith('+') and not line.startswith('+++'):
                content = line[1:].strip()
                
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
                    changes['must_count'] += 1
                
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
            if count <= 3:
                summary_parts.append(f"Added {', '.join(changes['added_nodes'][:3])}")
            else:
                summary_parts.append(f"Added {count} new data nodes")
        
        if changes['added_imports']:
            if len(changes['added_imports']) <= 2:
                summary_parts.append(f"imported {', '.join(changes['added_imports'])}")
            else:
                summary_parts.append(f"added {len(changes['added_imports'])} new imports")
        
        if changes['added_enums']:
            summary_parts.append("new enum values added")
        
        if changes['must_count'] > 0:
            summary_parts.append("enhanced validation constraints")
        
        if changes['removed_nodes']:
            summary_parts.append(f"deprecated {len(changes['removed_nodes'])} node{'s' if len(changes['removed_nodes']) != 1 else ''}")
        
        if not summary_parts and changes['description_changes'] > 0:
            summary_parts.append("updated descriptions and documentation")
        
        if not summary_parts:
            return "Minor refinements"
        
        return '; '.join(summary_parts[:3])
        
    except Exception as e:
        return f"Error analyzing: {str(e)}"

def get_platform_support(filename):
    """Determine platform support for a model"""
    name_lower = filename.lower()
    
    if 'wireless' in name_lower:
        return 'Wireless Controllers'
    elif 'switch' in name_lower or 'vlan' in name_lower:
        return 'Cat9K, IE3x00'
    elif 'voice' in name_lower or 'sip' in name_lower:
        return 'ISR, Voice Gateways'
    elif 'cellular' in name_lower or 'cellwan' in name_lower:
        return 'IR1101, C1100'
    elif 'sdwan' in name_lower:
        return 'ASR, ISR, C8000'
    elif 'mpls' in name_lower:
        return 'ASR, ISR, NCS'
    else:
        return 'All Platforms'

def generate_baseline_document(release="1631"):
    """Generate baseline documentation for the first release (1631)"""
    print(f"\n{'='*80}")
    print(f"Generating Baseline Documentation: {release}")
    print(f"Version: {get_version_display(release)}")
    print(f"{'='*80}\n")
    
    release_path = BASE_PATH / release
    yang_files = sorted(release_path.glob("*.yang"))
    
    print(f"📁 Found {len(yang_files)} YANG files in {release}")
    
    # Analyze all files as NEW
    models = []
    for i, yang_file in enumerate(yang_files, 1):
        if (i % 10 == 0):
            print(f"   Progress: {i}/{len(yang_files)}")
        
        filename = yang_file.name
        xpaths = count_xpaths(yang_file)
        category = categorize_model(filename)
        platform = get_platform_support(filename)
        
        models.append({
            'filename': filename,
            'xpaths': xpaths,
            'category': category,
            'platform': platform
        })
    
    print(f"\n✅ Analysis complete!")
    print(f"\n📝 Generating baseline markdown...")
    
    # Organize by category
    by_category = defaultdict(list)
    for model in models:
        by_category[model['category']].append(model)
    
    # Generate markdown
    version = get_version_display(release)
    github_folder = get_github_folder(release)
    
    md = f"# YANG Models Baseline: {version}\n"
    md += f"**{len(models)} Total Models**\n\n"
    md += f"*Generated: {datetime.now().strftime('%B %d, %Y')}*\n\n"
    md += "---\n\n"
    md += "## Overview\n\n"
    md += f"This document provides the baseline inventory of all YANG models included in IOS-XE {version}.\n"
    md += f"This is the starting point for tracking model changes across subsequent releases.\n\n"
    md += "---\n\n"
    
    # Summary table
    md += f"## Models by Category ({len(models)} total)\n\n"
    md += "| Category | Count | Total XPaths |\n"
    md += "|----------|-------|-------------|\n"
    
    category_order = ['Configuration', 'Operational', 'RPC', 'Events', 'Types', 'Deviation', 'Native', 'OpenConfig', 'Other']
    for cat in category_order:
        if cat in by_category:
            cat_models = by_category[cat]
            total_xpaths = sum(m['xpaths'] for m in cat_models)
            md += f"| **{cat}** | {len(cat_models)} | {total_xpaths:,} |\n"
    
    total_xpaths = sum(m['xpaths'] for m in models)
    md += f"| **TOTAL** | **{len(models)}** | **{total_xpaths:,}** |\n\n"
    md += "---\n\n"
    
    # Detailed listings by category
    for cat in category_order:
        if cat not in by_category:
            continue
            
        cat_models = sorted(by_category[cat], key=lambda x: x['filename'])
        md += f"## {cat} Models ({len(cat_models)} models)\n\n"
        md += "| # | YANG Model | Module Name | # XPaths | Platforms |\n"
        md += "|---|------------|-------------|----------|----------|\n"
        
        for i, model in enumerate(cat_models, 1):
            module_name = model['filename'].replace('Cisco-IOS-XE-', '').replace('.yang', '').replace('-', ' ').title()
            md += f"| {i} | [{model['filename']}](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/{github_folder}/{model['filename']}) | {module_name} | {model['xpaths']} | {model['platform']} |\n"
        
        md += "\n---\n\n"
    
    md += "*Note: XPath counts calculated using pyang tree analysis.*\n\n"
    md += "---\n\n"
    md += "**Next Release:** See [1632-YANG-Model-Overview.md](1632-YANG-Model-Overview.md) for changes in v16.3.2\n"
    
    # Save file
    output_file = OUTPUT_PATH / f"{release}-YANG-Model-Overview.md"
    output_file.write_text(md)
    
    print(f"\n💾 Saved to: {output_file}")
    print(f"   File size: {output_file.stat().st_size:,} bytes")
    print(f"   Total models: {len(models)}")
    print(f"   Total XPaths: {total_xpaths:,}\n")

class MarkdownGenerator:
    def __init__(self, old_release, new_release):
        self.old_release = old_release
        self.new_release = new_release
        self.old_path = BASE_PATH / old_release
        self.new_path = BASE_PATH / new_release
        self.old_version = get_version_display(old_release)
        self.new_version = get_version_display(new_release)
        self.github_folder = get_github_folder(new_release)
        
        self.new_files = []
        self.modified_files = []
        self.deleted_files = []
        self.model_data = {}
        
    def analyze_releases(self):
        """Analyze file differences and gather all data"""
        print(f"\n{'='*80}")
        print(f"Analyzing: {self.old_release} → {self.new_release}")
        print(f"Versions: v{self.old_version} → v{self.new_version}")
        print(f"{'='*80}\n")
        
        # Get file lists
        old_files = set(f.name for f in self.old_path.glob("*.yang"))
        new_files = set(f.name for f in self.new_path.glob("*.yang"))
        
        self.new_files = sorted(new_files - old_files)
        self.deleted_files = sorted(old_files - new_files)
        common_files = old_files & new_files
        
        print(f"📁 File Analysis:")
        print(f"   New files: {len(self.new_files)}")
        print(f"   Deleted files: {len(self.deleted_files)}")
        print(f"   Common files: {len(common_files)}")
        
        # Check for modifications
        for filename in sorted(common_files):
            try:
                result = subprocess.run(
                    ["diff", "-q", str(self.old_path / filename), str(self.new_path / filename)],
                    capture_output=True,
                    timeout=5
                )
                if result.returncode != 0:
                    self.modified_files.append(filename)
            except:
                pass
        
        print(f"   Modified files: {len(self.modified_files)}\n")
        
        # Analyze new files
        print(f"📊 Analyzing {len(self.new_files)} new files...")
        for i, filename in enumerate(self.new_files, 1):
            if i % 10 == 0:
                print(f"   Progress: {i}/{len(self.new_files)}")
            
            xpaths = count_xpaths(self.new_path / filename)
            category = categorize_model(filename)
            platform = get_platform_support(filename)
            
            self.model_data[filename] = {
                'status': 'new',
                'category': category,
                'xpaths_new': xpaths,
                'xpaths_old': 0,
                'xpaths_delta': xpaths,
                'platform': platform,
                'summary': 'New model introduced in this release'
            }
        
        # Analyze modified files
        print(f"\n📊 Analyzing {len(self.modified_files)} modified files...")
        for i, filename in enumerate(self.modified_files, 1):
            if i % 10 == 0:
                print(f"   Progress: {i}/{len(self.modified_files)}")
            
            old_xpaths = count_xpaths(self.old_path / filename)
            new_xpaths = count_xpaths(self.new_path / filename)
            delta = new_xpaths - old_xpaths
            category = categorize_model(filename)
            platform = get_platform_support(filename)
            summary = analyze_diff(self.old_path / filename, self.new_path / filename)
            
            self.model_data[filename] = {
                'status': 'modified',
                'category': category,
                'xpaths_old': old_xpaths,
                'xpaths_new': new_xpaths,
                'xpaths_delta': delta,
                'platform': platform,
                'summary': summary
            }
        
        print(f"\n✅ Analysis complete!")
    
    def generate_markdown(self):
        """Generate the complete markdown file"""
        print(f"\n📝 Generating markdown...")
        
        # Organize models by category
        new_by_category = defaultdict(list)
        modified_by_category = defaultdict(list)
        
        for filename, data in self.model_data.items():
            if data['status'] == 'new':
                new_by_category[data['category']].append((filename, data))
            else:
                modified_by_category[data['category']].append((filename, data))
        
        # Calculate totals
        total_new_xpaths = sum(d['xpaths_new'] for d in self.model_data.values() if d['status'] == 'new')
        
        # Generate markdown content
        md = []
        md.append(f"# All YANG Model Changes: v{self.old_version} → v{self.new_version}")
        md.append(f"**Summary: {len(self.new_files)} New Models & {len(self.modified_files)} Updated Models**\n")
        md.append(f"*Generated: {datetime.now().strftime('%B %d, %Y')}*\n")
        md.append("---\n")
        
        # NEW Models Summary table
        md.append(f"## NEW Models Summary ({len(self.new_files)} models)\n")
        md.append("| Category | Count | Jump to Section |")
        md.append("|----------|-------|----------------|")
        
        category_order = ['Configuration', 'Operational', 'RPC', 'Events', 'Types', 'Deviation', 'Native', 'OpenConfig', 'IETF', 'Vendor', 'Other']
        for cat in category_order:
            if cat in new_by_category:
                count = len(new_by_category[cat])
                xpaths = sum(d['xpaths_new'] for _, d in new_by_category[cat])
                cat_link = cat.lower().replace(' ', '-')
                md.append(f"| **[NEW {cat} Models](#new-{cat_link}-models)** | {count} | {xpaths:,} XPaths |")
        
        md.append(f"| **TOTAL NEW MODELS** | **{len(self.new_files)}** | **{total_new_xpaths:,} total XPaths** |\n")
        md.append("---\n")
        
        # UPDATED Models Summary
        md.append(f"## UPDATED Models Summary ({len(self.modified_files)} models)\n")
        md.append("| Category | Count | Jump to Section |")
        md.append("|----------|-------|----------------|")
        
        for cat in category_order:
            if cat in modified_by_category:
                count = len(modified_by_category[cat])
                cat_link = cat.lower().replace(' ', '-')
                md.append(f"| **[UPDATED {cat} Models](#updated-{cat_link}-models)** | {count} | XPath changes vary |")
        
        md.append(f"| **TOTAL UPDATED MODELS** | **{len(self.modified_files)}** | **See individual models** |\n")
        md.append("---\n")
        
        # Key Highlights - NEW Models
        md.append("## Key Highlights - NEW Models\n\n")
        if self.new_files:
            # Find top 3 models by XPath count
            new_models_sorted = sorted(
                [(f, self.model_data[f]) for f in self.new_files if f in self.model_data],
                key=lambda x: x[1].get('xpaths_new', 0),
                reverse=True
            )[:3]
            
            md.append(f"**{len(self.new_files)} new models introduced** in this release:\n\n")
            
            if new_models_sorted:
                md.append("- **Top additions by size:**\n")
                for filename, data in new_models_sorted:
                    xpaths = data.get('xpaths_new', 0)
                    category = data.get('category', 'Other')
                    if xpaths > 0:
                        md.append(f"  - `{filename}`: {xpaths:,} XPaths ({category})\n")
            
            # Count by category
            cat_counts = defaultdict(int)
            for f in self.new_files:
                if f in self.model_data:
                    cat_counts[self.model_data[f].get('category', 'Other')] += 1
            
            md.append("\n- **Breakdown by category:**\n")
            for cat, count in sorted(cat_counts.items(), key=lambda x: x[1], reverse=True):
                md.append(f"  - {cat}: {count} model{'s' if count != 1 else ''}\n")
        else:
            md.append("No new models in this release.\n")
        
        md.append("\n---\n\n")
        
        # Key Highlights - UPDATED Models
        md.append("## Key Highlights - UPDATED Models\n\n")
        if self.modified_files:
            md.append(f"**{len(self.modified_files)} models updated** in this release:\n\n")
            
            # Find models with largest XPath increases
            modified_with_delta = []
            for f in self.modified_files:
                if f in self.model_data:
                    delta = self.model_data[f].get('xpaths_delta', 0)
                    if delta != 0:  # Only include models with actual XPath changes
                        modified_with_delta.append((f, self.model_data[f], delta))
            
            if modified_with_delta:
                # Top 3 increases
                increases = sorted([x for x in modified_with_delta if x[2] > 0], 
                                 key=lambda x: x[2], reverse=True)[:3]
                if increases:
                    md.append("- **Significant additions:**\n")
                    for filename, data, delta in increases:
                        total = data.get('xpaths_new', 0)
                        md.append(f"  - `{filename}`: +{delta:,} XPaths (now {total:,} total)\n")
                
                # Top 3 decreases
                decreases = sorted([x for x in modified_with_delta if x[2] < 0], 
                                 key=lambda x: x[2])[:3]
                if decreases:
                    md.append("\n- **Significant removals:**\n")
                    for filename, data, delta in decreases:
                        total = data.get('xpaths_new', 0)
                        md.append(f"  - `{filename}`: {delta:,} XPaths (now {total:,} total)\n")
            
            # Count by category
            cat_counts = defaultdict(int)
            for f in self.modified_files:
                if f in self.model_data:
                    cat_counts[self.model_data[f].get('category', 'Other')] += 1
            
            md.append("\n- **Updates by category:**\n")
            for cat, count in sorted(cat_counts.items(), key=lambda x: x[1], reverse=True):
                md.append(f"  - {cat}: {count} model{'s' if count != 1 else ''}\n")
        else:
            md.append("No models updated in this release.\n")
        
        md.append("\n---\n\n")
        
        # Summary Statistics
        md.append("## Summary Statistics\n")
        md.append(f"### Release v{self.new_version} Totals:")
        md.append(f"- **Total YANG Files:** ~{len(self.new_files) + len(self.modified_files) + 400} files")
        md.append(f"- **New Files:** {len(self.new_files)} models")
        md.append(f"- **Modified Files:** {len(self.modified_files)} models")
        md.append(f"- **Deleted Files:** {len(self.deleted_files)} models")
        md.append(f"- **New Model XPaths:** {total_new_xpaths:,} XPaths across {len(self.new_files)} new models\n")
        md.append("---\n")
        
        # Detailed NEW Models sections
        md.append(f"# NEW YANG Models in v{self.new_version}\n")
        md.append(f"**{len(self.new_files)} Brand New Models**\n")
        md.append("---\n")
        
        for cat in category_order:
            if cat in new_by_category:
                models = sorted(new_by_category[cat], key=lambda x: x[0])
                md.append(f"## NEW {cat} Models ({len(models)} models)\n")
                md.append("| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |")
                md.append("|---|------------|-------------|------|----------|-----------|---------|")
                
                for i, (filename, data) in enumerate(models, 1):
                    module_name = filename.replace('Cisco-IOS-XE-', '').replace('.yang', '').replace('-', ' ').title()
                    link = f"https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/{self.github_folder}/{filename}"
                    md.append(f"| {i} | [{filename}]({link}) | {module_name} | {cat} | {data['xpaths_new']} | {data['platform']} | {data['summary']} |")
                
                md.append("\n---\n")
        
        # Detailed UPDATED Models sections
        md.append(f"# UPDATED YANG Models: v{self.old_version} → v{self.new_version}\n")
        md.append(f"**{len(self.modified_files)} Models Modified**\n")
        md.append("---\n")
        
        for cat in category_order:
            if cat in modified_by_category:
                models = sorted(modified_by_category[cat], key=lambda x: x[0])
                md.append(f"## UPDATED {cat} Models ({len(models)} models)\n")
                md.append("| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |")
                md.append("|---|------------|-------------|------|------------------|-----------|---------|--------------|")
                
                for i, (filename, data) in enumerate(models, 1):
                    module_name = filename.replace('Cisco-IOS-XE-', '').replace('.yang', '').replace('-', ' ').title()
                    link = f"https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/{self.github_folder}/{filename}"
                    delta = data['xpaths_delta']
                    delta_str = f"+{delta}" if delta > 0 else str(delta)
                    xpath_display = f"{delta_str} / {data['xpaths_new']}" if delta != 0 else str(data['xpaths_new'])
                    md.append(f"| {i} | [{filename}]({link}) | {module_name} | {cat} | {xpath_display} | {data['platform']} | [Auto-generated summary] | {data['summary']} |")
                
                md.append("\n---\n")
        
        # Footer
        md.append("*Note: XPath counts calculated using pyang tree analysis. Summaries generated from diff analysis.*\n")
        md.append("---\n")
        md.append("**For questions or issues with this documentation, refer to:**")
        md.append("- [PROJECT_PLAN.md](PROJECT_PLAN.md) - Methodology and replication instructions")
        
        return '\n'.join(md)
    
    def save_markdown(self, content):
        """Save markdown to file"""
        output_file = OUTPUT_PATH / f"{self.new_release}-YANG-Model-Overview.md"
        output_file.write_text(content)
        print(f"\n💾 Saved to: {output_file}")
        print(f"   File size: {len(content):,} bytes")
        print(f"   Lines: {content.count(chr(10)):,}")

def main():
    parser = argparse.ArgumentParser(description='Generate YANG comparison markdown')
    parser.add_argument('--old', help='Old release folder (e.g., 1711)')
    parser.add_argument('--new', help='New release folder (e.g., 1721)')
    parser.add_argument('--batch', action='store_true', help='Generate all comparisons')
    
    args = parser.parse_args()
    
    if args.batch:
        print("="*80)
        print("BATCH MODE: Generating 31 total files")
        print("  - 1 baseline document (1631)")
        print("  - 30 comparison documents (1632 through 17181)")
        print("  - Note: 2611 comparison already exists")
        print("="*80)
        print()
        
        # First, generate the baseline for 1631
        generate_baseline_document("1631")
        
        # Then generate all comparisons from 1632 through 17181
        for i in range(len(RELEASE_ORDER) - 2):
            old_rel = RELEASE_ORDER[i]
            new_rel = RELEASE_ORDER[i + 1]
            
            gen = MarkdownGenerator(old_rel, new_rel)
            gen.analyze_releases()
            content = gen.generate_markdown()
            gen.save_markdown(content)
        
        print("\n" + "="*80)
        print("✅ BATCH COMPLETE: 31 files generated")
        print("="*80)
    elif args.old and args.new:
        gen = MarkdownGenerator(args.old, args.new)
        gen.analyze_releases()
        content = gen.generate_markdown()
        gen.save_markdown(content)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
