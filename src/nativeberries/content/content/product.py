# -*- coding: utf-8 -*-

from five import grok
from nativeberries.content import _
from nativeberries.content.interfaces import IProduct
from plone.dexterity.content import Item


class Product(Item):
    """Represent a product."""
    grok.implements(IProduct)

