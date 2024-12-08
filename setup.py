# setup.py
from setuptools import setup, find_packages

setup(
    name="anar",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'torch>=1.9.0',
        'transformers>=4.15.0',
        'camel-tools>=1.2.0',
        'networkx>=2.6.3',
        'numpy>=1.19.5',
        'pandas>=1.3.3',
        'scikit-learn>=0.24.2',
        'arabic-reshaper>=2.1.3',
        'python-bidi>=0.4.2',
        'neo4j>=4.4.0',
    ],
    author="Mossab Ibrahim",
    author_email="mibrahim@ucm.es",
    description="Arabic Narrative Analysis and Recognition System",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Mossab82/arabic_narratives",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
