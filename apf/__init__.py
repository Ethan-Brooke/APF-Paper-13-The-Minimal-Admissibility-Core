"""APF v6.9 — Admissibility Physics Framework.

342 bank-registered theorems, 355 total verify_all checks. Zero postulates.

v6.9: PLEC formalization (2026-04-18).
  New apf/plec.py module with Regime R + five-type regime-exit taxonomy:
    Regime_R                 — R1..R4 joint validity; PLEC well-posedness.
    Regime_exit_Type_I       — collapse of admissible variation (saturation).
    Regime_exit_Type_II      — minimizer nonuniqueness (branching).
    Regime_exit_Type_III     — change of admissible class (record locking).
    Regime_exit_Type_IV      — loss of smooth / local structure.
    Regime_exit_Type_V       — pure representational redundancy.
  New A9_closure in apf/gravity.py unifying the Lovelock prerequisites
    A9.1..A9.5 (locality, covariance, conservation, second-order,
    propagation) dispersed across core/gravity/spacetime/internalization_geo.
  Papers 5/6 v2.0-PLEC now code-anchored (coderef pass complete).

v6.8: Canonicalization (2026-04-18).
  335 bank-registered / 348 verify_all; 18 modules; archive + naming discipline.

v6.7: Option 3 Work Plan — Phases 1–6 complete.
  Phase 1 (seesaw gap): L_seesaw_from_A1 [P] — 9-link chain, zero imports.
  Phase 2 (mass matrix): L_mass_from_capacity [P] — 11-link chain, zero FN.
    L_multiplicative_amplitude, L_Yukawa_bilinear, RT_FN_vs_capacity.
  Phase 3 (texture): L_texture_from_capacity [P] — 10-link chain, zero Fritzsch.
    L_GJ_from_capacity, RT_texture_chain.
  Phase 4 (bridges): L_bridges_closed [P] — all 5 bridges now theorems.
    RT_bridge_audit.
  Phase 5 (Theorem R): RT_R1/R2/R3 [P] — not circular, R3 rewritten.
  Phase 6 (NCG): L_NCG_status [P] — 11/11 items derived, zero physics imports.
    RT_NCG_no_physics_import. Long-term: derive formalism itself (math research).

v6.6: δ_PMNS resolution + DESI DR2 cosmological confrontation.
  L_seesaw_factorization, L_PMNS_CP_corrected, L_DESI_DR2_confrontation,
  L_joint_cosmo_neutrino, L_top_mass_hint.

v6.5: Down-sector closure + NNLO precision.
  L_Higgs_curvature_channel, L_NNLO_Fritzsch, L_sin2_oneloop, L_lepton_GJ.

v6.4: Gauge uniqueness + Weinberg angle Cauchy + CKM resolution.
"""
__version__ = '6.9'
