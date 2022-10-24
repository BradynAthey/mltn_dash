from setuptools import find_packages, setup

setup(
    name="mltn",
    version="0.0.0",
    description="MLTN: Machine Learning TransitioN toolkit",
    author="",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "pytest",
        "dash",
        "pandas",
        "jupyter",
        "matplotlib",
        "joblib",
        "dash_cytoscape",
    ],
)
