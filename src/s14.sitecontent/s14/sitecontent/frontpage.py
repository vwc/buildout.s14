from five import grok
from plone import api

from plone.app.layout.navigation.interfaces import INavigationRoot
from plone.app.contentlisting.interfaces import IContentListing

from vwc.blog.blogentry import IBlogEntry


class FrontPageView(grok.View):
    grok.context(INavigationRoot)
    grok.require('zope2.View')
    grok.name('frontpage-view')

    def update(self):
        self.has_blogenties = len(self.blogentries()) > 0

    def blogentries(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        results = catalog(object_provides=IBlogEntry.__identifier__,
                          review_state='published',
                          sort_on='effectve',
                          sort_limit=2)[:2]
        items = IContentListing(results)
        return items
