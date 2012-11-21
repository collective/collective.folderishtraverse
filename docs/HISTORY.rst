Changelog
=========

1.3dev (unreleased)
-------------------

- Show the Actions and Display content-menus also in folder listings. Allows
  Action submenu items like from c.folderorder and setting the display to
  something else than traverse_view.
  [thet]

- Add statusmessage for when displaying the traverse_view for non-anonymous
  users.
  [thet]

- When no endpoint is found, redirect to folder_summary_view for anonymous
  users. folder_contents needs higher permissions.
  [thet]

1.2 (2012-11-07)
----------------

- For non-anonymous users or if no endpoint was found, redirect to
  folder_contents. This view is generally nicer and more usable.
  [thet]

1.1 (2012-02-20)
----------------

- Allow the traverse_view also on the Plone Site itself.
  [thet]

1.0 (2012-02-02)
----------------

- Initial release
