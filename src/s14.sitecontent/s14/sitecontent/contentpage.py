from five import grok

from z3c.form import group, field
from zope import schema

from plone.dexterity.content import Container
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.interfaces import IImageScaleTraversable


from s14.sitecontent import MessageFactory as _


class IContentPage(form.Schema, IImageScaleTraversable):
    """
    Folderish Content Pages
    """
    text = RichText(
        title=_(u"Body Text"),
        required=False,
    )


class ContentPage(Container):
    grok.implements(IContentPage)


class View(grok.View):
    grok.context(IContentPage)
    grok.require('zope2.View')
    grok.name('view')
