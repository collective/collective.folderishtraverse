from setuptools import setup, find_packages

version = '1.6.3'

setup(name='collective.folderishtraverse',
      version=version,
      description="Traverse to first item in folder",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.rst").read(),
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
          'Products.CMFCore',
          'Products.CMFPlone',
          'Products.statusmessages',
          'Zope2', # For Products.Five
          'plone.folder',
          'zope.component',
          'zope.i18nmessageid',
          # this could be optional, if needed
          'plone.memoize',
          'plone.app.contentmenu',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
