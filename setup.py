"""Setup script."""

from setuptools import find_packages, setup

# Requirements definitions
SETUP_REQUIRES = [
    "setuptools",
]

INSTALL_REQUIRES = [
    "matplotlib",
    "numpy",
    "tqdm",
    "faker",
    "pandas",
]

EXTRAS_REQUIRE = {
    "develop": [
        "black",
        "isort",
        "flake8",
        "autopep8",
        "pre-commit",
        "versioneer",
    ],
}

# https://pypi.org/classifiers/
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3.11",
    "Environment :: CPU",
    "Topic :: Scientific/Engineering",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

setup(
    name="GeneratorExcersice",
    version=0.1,
    description=("GeneratorExcersice"),
    license="MIT License",
    author="Søren Langkilde",
    url="https://github.com/soeren97/GeneratorExcersice",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    setup_requires=SETUP_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    classifiers=CLASSIFIERS,
)
