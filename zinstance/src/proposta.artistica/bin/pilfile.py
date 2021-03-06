#!/usr/bin/python
#
# The Python Imaging Library.
# $Id$
#
# a utility to identify image files
#
# this script identifies image files, extracting size and
# pixel mode information for known file formats.  Note that
# you don't need the PIL C extension to use this module.
#
# History:
# 0.0 1995-09-01 fl   Created
# 0.1 1996-05-18 fl   Modified options, added debugging mode
# 0.2 1996-12-29 fl   Added verify mode
# 0.3 1999-06-05 fl   Don't mess up on class exceptions (1.5.2 and later)
# 0.4 2003-09-30 fl   Expand wildcards on Windows; robustness tweaks
#

from __future__ import print_function



import sys
sys.path[0:0] = [
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Plone-5.0.4-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Pillow-3.1.1-py2.7-linux-x86_64.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/src',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.robotframework-0.9.15-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/watchdog-0.8.3-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/robotframework_ride-1.3-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/robotframework_debuglibrary-0.3-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.testrunner-4.4.4-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.schema-4.4.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.i18n-3.7.4-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.configuration-3.7.4-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.component-3.9.5-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/setuptools-18.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/selenium-2.46.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/robotsuite-1.6.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/robotframework_selenium2library-1.6.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/robotframework-2.8.4-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.uuid-1.0.3-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.testing-4.1.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.testing-5.0.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/five.globalrequest-1.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Babel-1.3-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.PluggableAuthService-1.11.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.PlonePAS-5.0.9-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.MailHost-2.13.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.CMFPlone-5.0.4-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.CMFCore-2.2.10-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.contenttypes-1.2.11-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.dexterity-2.1.20-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/z3c.jbot-0.7.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.api-1.5-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.upgrade-1.3.24-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.openid-2.1.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.iterate-3.1.5-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.caching-1.2.10-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.CMFPlacefulWorkflow-1.6.5-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.ATContentTypes-2.2.11-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.Archetypes-1.10.13-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/pathtools-0.1.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/argh-0.26.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/PyYAML-3.12-py2.7-linux-x86_64.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Pygments-2.0.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.interface-3.6.7-py2.7-linux-x86_64.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.exceptions-3.6.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/six-1.10.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.event-3.5.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.i18nmessageid-3.5.3-py2.7-linux-x86_64.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/pytz-2015.7-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/unittest2-0.5.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/lxml-3.5.0-py2.7-linux-x86_64.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/docutils-0.12-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/decorator-4.0.9-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.publisher-3.12.6-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.lifecycleevent-3.6.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.browserpage-3.12.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.testing-3.9.7-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Zope2-2.13.24-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.GenericSetup-1.8.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.memoize-1.2.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/five.localsitemanager-2.0.5-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.dottedname-3.4.6-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.globalrequest-1.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.PluginRegistry-1.4-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.deprecation-3.4.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.session-3.5.6-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.protect-3.0.18-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.i18n-3.0.4-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.sendmail-3.7.5-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.deferredimport-3.5.3-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Persistence-2.13.2-py2.7-linux-x86_64.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/DocumentTemplate-2.13.2-py2.7-linux-x86_64.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/DateTime-4.0.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Acquisition-4.2.2-py2.7-linux-x86_64.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/AccessControl-3.0.12-py2.7-linux-x86_64.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.traversing-3.13.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.tales-3.5.3-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.tal-3.5.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.structuredtext-3.5.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.site-3.9.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.pagetemplate-3.6.3-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.location-3.9.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.container-3.11.2-py2.7-linux-x86_64.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.cachedescriptors-3.5.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.app.locales-3.6.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/z3c.autoinclude-0.3.5-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/transaction-1.1.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/slimit-0.8.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plonetheme.barceloneta-1.6.18-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.theme-3.0.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.schema-1.0.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.registry-1.0.3-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.portlets-2.2.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.portlet.static-3.0.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.portlet.collection-3.0.6-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.outputfilters-2.1.3-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.locking-2.1.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.intelligenttext-2.1.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.indexer-1.0.4-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.contentrules-2.0.5-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.browserlayer-2.1.6-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.batching-1.1.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.workflow-2.2.4-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.vocabularies-2.2.3-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.viewletmanager-2.0.9-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.uuid-1.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.users-2.3.5-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.theming-1.2.19-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.registry-1.3.11-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.redirector-1.3.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.portlets-3.1.3-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.locales-5.0.9-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.linkintegrity-3.0.4-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.layout-2.5.19-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.multilingual-3.0.16-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.i18n-3.0.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.folder-1.2.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.discussion-2.4.11-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.customerize-1.3.4-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.controlpanel-3.0.4-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.contentrules-4.0.10-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.contentmenu-2.1.7-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.contentlisting-1.2.4-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.content-3.0.20-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/mockup-2.1.4-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/five.pt-2.2.3-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/five.customerize-1.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/cssmin-0.2.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/borg.localrole-3.1.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/ZODB3-3.10.5-py2.7-linux-x86_64.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.statusmessages-4.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.contentmigration-2.1.12-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.ResourceRegistries-3.0.3-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.PortalTransforms-2.2.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.PlacelessTranslationService-2.0.5-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.PasswordResetTool-2.2.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.MimetypesRegistry-2.0.8-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.ExternalEditor-1.1.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.ExtendedPathIndex-3.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.DCWorkflow-2.2.4-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.CMFUid-2.2.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.CMFQuickInstallerTool-3.0.13-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.CMFEditions-2.2.19-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.CMFDynamicViewFTI-4.1.3-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.CMFDiffTool-3.0.4-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/ExtensionClass-4.1.2-py2.7-linux-x86_64.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.app.publication-3.12.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.ZSQLMethods-2.13.4-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.z3cform-1.2.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.lockingbehavior-1.0.3-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.versioningbehavior-1.2.7-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.namedfile-3.0.8-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.relationfield-1.3.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.dexterity-2.4.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.querystring-1.3.14-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.event-2.0.7-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/z3c.form-3.2.9-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.z3cform-0.8.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.supermodel-1.2.7-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.autoform-1.6.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.schemaeditor-2.0.9-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.rfc822-1.1.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.formwidget.namedfile-1.0.15-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.behavior-1.1.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.textfield-1.2.6-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.security-3.7.4-py2.7-linux-x86_64.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.ZCatalog-3.0.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.SecureMailHost-1.1.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.CMFFormController-3.0.5-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.ramcache-1.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.openid-2.0.4-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.viewlet-3.7.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.annotation-3.5.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/z3c.zcmlhook-1.0b1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.browserresource-3.10.3-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.cachepurging-1.0.11-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.caching-1.0.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/python_dateutil-2.4.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/ZConfig-2.9.3-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.validation-2.0.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.widgets-2.0.4-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.collection-1.1.6-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.blob-1.6.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.folder-1.0.7-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.datetime-3.4.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.contenttype-3.5.5-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.proxy-3.6.1-py2.7-linux-x86_64.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.browser-1.3-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.StandardCacheManagers-2.13.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.PythonScripts-2.13.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.MIMETools-2.13.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.ExternalMethod-2.13.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.BTreeFolder2-2.14.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.testbrowser-3.11.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.size-3.4.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.sequencesort-3.4.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.ptresource-3.9.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.processlifetime-1.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.contentprovider-3.7.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.browsermenu-3.9.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zLOG-2.11.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zExceptions-2.13.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zdaemon-2.0.7-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/tempstorage-2.12.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/initgroups-2.13.0-py2.7-linux-x86_64.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/ZopeUndo-2.12.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/RestrictedPython-3.6.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Record-2.13.0-py2.7-linux-x86_64.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.ZCTextIndex-2.13.5-py2.7-linux-x86_64.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.OFSP-2.13.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/MultiMapping-2.13.0-py2.7-linux-x86_64.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Missing-2.13.1-py2.7-linux-x86_64.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.formlib-4.0.6-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.keyring-3.0.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/collective.monkeypatcher-1.1.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/repoze.xmliter-0.6-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.transformchain-1.1.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Unidecode-0.4.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.broken-3.6.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.filerepresentation-3.6.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zc.buildout-2.4.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/ply-3.4-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.componentvocabulary-1.0.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/roman-1.4.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.subrequest-1.6.11-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.resourceeditor-2.0.5-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.resource-1.0.5-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/diazo-1.2.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/feedparser-5.2.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.intid-1.1.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/z3c.relationfield-0.7-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/archetypes.multilingual-3.0.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.stringinterp-1.1.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Chameleon-2.24-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/z3c.pt-3.0.0a1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/sourcecodegen-0.6.14-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zc.lockfile-1.0.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Markdown-2.6.5-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/python_gettext-3.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.ZopeVersionControl-1.1.3-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.copy-3.5.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.error-3.7.4-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.authentication-3.7.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/z3c.formwidget.query-0.12-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.app.file-3.6.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/five.intid-1.1.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.intid-3.7.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.synchronize-1.0.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.alterego-1.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.formwidget.recurrence-2.0.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.event-1.3-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/icalendar-3.9.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/collective.elephantvocabulary-0.2.5-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/Products.DateRecurringIndex-2.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.scale-1.4.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/python_openid-2.2.5-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/z3c.caching-2.0a1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/plone.app.imaging-2.0.3-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/archetypes.schemaextender-2.1.5-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/mechanize-0.2.5-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/future-0.15.2-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/cssselect-0.9.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zc.relation-1.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/z3c.objpath-1.1-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.dublincore-3.7.0-py2.7.egg',
  '/home/nil/plone_prova/zinstance/src/proposta.artistica/eggs/zope.keyreference-3.6.4-py2.7.egg',
  ]


