#!/usr/bin/env python3
"""
XPath Counter Utility for YANG Models

Counts configuration/operational XPaths in YANG files using pyang tree analysis.
This matches the counting methodology used in the comparison documents.

Usage:
    python3 count_xpaths.py <yang_file>
    python3 count_xpaths.py --dir <directory>
    python3 count_xpaths.py --compare <old_file> <new_file>
"""

import sys
import subprocess
import re
from pathlib import Path
import argparse

def count_xpaths(yang_file):
    """
    Count XPaths in a YANG file using pyang tree output.
    
    Equivalent shell command:
    pyang -f tree --tree-depth=99 file.yang 2>/dev/null | \
        grep -E "^\s*[+|]" | grep -E "(rw|ro|x|--)" | wc -l
    
    Returns:
        int: Number of XPaths (data nodes) in the YANG file
    """
    try:
        result = subprocess.run(
            ["pyang", "-f", "tree", "--tree-depth", "99", str(yang_file)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=30
        )
        
        if result.returncode != 0:
            return None
        
        count = 0
        for line in result.stdout.split('\n'):
            # Match lines starting with whitespace followed by + or |
            if re.match(r'^\s*[+|]', line):
                # Check for node indicators (rw, ro, x, or --)
                if any(indicator in line for indicator in ['rw', 'ro', 'x', '--']):
                    count += 1
        
        return count
        
    except subprocess.TimeoutExpired:
        print(f"ERROR: Timeout counting {yang_file}", file=sys.stderr)
        return None
    except FileNotFoundError:
        print("ERROR: pyang not found. Install with: pip install pyang", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return None

def count_directory(directory, pattern="*.yang"):
    """Count XPaths for all YANG files in a directory."""
    path = Path(directory)
    if not path.is_dir():
        print(f"ERROR: {directory} is not a directory", file=sys.stderr)
        return
    
    print(f"Counting XPaths in {directory}...")
    print(f"{'File':<50} {'XPaths':>10}")
    print("=" * 62)
    
    total = 0
    for yang_file in sorted(path.glob(pattern)):
        count = count_xpaths(yang_file)
        if count is not None:
            print(f"{yang_file.name:<50} {count:>10}")
            total += count
        else:
            print(f"{yang_file.name:<50} {'ERROR':>10}")
    
    print("=" * 62)
    print(f"{'TOTAL':<50} {total:>10}")

def compare_files(old_file, new_file):
    """Compare XPath counts between two versions of a YANG file."""
    old_path = Path(old_file)
    new_path = Path(new_file)
    
    print(f"Comparing: {old_path.name}")
    print("-" * 50)
    
    old_count = count_xpaths(old_path)
    new_count = count_xpaths(new_path)
    
    if old_count is None or new_count is None:
        print("ERROR: Could not count XPaths")
        return
    
    delta = new_count - old_count
    delta_sign = "+" if delta > 0 else ""
    
    print(f"Old version: {old_count:>6} XPaths")
    print(f"New version: {new_count:>6} XPaths")
    print(f"Delta:       {delta_sign}{delta:>6} XPaths")
    print(f"Format:      {delta_sign}{delta} / {new_count}")

def main():
    parser = argparse.ArgumentParser(
        description='Count XPaths in YANG models',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Count XPaths in a single file
  python3 count_xpaths.py Cisco-IOS-XE-native.yang
  
  # Count all YANG files in a directory
  python3 count_xpaths.py --dir /path/to/yang/files
  
  # Compare two versions
  python3 count_xpaths.py --compare old/native.yang new/native.yang
        """
    )
    
    parser.add_argument('file', nargs='?', help='YANG file to analyze')
    parser.add_argument('--dir', help='Directory containing YANG files')
    parser.add_argument('--compare', nargs=2, metavar=('OLD', 'NEW'),
                       help='Compare XPath counts between two files')
    
    args = parser.parse_args()
    
    if args.compare:
        compare_files(args.compare[0], args.compare[1])
    elif args.dir:
        count_directory(args.dir)
    elif args.file:
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"ERROR: File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        
        count = count_xpaths(file_path)
        if count is not None:
            print(f"{file_path.name}: {count} XPaths")
        else:
            print(f"ERROR: Could not count XPaths in {file_path.name}", file=sys.stderr)
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
