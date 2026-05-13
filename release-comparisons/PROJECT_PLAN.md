# YANG Release Comparison Project Plan

**Project:** Generate comprehensive YANG model comparison documentation for all IOS-XE releases  
**Created:** May 6, 2026  
**Status:** In Progress - Phase 1 (Sample Generation)

---

## 📋 Project Overview

### Goal
Create detailed markdown documentation comparing YANG models between consecutive IOS-XE releases, following the format established in `2611-YANG-Model-Overview.md`.

### Scope
- **Total Releases:** 32 folders
- **Total Comparison Files:** 31 markdown files
- **Release Categories:** 16.x, 17.x, 26.x series
- **Output Location:** `release-comparisons/` folder

---

## 📂 Folder Structure

```
release-comparisons/
├── PROJECT_PLAN.md                    # This file
├── PROGRESS_TRACKER.md                # Progress checklist
├── scripts/
│   ├── compare_releases.py            # Main automation script
│   ├── count_xpaths.py                # XPath counting utility
│   ├── analyze_diff.py                # YANG diff analyzer
│   └── generate_markdown.py           # Markdown generator
├── 16111-YANG-Model-Overview.md       # 16.10.1 → 16.11.1
├── 16121-YANG-Model-Overview.md       # 16.11.1 → 16.12.1
├── 1631-YANG-Model-Overview.md        # 16.12.1 → 16.3.1
├── ...
├── 1721-YANG-Model-Overview.md        # 17.1.1 → 17.2.1
├── ...
├── 17181-YANG-Model-Overview.md       # 17.17.1 → 17.18.1
└── 2611-YANG-Model-Overview.md        # 17.18.1 → 26.11 (COMPLETED)
```

---

## 🗂️ Release Order (Chronological)

### 16.x Series
1. 16101 (16.10.1) - Baseline
2. 16111 (16.11.1) → Compare with 16101
3. 16121 (16.12.1) → Compare with 16111
4. 1631 (16.3.1) → Compare with 16121
5. 1632 (16.3.2) → Compare with 1631
6. 1641 (16.4.1) → Compare with 1632
7. 1651 (16.5.1) → Compare with 1641
8. 1661 (16.6.1) → Compare with 1651
9. 1662 (16.6.2) → Compare with 1661
10. 1671 (16.7.1) → Compare with 1662
11. 1681 (16.8.1) → Compare with 1671
12. 1691 (16.9.1) → Compare with 1681
13. 1693 (16.9.3) → Compare with 1691

### 17.x Series
14. 1711 (17.1.1) → Compare with 1693
15. 1721 (17.2.1) → Compare with 1711
16. 1731 (17.3.1) → Compare with 1721
17. 1741 (17.4.1) → Compare with 1731
18. 1751 (17.5.1) → Compare with 1741
19. 1761 (17.6.1) → Compare with 1751
20. 1771 (17.7.1) → Compare with 1761
21. 1781 (17.8.1) → Compare with 1771
22. 1791 (17.9.1) → Compare with 1781
23. 17101 (17.10.1) → Compare with 1791
24. 17111 (17.11.1) → Compare with 17101
25. 17121 (17.12.1) → Compare with 17111
26. 17131 (17.13.1) → Compare with 17121
27. 17141 (17.14.1) → Compare with 17131
28. 17151 (17.15.1) → Compare with 17141
29. 17161 (17.16.1) → Compare with 17151
30. 17171 (17.17.1) → Compare with 17161
31. 17181 (17.18.1) → Compare with 17171

### 26.x Series
32. apoorva-261 (26.11) → Compare with 17181 ✅ **COMPLETED**

---

## 📝 File Naming Convention

- **Pattern:** `[NEWER_VERSION]-YANG-Model-Overview.md`
- **Examples:**
  - `16111-YANG-Model-Overview.md` (compares 16101 → 16111)
  - `1721-YANG-Model-Overview.md` (compares 1711 → 1721)
  - `2611-YANG-Model-Overview.md` (compares 17181 → 2611) ✅

