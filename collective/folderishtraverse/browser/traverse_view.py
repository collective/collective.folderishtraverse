from zExceptions import Redirect
from zope.component import getMultiAdapter
from zope.i18nmessageid import MessageFactory
from AccessControl import getSecurityManager
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import utils
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from Products.Five.browser import BrowserView
from Products.statusmessages.interfaces import IStatusMessage
from plone.folder.interfaces import IFolder


_ = MessageFactory('collective.folderishtraverse')


# XXX: maybe make this a registry entry?
NON_TRAVERSE_FALLBACK_VIEW = 'folder_summary_view'


class TraverseView(BrowserView):

    @property
    def anonymous(self):
        portal_state = getMultiAdapter((self.context, self.request),
                                       name=u'plone_portal_state')
        return portal_state.anonymous()

    @property
    def permitted(self):
        sm = getSecurityManager()
        return sm.checkPermission('List folder contents', self.context)

    def __call__(self, *args, **kwargs):
        ctx = self.context
        wft = getToolByName(ctx, 'portal_workflow')
        types = utils.typesToList(ctx)
        url = None

        if self.anonymous:
            def find_endpoint(obj):
                if not IFolder.providedBy(obj) and\
                   not IPloneSiteRoot.providedBy(obj): return obj
                contents = obj.contentIds()
                # TODO: make list reversable
                for id in contents:
                    child = obj[id]

                    # only traverse to published objects
                    try:
                        state = wft.getInfoFor(child, 'review_state')
                    except:
                        state = None
                    if not state == 'published': continue

                    # only traverse to objects listed in typesToList
                    if child.portal_type not in types: continue

                    # we've found a published object, which can be used as
                    # possible endpoint, except it has 'traverse_view' enabled
                    obj = child
                    if child.defaultView() == 'traverse_view':
                        obj = find_endpoint(child)
                    break
                return obj
            ctx = find_endpoint(ctx)

        url = ctx.absolute_url()
        if ctx.defaultView() == 'traverse_view':
            if not self.permitted:
                # Not allowed to list folder contents. Show fallback.
                url = '%s/%s' % (url, NON_TRAVERSE_FALLBACK_VIEW)
            else:
                # List folder contents permitted. Show folder_contents.
                url = '%s/folder_contents' % url
                messages = IStatusMessage(self.request)
                messages.addStatusMessage(
                    _("traverse_view-statusmessage",
                      u"""This is a traverse view. Anonymous users are
                          redirected to the first subitem in this
                          directory."""),
                     type="info")
        raise Redirect(url)
