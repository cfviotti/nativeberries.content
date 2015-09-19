# -*- coding: utf-8 -*-

from five import grok
from nativeberries.content import _
from nativeberries.content.interfaces import IRecipe
from plone.dexterity.content import Item


class Recipe(Item):
    """Represent a recipe."""
    grok.implements(IRecipe)

