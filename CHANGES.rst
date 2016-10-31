Changes
=======

1.2 (unreleased)
-----------------

- Improve readability of traverse_view
  [jensens]

- Add browser-layer
  [jensens]

- Add basic testing.
  [jensens]

- Add integrated buildout for easier development.
  [jensens]

1.10 (2015-07-15)
-----------------

- normalize non-readable boolean expression.
  [jensens]

- Dont cache on instance to reduce write on reads.
  Cache volatile for 60min instead.
  [jensens]

- On traversing, don't check for the ``published`` workflow state but for
  content permissions.
  [thet]

- Use the plone.app.contenttypes folder listing view as fallback view, if
  available.
  [thet]


1.9 (2014-06-03)
----------------

- Add simplified Chinese translations.
  [jianaijun]

- Change permission needed to not beeing redirected to the first content item
  from ``List folder contents`` to ``Add portal content``. This is a better
  default, as only editors need not beeing redirected to be able to add and
  edit content.
  [thet]


1.8 (2014-05-02)
----------------

- Added Chinese Simplified translation.
  [jianaijun]

- Register views more generally to also support Dexterity based folderish
  types.
  [thet]

1.7 (2014-02-03)
----------------

- Redirect not only for anonymous users but all users not having the "List
  folder contents" permission on contexts with "traverse_view" enabled.
  [thet]


1.6.3 (2013-11-23)
------------------

- If no translation is found for a content item which' language doesn't match,
  continue with the next object in the folder instead of redirecting to the
  folder_summary_view.
  [thet]


1.6.2 (2013-04-23)
------------------

- Add "en" and "de" translations.
  [thet]


1.6.1 (2013-01-28)
------------------

- Do not try to translate object if no lang set.
  [rnix]


1.6 (2013-01-14)
----------------

- Consider translation in traverse_view if LinguaPlone is installed.
  [rnix]

- Add z3c.autoinclude.plugin entry point.
  [thet]


1.5.1 (2012-12-18)
------------------

- Use ``zExceptions.Redirect`` instead of ``request.response.redirect`` in
  traverse view. The Redirect exception redirects immediately instead of
  rendering the current page and submitting a transaction.commit() first.
  [rnix]


1.5 (2012-12-11)
----------------

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
