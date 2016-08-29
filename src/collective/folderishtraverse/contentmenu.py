# -*- coding: utf-8 -*-
from plone.app.contentmenu.menu import ActionsSubMenuItem
from plone.app.contentmenu.menu import DisplaySubMenuItem
from plone.memoize import volatile
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import utils

import time


def _cache_key(method, self):
    return time.time() // (60 * 60)  # cache for 60 min


class AlwaysActionsSubMenuItem(ActionsSubMenuItem):
    """Show the Actions contentmenu also in folder_contents views.
    """

    @volatile.cache(_cache_key, volatile.store_on_context)
    def available(self):
        actions_tool = getToolByName(self.context, 'portal_actions')
        editActions = actions_tool.listActionInfos(
            object=self.context,
            categories=('object_buttons',),
            max=1)
        return len(editActions) > 0


class AlwaysDisplaySubMenuItem(DisplaySubMenuItem):
    """Show the Display contentmenu also in folder_contents views.
    """

    @volatile.cache(_cache_key, volatile.store_on_context)
    def disabled(self):
        context = self.context
        if self.context_state.is_default_page():
            context = utils.parent(context)
        return (
            getattr(context, 'isPrincipiaFolderish', False) and
            'index_html' in context.objectIds()
        )
