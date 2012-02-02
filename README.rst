Introduction
============

This package provides an view which traverses to the first item found in an
ordered container. The traversing/redirection happens only for anonymous users,
otherwise a view based on folder_listing is returned.

collective.folderishtraverse provides a traverse view for Folders. If selected,
the traversing to the first child of the folder happens. If the child's view is
also the traverse view, the traversing happens again, if possible.

collective.folderishtraverse is an alternative to a default page in Plone. The
difference is, that the target content is shown in the navigation tree and that
traversing to any nested content in any level of the tree's hierarchy is
possible.

Author
======

Johannes Raggam, BlueDynamics Alliance <raggam-nl@adm.at>
