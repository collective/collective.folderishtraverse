# -*- coding: utf-8 -*-
#
# GNU General Public License (GPL)
#
from Products.Five.browser import BrowserView
from plone.folder.interfaces import IFolder

class TraverseView(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request
        import pdb;pdb.set_trace()
        if IFolder.providedBy(self.context):
            return self.request.response

    def __call__(self, *args, **kwargs):
        return u''