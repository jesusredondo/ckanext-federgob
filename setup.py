from setuptools import setup, find_packages
import sys, os

version = '1'

setup(
    name='ckanext-federgob',
    version=version,
    description="Extension to federate the catalog with datos.gob.",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Jesus Redondo Garcia',
    author_email='redondogarciajesus@gmail.com',
    url='http://opendata.caceres.es',
    license='CC-BY-4.0',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.federgob'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        federgob=ckanext.federgob.plugin:federgobPlugin
    ''',
)
