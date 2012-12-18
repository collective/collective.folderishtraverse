Changelog
=========


1.6
---

- Use ``zExceptions.Redirect`` instead of ``request.response.redirect`` in
  traverse view. The Redirect exception redirects immediately instead of
  rendering the current page and submitting a transaction.commit() first.
  [rnix]


1.5
---

- Add ``NON_TRAVERSE_FALLBACK_VIEW``. May be patched if fallback view for
  ``folder_contents`` should differ from ``folder_summary_view``.
  [rnix]

- Check non-traversing fallback view against ``List folder contents``
  permission instead of anonymous.
  [rnix]


1.4 (2012-11-25)
----------------

- Show the "Display" content-menu also in the folder contents view on the Plone
  Site Root. The "Actions" menu is not displayed yet, since object_buttons are
  not registered for the Plone Site Root (copy, cut, rename and delete wouldn't
  make much sense on the portal object itself).
  [thet]


1.3 (2012-11-22)
----------------

- Show the Actions and Display content-menus also in folder content views.
  Allows Action submenu items like from c.folderorder and setting the display
  to something else than traverse_view.
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
