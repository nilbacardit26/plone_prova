# -*- coding: utf-8 -*-
from plone.app.content.browser.contents import ContentsBaseAction
from plone.app.content.interfaces import IStructureAction
from Products.CMFPlone import PloneMessageFactory as _
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component.hooks import getSite
from zope.i18n import translate
from zope.interface import implementer


@implementer(IStructureAction)
class TagsAction(object):

    template = ViewPageTemplateFile('templates/tags.pt')
    order = 6

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def get_options(self):
        site = getSite()
        base_url = site.absolute_url()
        base_vocabulary = '%s/@@getVocabulary?name=' % base_url
        return {
            'title': translate(_('Tags'), context=self.request),
            'id': 'tags',
            'icon': 'tags',
            'url': self.context.absolute_url() + '/@@fc-tags',
            'form': {
                'template': self.template(
                    vocabulary_url='%splone.app.vocabularies.Keywords' % (
                        base_vocabulary)
                    )
            }
        }


class TagsActionView(ContentsBaseAction):
    required_obj_permission = 'Modify portal content'
    success_msg = _('Successfully updated tags on items')
    failure_msg = _('Failed to modify tags on items')

    def action(self, obj):
        toadd = self.request.form.get('toadd')
        if toadd:
            toadd = set(toadd.split(','))
        else:
            toadd = set([])
        toremove = self.request.get('toremove')
        if toremove:
            toremove = set(toremove.split(','))
        else:
            toremove = set([])
        tags = set(obj.Subject())
        tags = tags - toremove
        tags = tags | toadd
        obj.setSubject(list(tags))
        obj.reindexObject()
