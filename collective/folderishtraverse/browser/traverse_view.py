# -*- coding: utf-8 -*-
#
# GNU General Public License (GPL)
#
from Products.Five.browser import BrowserView
from plone.folder.interfaces import IFolder

from AccessControl import getSecurityManager

class TraverseView(BrowserView):

    @property
    def anonymous(self):
        # TODO: is there a plone view global var for that?
        return getSecurityManager().getUser().getUserName() == 'Anonymous User'

    def __call__(self, *args, **kwargs):
        # TODO: only traverse to objects which are listet in typestolist.
        #       see adm.sfd.layout.browser.portlets.navigation.navtree_builder
        if IFolder.providedBy(self.context) and self.anonymous:
            if len(self.context.contentIds()):
                # TODO: reversing the listing must be configurable!
                obj = self.context.contentIds()[-1]
                url = self.context[obj].absolute_url()
                return self.request.response.redirect(url)

        # TODO: must this be a redirect? or can folder_summary_view retrieved
        #       somehow else - like PageTemplateView, etc.?
        url = self.context.absolute_url() + '/folder_summary_view'
        return self.request.response.redirect(url)
