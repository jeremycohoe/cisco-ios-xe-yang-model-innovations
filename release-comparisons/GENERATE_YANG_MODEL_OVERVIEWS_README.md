# IOS XE YANG model release comparisons

## Overview

The [26.1.1 → 26.2.1 YANG overview](2621-YANG-Model-Overview.md) is the current source and saved-profile audit. Its supporting CSVs cover grouping, deviation, and augment deltas, platform applicability, modules newly listed by each profile, advertised feature changes, and changed deviation targets by profile. Use [NEXT-RELEASE-HANDOFF.md](NEXT-RELEASE-HANDOFF.md) for the next release audit.

The 31 earlier documents cover a v16.3.1 baseline and 30 historical comparisons. Their format and generation scripts predate the 26.2.1 audit. The source YANG folders are inputs and are not published here.

## Files in this Directory

- **NEXT-RELEASE-HANDOFF.md** - Current audit method, evidence boundaries, and next-release instructions
- **PROJECT_PLAN.md** - Historical planning context
- **PROGRESS_TRACKER.md** - Historical comparison status
- **scripts/** - Legacy generation and XPath-counting tools for earlier report formats
- **[VERSION]-YANG-Model-Overview.md** - Individual comparison/baseline files

## How to Read These Files

**Baseline (1631):** Complete inventory of all models in v16.3.1

**Comparison files:** Each compares two release snapshots
- Filename indicates the **newer** release
- Content shows **previous → current** changes
- Example: `1721-YANG-Model-Overview.md` = v17.1.1 → v17.2.1

## Chronological Order

**16.3.x - 16.9.x:** 1631 → 1632 → 1641 → 1651 → 1661 → 1662 → 1671 → 1681 → 1691 → 1693  
**16.10.x - 16.12.x:** 16101 → 16111 → 16121  
**17.1.x - 17.9.x:** 1711 → 1721 → 1731 → 1741 → 1751 → 1761 → 1771 → 1781 → 1791  
**17.10.x - 17.18.x:** 17101 → 17111 → 17121 → 17131 → 17141 → 17151 → 17161 → 17171 → 17181  
**26.1.1 → 26.2.1:** 2611 → 2621

See [PROGRESS_TRACKER.md](PROGRESS_TRACKER.md) for historical status. The current 26.2.1 overview and its CSVs are the source of record for that comparison.

## File Format

Earlier comparison documents may include:
- **Summary tables** by category (Configuration, Operational, RPC, Events, etc.)
- **XPath counts** and deltas for all models
- **Auto-generated highlights** showing significant additions/removals
- **What Changed** summaries from diff analysis
- **GitHub links** to source files, which may be unavailable; the current report keeps source filenames as plain text
- **Platform support** information (All Platforms, Wireless, ASR/ISR/NCS, etc.)

## Legacy generators

`scripts/generate_markdown.py`, `scripts/compare_releases.py`, and `scripts/count_xpaths.py` are retained for older comparisons. They do **not** reproduce the 26.2.1 overview or its seven supporting CSVs. In particular, the current report requires augment, feature, and saved-profile analysis beyond these scripts. Do not treat their XPath totals as resolved per-profile schema counts.

The following commands are historical examples for the older report format.

### Prerequisites for historical scripts
```bash
pip install pyang
```

### Historical single comparison
```bash
cd release-comparisons
python3 scripts/generate_markdown.py --old 1711 --new 1721
```

### Historical batch generation
```bash
cd release-comparisons
python3 scripts/generate_markdown.py --batch
```

### Historical analysis only
```bash
cd release-comparisons
python3 scripts/compare_releases.py --old 1711 --new 1721
```

## Methodology

See [NEXT-RELEASE-HANDOFF.md](NEXT-RELEASE-HANDOFF.md) for the current method. [PROJECT_PLAN.md](PROJECT_PLAN.md) retains historical project context, including:
- XPath counting approach
- Diff analysis techniques
- Model categorization logic
- GitHub link mapping

### Reference

- **Current comparison:** [2621-YANG-Model-Overview.md](2621-YANG-Model-Overview.md)
- **Next release:** [NEXT-RELEASE-HANDOFF.md](NEXT-RELEASE-HANDOFF.md)
