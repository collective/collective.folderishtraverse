from Products.Five.browser import BrowserView
from plone.folder.interfaces import IFolder

from zope.component import getMultiAdapter

class TraverseView(BrowserView):

    @property
    def anonymous(self):
        portal_state = getMultiAdapter((self.context, self.request),
                                       name=u'plone_portal_state')
        return portal_state.anonymous()

    def __call__(self, *args, **kwargs):
        # TODO: only traverse to objects which are listed in typestolist.
        #       see adm.sfd.layout.browser.portlets.navigation.navtree_builder
        ctx = self.context
        if IFolder.providedBy(ctx) and self.anonymous:
            con = ctx.contentIds()
            if len(con):
                # TODO: reversing the listing must be configurable!
                obj = con[-1]
                url = ctx[obj].absolute_url()

        if not url:
            # TODO: must this be a redirect? or can folder_summary_view
            #       retrieved somehow else - like PageTemplateView, etc.?
            url = '%s/folder_summary_view' % ctx.absolute_url()
        return self.request.response.redirect(url)
