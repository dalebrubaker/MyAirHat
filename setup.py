"""Setup configuration for MyAirHat package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="myairhat",
    version="0.1.0",
    author="Clean Air Hats Organization",
    author_email="info@cleanairhats.org",
    description="Open-source technical package generator for MyAirHat™ respiratory protection device",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dalebrubaker/MyAirHat",
    project_urls={
        "Bug Tracker": "https://github.com/dalebrubaker/MyAirHat/issues",
        "Documentation": "https://www.cleanairhats.org",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Manufacturing",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        # Add dependencies here as needed
        # "reportlab>=3.6.0",  # For PDF generation
        # "pillow>=9.0.0",     # For image processing
        # "svgwrite>=1.4.0",   # For SVG pattern generation
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "ruff>=0.1.0",
            "mypy>=1.0.0",
            "black>=23.0.0",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "myairhat=myairhat.main:main",
        ],
    },
)