---

## 🔧 Technical Approach

### Phase 1: Sample Generation (CURRENT)
1. ✅ Create project structure
2. 🔄 Generate 2 sample files:
   - `1721-YANG-Model-Overview.md` (17.1.1 → 17.2.1)
   - `1731-YANG-Model-Overview.md` (17.2.1 → 17.3.1)
3. ✅ Review and finalize workflow

### Phase 2: Full Automation
1. Create comprehensive comparison script
2. Process all 31 comparisons
3. Validate and review outputs

### Phase 3: Quality Assurance
1. Verify hyperlinks to GitHub
2. Validate XPath counts
3. Review "What Changed" descriptions

---

## 🛠️ Analysis Methodology

### 1. File Detection
```bash
# Identify new, modified, and deleted files
comm -23 <(ls newer_release/ | sort) <(ls older_release/ | sort)  # New files
comm -12 <(ls newer_release/ | sort) <(ls older_release/ | sort)  # Common files
comm -13 <(ls newer_release/ | sort) <(ls older_release/ | sort)  # Deleted files
```

### 2. XPath Counting
```bash
# Using pyang to count configuration nodes
pyang -f tree --tree-depth=99 [file.yang] 2>/dev/null | grep -c "^\s*[+|]"
```

### 3. Diff Analysis
```bash
# Generate unified diff
diff -u older_release/file.yang newer_release/file.yang

# Parse for:
# - Added nodes (leaf, container, list)
# - Removed nodes
# - Modified descriptions
# - New imports
# - Enum additions
# - Must constraints
```

### 4. Change Summarization
- Extract meaningful changes from diff
- Categorize by impact (configuration, operational, etc.)
- Calculate XPath deltas (+X / Y total)
- Generate 1-2 sentence summary

### 5. Platform Detection
- Parse capability XML files if available
- Default to "All Platforms" if >50% support
- Platform-specific for targeted models

---

## 📊 Output Format

Each markdown file follows this structure:

```markdown
# All YANG Model Changes: v[OLD] → v[NEW]
**Summary: X New Models & Y Updated Models**
*Generated: [DATE]*

## NEW Models Summary (X models)
| Category | Count | XPaths |
|----------|-------|--------|
| Configuration | X | Y |
| Operational | X | Y |
| RPC | X | Y |
| Events | X | Y |

## UPDATED Models Summary (Y models)
| Category | Count | XPath Changes |
|----------|-------|---------------|
| Configuration | X | +Y |
| Operational | X | +Y |
| Native | X | +Y |

## Key Highlights - NEW Models
[Organized by functional area]

## Key Highlights - UPDATED Models
[Top changes by impact]

## Detailed Tables
### NEW Configuration Models
| # | YANG Model | Type | XPaths | Platforms | Summary |
|---|------------|------|--------|-----------|---------|

### UPDATED Configuration Models  
| # | YANG Model | Type | XPaths | Platforms | Summary | What Changed |
|---|------------|------|--------|-----------|---------|--------------|
```

---

## 🔗 GitHub Link Format

All YANG model links point to the newer release folder:

```markdown
[Cisco-IOS-XE-native.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/[RELEASE_FOLDER]/Cisco-IOS-XE-native.yang)
```

**Examples:**
- For 1721 comparison: `...xe/1721/file.yang`
- For 17181 comparison: `...xe/17181/file.yang`
- For 2611 comparison: `...xe/2611/file.yang` (uses apoorva-261 → 2611 mapping)

---

## 📈 Progress Tracking

See [PROGRESS_TRACKER.md](PROGRESS_TRACKER.md) for detailed checklist.

**Current Status:** 1 of 31 files completed (3%)

---

## 🔄 Replication Instructions

### Prerequisites
```bash
# Install required tools
brew install pyang  # macOS
# or
pip install pyang

# Python 3.8+
python3 --version
```

