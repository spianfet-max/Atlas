# Atlas

Bond portfolio builder for the UGM team. Load the bond universe from Excel (or CSV); everything runs in the browser and the file is never uploaded.

1. **Macro backdrop and stance**: OECD leading indicator, US CPI, US 2Y and curve, JGB curve, VIX, high yield vs Treasuries (Keel). Simple rules turn them into a stance on duration, curve, credit, callables and floaters; every part can be overridden. "Apply stance to the builder" sets the builder limits.
2. **Universe**: filters, a yield/spread/expected-return vs duration map coloured by rating, rich/cheap against a curve fitted to each currency × rating band, a sortable table and a bond detail panel with 12-month breakevens.
3. **Expected return in the base currency (unhedged)**: yield + roll-down, then FX unchanged, as the forward, or your views.
4. **Builder**: keeps locked bonds (added by hand), fills the rest by rank under limits (bonds, duration, rating, high-yield %, sector %, currency %, maturity, size outstanding, minimum piece, one bond per issuer, perpetuals, callables), then swaps to meet the duration target. Editable weights, cash-flow ladder, mix, checks, Excel export.
5. **Scenarios**: rates by currency, IG/HY spreads, FX against the base; seven editable presets.

## Files

```
index.html     for work: self-contained, the Excel reader (SheetJS 0.18.5) is inlined, opens from a local file or GitHub Pages
artifact.html  the same page for claude.ai (SheetJS from cdnjs)
build.py       rebuilds both from src/ and vendor/
src/           page, house style (core.css/js), macro snapshot (sample.json)
vendor/        xlsx.full.min.js (SheetJS Community Edition 0.18.5, Apache 2.0)
```

Column names are matched automatically (Bloomberg export names included: ISIN, Issuer Name, Crncy, Cpn, Maturity, BBG Composite, RTG_MOODY, Ask Yld to Worst, OAS, Mod Dur, Industry Sector, Cntry of Risk, Payment Rank, Mty Typ, Nxt Call Dt, Cpn Typ, Min Piece, Amt Out, Ask Price). Fix any in the matching panel; the choice is remembered for files with the same headers.

Without Keel (e.g. at work behind the firewall) the macro panel shows a dated snapshot and the stance can be set by hand; the universe, builder and scenarios work the same.
