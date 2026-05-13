# IOS-XE YANG Model Release Comparisons

## Overview

Comprehensive YANG model comparison documentation tracking changes across all Cisco IOS-XE releases from 16.3.1 through 26.11.

**31 documents total:**
- 1 baseline (v16.3.1)
- 30 release comparisons
- Covers 16.x, 17.x, and 26.x series

## Files in this Directory

- **PROJECT_PLAN.md** - Detailed methodology and replication instructions
- **PROGRESS_TRACKER.md** - Status tracking for all comparison files
- **scripts/** - Python automation tools (pyang-based analysis)
- **[VERSION]-YANG-Model-Overview.md** - Individual comparison/baseline files

## How to Read These Files

**Baseline (1631):** Complete inventory of all models in v16.3.1

**Comparison files:** Each compares two consecutive releases
- Filename indicates the **newer** release
- Content shows **previous → current** changes
- Example: `1721-YANG-Model-Overview.md` = v17.1.1 → v17.2.1

## Chronological Order

**16.3.x - 16.9.x:** 1631 → 1632 → 1641 → 1651 → 1661 → 1662 → 1671 → 1681 → 1691 → 1693  
**16.10.x - 16.12.x:** 16101 → 16111 → 16121  
**17.1.x - 17.9.x:** 1711 → 1721 → 1731 → 1741 → 1751 → 1761 → 1771 → 1781 → 1791  
**17.10.x - 17.18.x:** 17101 → 17111 → 17121 → 17131 → 17141 → 17151 → 17161 → 17171 → 17181  
**26.11:** 2611

See [PROGRESS_TRACKER.md](PROGRESS_TRACKER.md) for detailed status.

## File Format

Each comparison document includes:
- **Summary tables** by category (Configuration, Operational, RPC, Events, etc.)
- **XPath counts** and deltas for all models
- **Auto-generated highlights** showing significant additions/removals
- **What Changed** summaries from diff analysis
- **GitHub links** to all YANG files
- **Platform support** information (All Platforms, Wireless, ASR/ISR/NCS, etc.)

## Generating Comparisons

### Prerequisites
```bash
pip install pyang
```

### Single Comparison
```bash
cd release-comparisons
python3 scripts/generate_markdown.py --old 1711 --new 1721
```

### Batch Generation (All 31 Files)
```bash
cd release-comparisons
python3 scripts/generate_markdown.py --batch
```

### Analysis Only (No Markdown)
```bash
cd release-comparisons
python3 scripts/compare_releases.py --old 1711 --new 1721
```

## Methodology

See [PROJECT_PLAN.md](PROJECT_PLAN.md) for detailed methodology including:
- XPath counting approach
- Diff analysis techniques
- Model categorization logic
- GitHub link mapping

### Reference

- **Template:** The 2611-YANG-Model-Overview.md in parent directory
- **Documentation:** See PROJECT_PLAN.md for detailed methodology
