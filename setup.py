#!/usr/bin/env python
import sys
from distutils.core import setup

setup_args = {}

setup_args.update(dict(
    name='param',
    version="1.2.1",
    description='Declarative Python programming using Parameters.',
    long_description=open('README.rst').read(),
    author= "IOAM",
    author_email= "developers@topographica.org",
    maintainer= "IOAM",
    maintainer_email= "developers@topographica.org",
    platforms=['Windows', 'Mac OS X', 'Linux'],
    license='BSD',
    url='http://ioam.github.com/param/',
    packages = ["param","numbergen"],
    provides = ["param","numbergen"],
    classifiers = [
        "License :: OSI Approved :: BSD License",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries"]
))



if __name__=="__main__":

    if 'upload' in sys.argv:
        import param, numbergen
        param.__version__.verify()
        numbergen.__version__.verify()
        assert str(param.__version__) == setup_args['version']
        assert str(numbergen.__version__) == setup_args['version']

    setup(**setup_args)
