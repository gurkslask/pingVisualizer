#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    "braillegraph"
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pingVisualizer',
    version='0.1.0',
    description='Visualizes ping responses in braillcurves',
    long_description=readme + '\n\n' + history,
    author='Alexander Svensson',
    author_email='gurkslask@gmail.com',
    url='https://github.com/gurkslask/pingVisualizer',
    packages=[
        'pingVisualizer',
    ],
    package_dir={'pingVisualizer':
                 'pingVisualizer'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='pingVisualizer',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: Swedish',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
