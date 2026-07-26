from setuptools import setup, find_packages

setup(
    name="dirfmt-backup",
    version="0.1.0",
    description="Simple CLI backup tool with ZIP compression support",
    py_modules=["backup"],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": ["dbackup=backup:main"],
    },
    classifiers=["Topic :: System :: Archiving"],
)