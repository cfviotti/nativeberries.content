# -*- coding: utf-8 -*-

from five import grok
from nativeberries.content import _
from nativeberries.content.interfaces import ICarousel
from plone.dexterity.content import Item


class Carousel(Item):
    """Represent a carousel."""
    grok.implements(ICarousel)

