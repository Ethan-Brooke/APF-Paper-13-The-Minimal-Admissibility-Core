from setuptools import setup, find_packages

setup(
    name="apf",
    version="6.9.0",
    description="Admissibility Physics Framework — machine-verifiable theorem bank (v6.9 PLEC formalization)",
    author="E.S. Brooke / Admissible Technologies",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20",
        "scipy>=1.7",
    ],
    # v6.9 PLEC formalization (2026-04-18):
    #   - 19 bank-registered modules (+ apf/plec.py new); 24 verify_all modules;
    #   - 342 bank-registered theorems; 355 total verify_all checks;
    #   - 48 quantitative predictions, 0 free parameters;
    #   - 7 new PLEC-infrastructure checks: Regime_R, Regime_exit_Type_I..V,
    #     A9_closure (unified Lovelock-prerequisite chain);
    #   - depends on numpy + scipy.
)
