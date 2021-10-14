from setuptools import setup, find_packages

setup(
    name="gatos",
    version="0.2.2",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "Click",
        "geci_plots @ git+https://github.com/IslasGECI/geci_plots.git@v0.4.0",
        "matplotlib",
        "metadatatools @ git+https://git@github.com/IslasGECI/metadata_tools@v0.2.2",
        "numpy",
        "pandas",
        "pymc3"
    ],
    entry_points={
        "console_scripts": [
            "crea_tamagno_poblacion_gatos = gatos.generaTamanioPoblacionGatos:cli",
            "crea_tabla_pvalor = gatos.tabla_p_valor_erradicacion_gatos:cli",
        ]
    },
)
