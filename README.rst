Introduction
============

This package provides an view which traverses to the first item found in an
ordered container. If the default view of the item, which the traverse view is
traversing to is also a traverse view, the traversing happens again to the next
sub-sub-item in the sub-folder, if possible.

The traversing/redirection is only done for users who are not allowed to see
the folder listing of the current context (usally anonymous users and normal
members). For users with higher permissions, a folder contents view is shown.
This way, members can easily edit the folder without beeing redirected to
another folder.

collective.folderishtraverse is an alternative to a default page in Plone. The
difference is, that the target content is shown in the navigation tree and that
traversing to any nested content in any level of the tree's hierarchy is
possible.

Author
======

Johannes Raggam, BlueDynamics Alliance <raggam-nl@adm.at>
