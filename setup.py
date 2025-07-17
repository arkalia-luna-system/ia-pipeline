#!/usr/bin/env python3
"""
Setup script pour Athalia/Arkalia AI Pipeline
"""

from setuptools import setup, find_packages
import os

# Lire le README pour la description longue
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Lire les requirements
def read_requirements():
    requirements = []
    if os.path.exists("requirements.txt"):
        with open("requirements.txt", "r", encoding="utf-8") as fh:
            requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]
    return requirements

setup(
    name="athalia-ai",
    version="1.0.0",
    author="Arkalia Luna System",
    author_email="contact@arkalia-luna.com",
    description="Pipeline d'industrialisation IA pour génération automatique de projets",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/arkalia-luna-system/ia-pipeline",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.10",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
        "ai": [
            "anthropic>=0.7.0",
            "openai>=1.0.0",
        ],
        "dashboard": [
            "streamlit>=1.28.0",
            "plotly>=5.15.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "athalia=athalia_core.main:main",
            "athalia-cli=athalia_core.cli:main",
            "athalia-dashboard=athalia_core.dashboard:main",
        ],
    },
    include_package_data=True,
    package_data={
        "athalia_core": [
            "templates/*.py",
            "classification/*.py",
            "plugins/*.py",
        ],
    },
    keywords="ai, code-generation, automation, testing, documentation, ci-cd",
    project_urls={
        "Bug Reports": "https://github.com/arkalia-luna-system/ia-pipeline/issues",
        "Source": "https://github.com/arkalia-luna-system/ia-pipeline",
        "Documentation": "https://github.com/arkalia-luna-system/ia-pipeline/tree/main/docs-tech",
    },
) 