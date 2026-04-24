# Do Not Claim — Paper 13

1. **Do not cite Paper 13 as a proof source.** It indexes proofs; cite the actual proof location.

2. **Do not quote Paper 13's scorecard without checking the codebase.** Paper 13 revisions lag the canonical codebase. The authoritative count is `EXPECTED_THEOREM_COUNT` in `apf/bank.py`.

3. **Do not claim Paper 13 defines APF.** It is a reference, not an axiomatisation. Axioms are in Paper 1.

4. **Do not claim "Paper 13 proves X".** Paper 13 notes that X is proved elsewhere and maps X to a check function.

5. **Do not claim the module architecture table captures every Python file in the codebase.** It captures bank-registered modules. Non-registered modules (e.g. session_v63c.py, red_team.py) are listed separately.

6. **Do not claim 0 free parameters means APF predicts every physical quantity.** It means every structural claim is derived; open problems (Type B anchors for $m_t, m_b$, dark matter identity, etc) remain.

7. **Do not treat Appendix J as a full development history.** It is a chronological index of phase-completions; detailed session notes are in the `wiki/Log.md` and work plan.

8. **Do not claim Paper 13 is pedagogically the right entry point.** It is a reference. Pedagogical entry is Paper 0 (ontology) or Paper 1 (spine).

9. **Do not claim 340 checks in this repo = 340 theorems.** In full-codebase mode, 340 of the checks correspond to the full bank of theorems; in Paper-8-only mode, you would get 36.

10. **Do not claim Paper 13 is canonical over `apf/bank.py`.** When they disagree, the codebase is the source of truth.

11. **Do not overstate the Planck-units-native framing (§11).** It is a convention note, not a new derivation.

12. **Do not claim Paper 13 v8.6 is final.** Every codebase update triggers a Paper 13 revision; v8.6 is the current state, not the terminal state.
