#!/usr/bin/env python
import sys

from setuptools import setup

try:
    from setuptools_rust import RustExtension, Binding
except ImportError:
    import subprocess

    errno = subprocess.call([sys.executable, "-m", "pip", "install", "setuptools-rust==1.5.2"])
    if errno:
        print("Please install setuptools-rust package")
        raise SystemExit(errno)
    else:
        from setuptools_rust import RustExtension

setup_requires = ["setuptools-rust==1.5.2", "wheel"]
install_requires = []

setup(
    name="ultrafeedparser",
    description="Minimal but fast feed parser for Python, partially written in Rust.",
    long_description=open('README.md').read(),
    version="0.1.2",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Rust",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
    ],
    packages=["ultrafeedparser"],
    rust_extensions=[RustExtension("ultrafeedparser.libultrafeedparser", binding=Binding.RustCPython)],
    install_requires=install_requires,
    setup_requires=setup_requires,
    include_package_data=True,
    zip_safe=False,
)
