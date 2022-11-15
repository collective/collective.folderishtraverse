# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup


version = "1.11"

setup(
    name="collective.folderishtraverse",
    version=version,
    description="Traverse to first item in folder",
    long_description=(open("README.rst").read() + "\n" + open("CHANGES.rst").read()),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
    keywords="plone view",
    author="Johannes Raggam",
    author_email="raggam-nl@adm.at",
    url="http://github.com/collective/collective.forlderishtraverse",
    license="GPL",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["collective"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "plone.folder",
        "Products.CMFCore",
        "Products.CMFPlone",
        "Products.statusmessages",
        "setuptools",
        "zope.component",
        "zope.i18nmessageid",
        "Zope2",  # For Products.Five
        # this could be optional, if needed
        "plone.app.contentmenu",
        "plone.memoize",
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
