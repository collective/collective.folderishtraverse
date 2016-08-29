# -*- coding: utf-8 -*-
from AccessControl import getSecurityManager
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import utils
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from Products.Five.browser import BrowserView
from Products.statusmessages.interfaces import IStatusMessage
from plone.folder.interfaces import IFolder
from zExceptions import Redirect
from zope.i18nmessageid import MessageFactory

try:
    from Products.LinguaPlone.interfaces import ITranslatable
    LINGUA_PLONE_INSTALLED = True
except ImportError:
    LINGUA_PLONE_INSTALLED = False
try:
    import plone.app.contenttypes  # noqa
    PAC_INSTALLED = True
except ImportError:
    PAC_INSTALLED = False


_ = MessageFactory('collective.folderishtraverse')


# XXX: maybe make this a registry entry?
NON_TRAVERSE_FALLBACK_VIEW = 'folder_summary_view'
if PAC_INSTALLED:
    NON_TRAVERSE_FALLBACK_VIEW = '@@summary_view'

EDITOR_PERMISSION = 'Add portal content'
VIEW_PERMISSION = 'View'


class TraverseView(BrowserView):

    def permitted(self, context=None, permission=EDITOR_PERMISSION):
        if not context:
            context = self.context
        sm = getSecurityManager()
        return sm.checkPermission(permission, context)

    def find_endpoint(self, obj, lang, types_to_list):
        if not (
            IFolder.providedBy(obj) or IPloneSiteRoot.providedBy(obj)
        ):
            return obj
        contents = obj.contentIds()
        # TODO: make list reversable
        for cid in contents:
            child = obj[cid]
            # try to get translation if LinguaPlone is installed, child
            # is translatable and child language does not match lang
            if LINGUA_PLONE_INSTALLED:
                if ITranslatable.providedBy(child):
                    child_lang = child.Language()
                    # child lang can be empty string, only try to
                    # translate if explicit lang
                    if child_lang and child_lang != lang:
                        translation = child.getTranslation(lang)
                        if not translation:
                            continue  # ...with next obj in folder
                        child = translation
            # only traverse to allowed objects
            allowed = self.permitted(
                context=child,
                permission=VIEW_PERMISSION
            )
            if not allowed:
                continue
            # only traverse to objects listed in typesToList
            if child.portal_type not in types_to_list:
                continue
            # we've found a published object, which can be used as
            # possible endpoint, except it has 'traverse_view' enabled
            obj = child
            if child.defaultView() == 'traverse_view':
                obj = self.find_endpoint(child, lang, types_to_list)
            break
        return obj

    def __call__(self, *args, **kwargs):
        ctx = self.context
        url = None
        if not self.permitted():
            types_to_list = utils.typesToList(ctx)
            plt = getToolByName(self.context, 'portal_languages')
            pref_lang = plt.getPreferredLanguage()
            ctx = self.find_endpoint(ctx, pref_lang, types_to_list)
        url = ctx.absolute_url()
        if ctx.defaultView() == 'traverse_view':
            if not self.permitted(context=ctx):
                # Not allowed to list folder contents. Show fallback.
                url = '%s/%s' % (url, NON_TRAVERSE_FALLBACK_VIEW)
            else:
                # List folder contents permitted. Show folder_contents.
                url = '%s/folder_contents' % url
                messages = IStatusMessage(self.request)
                messages.addStatusMessage(
                    _("traverse_view-statusmessage",
                      u"""This is a traverse view. Users who are not allowed to
                          see the folder listing are redirected to the first
                          subitem in this directory."""),
                    type="info")
        raise Redirect(url)
