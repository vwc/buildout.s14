from five import grok
from plone import api
from DateTime.DateTime import DateTime

from plone.app.contentlisting.interfaces import IContentListing
from plone.event.interfaces import IEvent
from plone.app.contenttypes.interfaces import IDocument
from vwc.blog.blogentry import IBlogEntry


class FrontPageView(grok.View):
    grok.context(IDocument)
    grok.require('zope2.View')
    grok.name('frontpage-view')

    def update(self):
        self.has_events = len(self.recent_events()) > 0
        self.has_blogentries = len(self.blogentries()) > 0

    def blogentries(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        items = catalog(object_provides=IBlogEntry.__identifier__,
                        review_state='published',
                        sort_on='effective',
                        sort_order='reverse',
                        sort_limit=2)[:2]
        results = IContentListing(items)
        return results

    def recent_events(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        items = catalog(object_provides=IEvent.__identifier__,
                        review_state='published',
                        end={'query': DateTime(),
                             'range': 'min'},
                        sort_on='start',
                        sort_limit=4)[:4]
        results = IContentListing(items)
        return results
