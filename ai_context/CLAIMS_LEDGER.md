# Claims Ledger — Paper 13

Paper 13 makes meta-claims (counts, indexes, scorecards) rather than structural claims.

| # | Claim | Status | Source | Failure mode |
|---|---|---|---|---|
| 1 | 420 bank-registered theorems at v8.6 | verifiable | canonical codebase `apf/bank.py` | `EXPECTED_THEOREM_COUNT` drift |
| 2 | 437 verify_all checks | verifiable | `verify_all.py MODULES` | module list drift |
| 3 | 34 registered modules + `apf/standalone/` | verifiable | `_MODULE_PATHS` | import path drift |
| 4 | 48 quantitative predictions | tally | prediction scorecard | prediction count re-categorisation |
| 5 | 32/39 within 3σ | empirical tally | prediction scorecard | PDG update |
| 6 | 0 free parameters | structural | architecture-level | free parameter identified |
| 7 | Every theorem in the index traces to a check function | provenance | `theorems.json` | orphan theorem in text |
| 8 | Module architecture table | descriptive | `apf/bank.py` | module missing from table |
| 9 | Dependency graph in §12 | descriptive | `derivation_graph.json` | missing dependency edge |
| 10 | Appendix J version-history entries | chronological | Paper 13 Old/ archive | archive out of sync |

## Attack surface priority

Claims 1-3 are most commonly out of sync when AI agents quote Paper 13 — the canonical codebase ticks forward faster than Paper 13 revisions. Always verify scorecard counts against the actual `EXPECTED_THEOREM_COUNT` in `apf/bank.py` before citing.

---

*340 bank-registered checks verify this paper's coderef content in full-codebase mode (the largest bundle of any paper repo).*
