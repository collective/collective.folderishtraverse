from plone.memoize.instance import memoize
#from plone.app.content.browser.interfaces import IContentsPage

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import utils

from plone.app.contentmenu.menu import ActionsSubMenuItem
from plone.app.contentmenu.menu import DisplaySubMenuItem

class AlwaysActionsSubMenuItem(ActionsSubMenuItem):

    @memoize
    def available(self):

        actions_tool = getToolByName(self.context, 'portal_actions')
        editActions = actions_tool.listActionInfos(
                object=self.context,
                categories=('object_buttons',),
                max=1)
        #if IContentsPage.providedBy(self.request) and\
        #    [it for it in editActions
        #            if it['id'] not in ('cut', 'copy', 'paste')]:
        #    return False
        return len(editActions) > 0


class AlwaysDisplaySubMenuItem(DisplaySubMenuItem):

    @memoize
    def disabled(self):

        #if IContentsPage.providedBy(self.request):
        #    return True
        context = self.context
        if self.context_state.is_default_page():
            context = utils.parent(context)
        if not getattr(context, 'isPrincipiaFolderish', False):
            return False
        elif 'index_html' not in context.objectIds():
            return False
        else:
            return True