import getopt
import glob
import logging
import sys

from PIL import Image

if len(sys.argv) == 1:
    print("PIL File 0.4/2003-09-30 -- identify image files")
    print("Usage: pilfile [option] files...")
    print("Options:")
    print("  -f  list supported file formats")
    print("  -i  show associated info and tile data")
    print("  -v  verify file headers")
    print("  -q  quiet, don't warn for unidentified/missing/broken files")
    sys.exit(1)

try:
    opt, args = getopt.getopt(sys.argv[1:], "fqivD")
except getopt.error as v:
    print(v)
    sys.exit(1)

verbose = quiet = verify = 0
logging_level = "WARNING"

for o, a in opt:
    if o == "-f":
        Image.init()
        id = sorted(Image.ID)
        print("Supported formats:")
        for i in id:
            print(i, end=' ')
        sys.exit(1)
    elif o == "-i":
        verbose = 1
    elif o == "-q":
        quiet = 1
    elif o == "-v":
        verify = 1
    elif o == "-D":
        logging_level = "DEBUG"

logging.basicConfig(level=logging_level)


def globfix(files):
    # expand wildcards where necessary
    if sys.platform == "win32":
        out = []
        for file in files:
            if glob.has_magic(file):
                out.extend(glob.glob(file))
            else:
                out.append(file)
        return out
    return files

for file in globfix(args):
    try:
        im = Image.open(file)
        print("%s:" % file, im.format, "%dx%d" % im.size, im.mode, end=' ')
        if verbose:
            print(im.info, im.tile, end=' ')
        print()
        if verify:
            try:
                im.verify()
            except:
                if not quiet:
                    print("failed to verify image", end=' ')
                    print("(%s:%s)" % (sys.exc_info()[0], sys.exc_info()[1]))
    except IOError as v:
        if not quiet:
            print(file, "failed:", v)
    except:
        import traceback
        if not quiet:
            print(file, "failed:", "unexpected error")
            traceback.print_exc(file=sys.stdout)
