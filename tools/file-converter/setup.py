from setuptools import setup, find_packages

setup(
    name="dirfmt-converter",
    version="0.1.0",
    description="Convert between file formats: md/html, csv/json from the command line",
    py_modules=["converter"],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": ["dconvert=converter:main"],
    },
    install_requires=["markdown"],
    classifiers=["Topic :: Utilities"],
)