### Manual Process (For Single Comparison)

1. **Identify Release Pair**
   ```bash
   OLD_RELEASE="1711"
   NEW_RELEASE="1721"
   ```

2. **Find New Files**
   ```bash
   cd /Users/sdeweese/github/yang/vendor/cisco/xe
   comm -23 <(ls ${NEW_RELEASE}/*.yang | xargs -n1 basename | sort) \
            <(ls ${OLD_RELEASE}/*.yang | xargs -n1 basename | sort) \
            > new_files_${NEW_RELEASE}.txt
   ```

3. **Find Modified Files**
   ```bash
   for file in ${NEW_RELEASE}/*.yang; do
       filename=$(basename "$file")
       if [ -f "${OLD_RELEASE}/${filename}" ]; then
           if ! diff -q "${OLD_RELEASE}/${filename}" "${NEW_RELEASE}/${filename}" > /dev/null; then
               echo "$filename"
           fi
       fi
   done > modified_files_${NEW_RELEASE}.txt
   ```

4. **Count XPaths**
   ```bash
   # For a single file
   pyang -f tree --tree-depth=99 ${NEW_RELEASE}/file.yang 2>/dev/null | \
       grep -E "^\s*[+|].*[+-]rw|[+-]ro|[+-]x" | wc -l
   ```

5. **Analyze Changes**
   ```bash
   diff -u ${OLD_RELEASE}/file.yang ${NEW_RELEASE}/file.yang | \
       grep "^[+-]" | grep -E "(leaf|container|list|import|enum)"
   ```

6. **Generate Markdown**
   - Use template from `2611-YANG-Model-Overview.md`
   - Fill in data from analysis
   - Update hyperlinks to correct release folder

### Automated Process (Using Scripts)

```bash
cd /Users/sdeweese/github/yang/vendor/cisco/xe/release-comparisons

# Run comparison for specific release
python3 scripts/compare_releases.py --old 1711 --new 1721

# Or process all releases
python3 scripts/compare_releases.py --all
```

---

## 🎯 Success Criteria

Each markdown file must include:
- ✅ Accurate file counts (new, modified, deleted)
- ✅ XPath counts for all models
- ✅ XPath deltas for modified models (+X / Y total)
- ✅ "What Changed" summaries (1-2 sentences)
- ✅ Working GitHub hyperlinks
- ✅ Platform support information
- ✅ Categorized by model type
- ✅ Key highlights section
- ✅ Follows 2611 format exactly

---

## 🐛 Known Issues & Considerations

1. **XPath Counting Variations**
   - Different pyang versions may yield slightly different counts
   - Groupings and augments affect counts
   - Document the pyang version used

2. **Platform Detection**
   - Not all releases have capability XML files
   - May need to infer from model naming/comments

3. **Change Analysis Accuracy**
   - Diff-based analysis may miss semantic changes
   - Focus on structural changes (nodes, imports, enums)

4. **GitHub Link Mapping**
   - apoorva-261 folder maps to 2611 in GitHub
   - Verify other folder name mappings

---

## 📚 Reference Materials

- **Template:** `../2611-YANG-Model-Overview.md`
- **Existing Scripts:**
  - `../analyze_yang_changes.py`
  - `../count_xpaths_pyang.sh`
  - `../update_table_with_changes.py`
- **YANG Resources:**
  - [RFC 7950 - YANG 1.1](https://datatracker.ietf.org/doc/html/rfc7950)
  - [pyang Documentation](https://github.com/mbj4668/pyang)

---

## 👤 Project Contacts

**Owner:** sdeweese  
**Last Updated:** May 6, 2026  
**Next Review:** After Phase 1 completion

---

## ✅ Next Steps

1. Generate 2 sample files (1721, 1731)
2. Review with stakeholder
3. Iterate on format/content
4. Build full automation
5. Process remaining 29 files
6. Final QA and validation
