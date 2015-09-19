# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from plone import api

class Utils(BrowserView):
    """View do Produto"""


    def returnContent(self, sort_on='created', sort_order='reverse', review_state='published', **kw):
        """Return data from catalog."""
        catalog = api.portal.get_tool('portal_catalog')
        return catalog.searchResults(sort_on=sort_on,
                                                 sort_order=sort_order,
                                                 review_state=review_state,
                                                 **kw)


