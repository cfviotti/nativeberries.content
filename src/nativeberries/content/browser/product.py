# -*- coding: utf-8 -*-

from five import grok
from nativeberries.content.interfaces import IProduct
from plone.directives import form
from plone.directives import dexterity
from z3c.form import field

grok.templatedir('templates')


class Product_View(dexterity.DisplayForm):
    grok.context(IProduct) 
    grok.require('zope2.View')
    grok.name('view')

