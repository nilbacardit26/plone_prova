# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
import logging
from zope.formlib.widgets import RadioWidget
from proposta.artistica import _
from zope.schema import Bool
from zope import schema
from zope.schema import List, Float
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from plone.autoform import directives as form
from plone.supermodel import model
from z3c.form.browser import checkbox





class IPropostaArtisticaLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

def _createAmbitVocabulary():
    ambits = ["Audiovisuals", "Circ", "Exposició/Fotografia/Arts plàstiques",
              "Dansa", "Jocs/Videojocs", "Música", "Narració de contes", "Poesia", "Teatre"]
    for i,ambit in enumerate(ambits):
        term = SimpleTerm(value=i, token=str(i), title=ambit)
        yield term

# Construct SimpleVocabulary objects of log level -> name mappings
ambit_vocabulary = SimpleVocabulary(list(_createAmbitVocabulary()))

def _createAltresAmbitVocabulary():
    altres_ambits = ["Audiovisuals", "Circ", "Exposició/Fotografia/Arts plàstiques",
                     "Dansa", "Jocs/Videojocs", "música", "Narració de contes", "Poesia",
                     "Projecte comunitari/Social","Teatre"]

    for i,ambit in enumerate(altres_ambits):
        term = SimpleTerm(value=i, token=str(i), title=ambit)
        yield term

ambit_vocabulary = SimpleVocabulary(list(_createAmbitVocabulary()))
altres_ambits = SimpleVocabulary(list(_createAltresAmbitVocabulary()))
englova_items = SimpleVocabulary.fromItems((
    (u"Si_token", "Sí"),
    (u"No_token", "No")))

def validateAccept(value):
    if value == 'Sí':
        value = 'No'
        return value

class IPropostaArtistica(Interface):

    title = schema.TextLine(
        title=_(u"Nom de l'espectacle"),
        required=True
    )

    form.widget(englova=CheckBoxFieldWidget)
    englova= schema.Choice(vocabulary=englova_items,
        title=u"L'espectacle s'englova en més d'un àmbit?"
    )
    
    ambits = schema.Choice(vocabulary=ambit_vocabulary,
        title=u"Àmbit Principal",
        default=False
    )

    altres_ambits = schema.Choice(vocabulary=altres_ambits,
        title=u"Altres Àmbits",
        default=False,
    )

    form.widget(estrena_absoluta=CheckBoxFieldWidget)
    estrena_absoluta= schema.Choice(vocabulary=englova_items,
        title=u"Estrena absoluta durant la fira?",
    )

    form.widget(estrena_espanyol=CheckBoxFieldWidget)
    estrena_espanyol= schema.Choice(vocabulary=englova_items,
        title=u"Estrena a l'estat espanyol?",
    )
    
    form.widget(estrena_catalunya=checkbox.CheckBoxFieldWidget)
    estrena_catalunya= schema.Choice(vocabulary=englova_items,
        title=u"Estrena a Catalunya?",
        constraint = validateAccept,
                                     
    )

    nombre = schema.Int(
        title=_(u"Nombre de persones que s'han de desplaçar"),
        required=True,
    )




