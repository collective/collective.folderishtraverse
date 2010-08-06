from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='collective.folderishtraverse',
      version=version,
      description="Traverse to first item in folder",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone view',
      author='Johannes Raggam',
      author_email='raggam-nl@adm.at',
      url='http://github.com/thet/collective.forlderishtraverse',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      )
