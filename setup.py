# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup


version = "1.2"

setup(
    name="collective.folderishtraverse",
    version=version,
    description="Traverse to first item in folder",
    long_description=(open("README.rst").read() + "\n" + open("CHANGES.rst").read()),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python",
    ],
    keywords="plone view",
    author="Johannes Raggam",
    author_email="thetetet@gmail.com",
    url="http://github.com/collective/collective.forlderishtraverse",
    license="GPL",
    packages=find_packages("src"),
    namespace_packages=["collective"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "plone.app.contentmenu",
        "plone.folder",
        "plone.memoize",
        "Products.CMFCore",
        "Products.CMFPlone",
        "Products.statusmessages",
        "setuptools",
        "zope.component",
        "zope.i18nmessageid",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            "plone.testing>=5.0.0",
            "plone.app.contenttypes",
            "plone.app.robotframework[debug]",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
