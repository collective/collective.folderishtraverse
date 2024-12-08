# -*- coding: utf-8 -*-
from AccessControl import getSecurityManager
from Products.CMFPlone import utils
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from Products.Five.browser import BrowserView
from plone.folder.interfaces import IFolder
from zExceptions import Redirect


NON_TRAVERSE_FALLBACK_VIEW = '@@summary_view'
VIEW_PERMISSION = 'View'


class TraverseView(BrowserView):

    def permitted(self, context=None, permission=VIEW_PERMISSION):
        if not context:
            context = self.context
        sm = getSecurityManager()
        return sm.checkPermission(permission, context)

    def find_redirection_target(self, obj, types_to_list):
        if not (
            IFolder.providedBy(obj) or IPloneSiteRoot.providedBy(obj)
        ):
            return obj

        contents = obj.contentIds()

        for cid in contents:
            child = obj[cid]

            # Only traverse to allowed objects
            if not self.permitted(context=child):
                continue

            # Only traverse to objects listed in typesToList
            if child.portal_type not in types_to_list:
                continue

            # We've found a published object, which can be used as possible
            # redirection target.
            obj = child

            # ... except it has 'traverse_view' enabled
            if child.defaultView() == 'traverse_view':
                obj = self.find_redirection_target(child, types_to_list)

            break
        return obj

    def __call__(self):

        # Find redirection target.
        context = self.context
        types_to_list = utils.typesToList(context)
        context = self.find_redirection_target(context, types_to_list)
        url = context.absolute_url()

        # Fallback - e.g. no valid context found or no items in folder.
        if context.defaultView() == 'traverse_view':
            url = '%s/%s' % (url, NON_TRAVERSE_FALLBACK_VIEW)

        self.request.response.setHeader("Location", url)
        self.request.response.setStatus(302)
        return Redirect(url)
