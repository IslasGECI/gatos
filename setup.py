from setuptools import setup, find_packages

setup(
    name="gatos",
    version="0.2.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires = [
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "crea_tamagno_poblacion_gatos = gatos.generaTamanioPoblacionGatos:cli",
            "crea_tabla_pvalor = gatos.tabla_p_valor_erradicacion_gatos:cli"
        ]
    }
)
