from plone.memoize.instance import memoize
#from plone.app.content.browser.interfaces import IContentsPage

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import utils

from plone.app.contentmenu.menu import ActionsSubMenuItem
from plone.app.contentmenu.menu import DisplaySubMenuItem


class AlwaysActionsSubMenuItem(ActionsSubMenuItem):
    """Show the Actions contentmenu also in folder_contents views.
    """

    @memoize
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

    @memoize
    def disabled(self):
        context = self.context
        if self.context_state.is_default_page():
            context = utils.parent(context)
        if not getattr(context, 'isPrincipiaFolderish', False):
            return False
        elif 'index_html' not in context.objectIds():
            return False
        else:
            return True
