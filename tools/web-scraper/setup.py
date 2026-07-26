from setuptools import setup, find_packages

setup(
    name="dirfmt-scraper",
    version="0.1.0",
    description="Quick CLI web scraper for extracting text and links from any URL",
    py_modules=["scraper"],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": ["dscraper=scraper:main"],
    },
    classifiers=["Topic :: Internet :: WWW/HTTP"],
)