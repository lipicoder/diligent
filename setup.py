"""Setup configuration for the package."""
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
import versioneer

# pylint: disable=invalid-name
long_desc = """diligent is a markdown and file serve based on cloud storage"""

requires = ["fastapi", "click", "wareroom"]

setup(
    name="diligent",
    url="https://github.com/lipicoder/diligent",
    author="lipi",
    author_email="lipicoder@qq.com",
    version = versioneer.get_version(),
    cmdclass = versioneer.get_cmdclass(),
    description="diligent is a markdown and file serve based on cloud storage",
    long_description=long_desc,
    zip_safe=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
)
