from Products.Five.browser import BrowserView
from plone.folder.interfaces import IFolder
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import utils
from zope.component import getMultiAdapter

class TraverseView(BrowserView):

    @property
    def anonymous(self):
        portal_state = getMultiAdapter((self.context, self.request),
                                       name=u'plone_portal_state')
        return portal_state.anonymous()

    def __call__(self, *args, **kwargs):
        ctx = self.context
        wft = getToolByName(ctx, 'portal_workflow')
        types = utils.typesToList(ctx)
        url = None
        if self.anonymous:
            def find_endpoint(obj):
                if not IFolder.providedBy(obj): return obj
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
        if ctx.defaultView() == 'traverse_view':
            return super(TraverseView, self).__call__(*args, **kwargs)
        else:
            url = ctx.absolute_url()
            return self.request.response.redirect(url)
