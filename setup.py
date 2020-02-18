from setuptools import setup, find_packages

setup(
    name="gatos",
    version="0.2.0",
    packages=find_packages() ,
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "crea_tamagno_poblacion_gatos = gatos.generaTamanioPoblacionGatos:cli",
            "crea_tabla_pvalor = gatos.tabla_p_valor_erradicacion_gatos:cli"
        ]
    },
    install_requires = [
        "Click"
    ]
)
