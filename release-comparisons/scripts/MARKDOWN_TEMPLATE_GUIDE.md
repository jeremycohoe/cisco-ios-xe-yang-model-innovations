# Markdown File Structure Template

This document describes the standardized structure for release comparison markdown files.

## File Structure

```markdown
# Title: All YANG Model Changes: v[OLD] → v[NEW]
**Summary: X New Models & Y Updated Models**
*Generated: [DATE]*

---

## NEW Models Summary (X models)
[Table with category breakdown and XPath counts]

---

## UPDATED Models Summary (Y models)
[Table with category breakdown and estimated changes]

---

## Key Highlights - NEW Models
[Organized by functional area with bullet points]

---

## Key Highlights - UPDATED Models
[Most significant updates organized by category]

---

## Summary Statistics  ← PLACED HERE (before detailed model listings)

### Release v[NEW] Totals:
- Total YANG Files
- New/Modified/Deleted counts
- XPath totals

### Major Categories:
[Breakdown by feature area]

### Platform Support:
[Platform coverage summary]

---

# NEW YANG Models in v[NEW]
[Detailed tables organized by model type]

## NEW Configuration Models
[Full table with XPath counts]

## NEW Operational Models
[Full table with XPath counts]

## NEW RPC Models
[Full table with XPath counts]

## NEW Event Notification Models
[Full table with XPath counts]

## NEW Other Models
[Full table with XPath counts]

---

# UPDATED YANG Models: v[OLD] → v[NEW]
[Detailed tables for key updated models]

## UPDATED Configuration Models (Sample - Key Models)
[Table with XPath deltas and "What Changed"]

## UPDATED Operational Models (Sample - Key Models)
[Table with XPath deltas and "What Changed"]

## UPDATED RPC Models (Sample - Key Models)
[Table with XPath deltas and "What Changed"]

## UPDATED Native Augmenting Models (Sample - Key Models)
[Table with XPath deltas and "What Changed"]

## UPDATED Wireless Models (Sample)
[Table with XPath deltas and "What Changed"]

## UPDATED Type Definitions & Deviations (Sample)
[Table showing minor changes]

## UPDATED OpenConfig & IETF Models (Sample)
[Table showing standard model updates]

---

## Additional UPDATED Models
[Bulleted list of remaining models with minor changes]

---

*Note: [Methodology note]*

---

**For questions or issues...**
[Links to supporting docs]
```

## Why Summary Statistics is Placed Early

The Summary Statistics section is positioned **after Key Highlights but before detailed model listings** because:

1. **Quick Reference** - Readers get high-level numbers before diving into details
2. **Context** - Provides scope before 300+ lines of detailed tables
3. **Logical Flow** - Overview → Highlights → Statistics → Details
4. **Template Consistency** - Matches the 2611 structure pattern

## Why Some Models Are Listed vs Tabled

### Detailed Tables (First ~20-30 models per category)
- **Key/high-impact models** get full table entries with:
  - XPath counts or deltas
  - Platform support
  - Detailed "What Changed" summaries
  
### Bulleted Lists (Remaining models)
- **Minor updates** are listed because:
  - Full details would add 100+ table rows
  - These typically have description/constraint changes only
  - Keeps document readable and focused
  - Maintains file size manageable

### When to Use Which

**Use Detailed Tables For:**
- All NEW models (always important)
- Top 10-15 most changed UPDATED models
- Models with significant XPath deltas (>10)
- Critical infrastructure models (native, interfaces, crypto, bgp, etc.)

**Use Bulleted Lists For:**
- Models with minor changes
- Description/validation updates only
- Models already covered in other sections
- Type definitions with minimal impact

## XPath Counting Methodology

### Command
```bash
pyang -f tree --tree-depth=99 file.yang 2>/dev/null | \
    grep -E "^\s*[+|]" | \
    grep -E "(rw|ro|x|--)" | \
    wc -l
```

### What It Counts
- Configuration nodes (rw - read-write)
- Operational nodes (ro - read-only)
- RPC/action nodes (x - execute)
- Structural nodes with children (--)

### What It Excludes
- Comments
- Imports/includes
- Type definitions (unless they create nodes)
- Module headers

### Python Implementation
See `scripts/count_xpaths.py` for reusable utility.

## Generating "What Changed" Summaries

### Approach
1. **Run diff** between old and new versions
2. **Parse changes** looking for:
   - Added/removed nodes (leaf, container, list)
   - New imports
   - Enum additions
   - Must constraint additions
   - Description changes
3. **Summarize** in 1-2 sentences focusing on:
   - Quantitative changes (X new nodes)
   - Qualitative impact (enhanced validation)
   - User-facing features

### Example Analysis
```python
# See scripts/compare_releases.py analyze_diff() method
changes = {
    'added_nodes': ['leaf new-feature', 'container stats'],
    'added_imports': ['Cisco-IOS-XE-types'],
    'added_enums': ['new-state-value'],
    'must_statements': 2
}

# Generates: "Added 2 new data nodes; imported Cisco-IOS-XE-types; 
#             enhanced validation constraints"
```

## File Naming Convention

**Pattern:** `[NEWER_VERSION]-YANG-Model-Overview.md`

**Examples:**
- `1721-YANG-Model-Overview.md` - Compares 1711 → 1721
- `17181-YANG-Model-Overview.md` - Compares 17171 → 17181
- `2611-YANG-Model-Overview.md` - Compares 17181 → 2611

**Always use the NEWER release as the filename** because:
- Clear which release is documented
- Chronological ordering in directory listings
- GitHub links point to the newer release
