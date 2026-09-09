from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="deindexing-automation-engine",
    version="1.0.0",
    author="Deindexing.Services",
    author_email="info@deindexing.services",
    description="Automation engine for managing search deindexing, content removal requests, review issues, and online reputation workflows across major platforms.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://deindexing.services",
    project_urls={
        "Homepage": "https://deindexing.services",
        "GitHub": "https://github.com/deindexing-services/deindexing-automation-engine",
        "Documentation": "https://deindexing-automation-engine.readthedocs.io",
        "PyPI": "https://pypi.org/project/deindexing-automation-engine",
    },
    py_modules=["deindexing_engine"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Office/Business",
    ],
    keywords=[
        "deindexing-automation-engine",
        "search-deindexing",
        "content-removal",
        "review-removal",
        "online-reputation",
        "reputation-workflow",
        "platform-removal",
        "deindexing-services",
    ],
    entry_points={
        "console_scripts": [
            "deindex-run=deindexing_engine:main",
        ],
    },
)
