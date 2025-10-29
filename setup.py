"""Setup configuration for FINCOUNT."""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="fincount",
    version="0.1.0",
    author="FINCOUNT Development Team",
    author_email="support@fincount.example.com",
    description="Enterprise-grade financial accounting software",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Alexic12/Software_Contable",
    project_urls={
        "Bug Tracker": "https://github.com/Alexic12/Software_Contable/issues",
        "Documentation": "https://github.com/Alexic12/Software_Contable/docs",
        "Source Code": "https://github.com/Alexic12/Software_Contable",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial :: Accounting",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
    python_requires=">=3.8",
    install_requires=[
        # Production dependencies will be added here
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.7.0",
            "flake8>=6.1.0",
            "mypy>=1.5.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "fincount=fincount:init",
        ],
    },
)
