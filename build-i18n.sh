#!/bin/sh
I18NDUDE=bin/i18ndude
I18NPATH=collective/folderishtraverse
DOMAIN=collective.folderishtraverse
$I18NDUDE rebuild-pot --pot $I18NPATH/locales/$DOMAIN.pot --create $DOMAIN $I18NPATH
$I18NDUDE sync --pot $I18NPATH/locales/$DOMAIN.pot $I18NPATH/locales/*/LC_MESSAGES/$DOMAIN.po

DOMAIN=plone
$I18NDUDE rebuild-pot --pot $I18NPATH/locales/$DOMAIN.pot --merge $I18NPATH/locales/merge-plone.pot --create $DOMAIN $I18NPATH
$I18NDUDE sync --pot $I18NPATH/locales/$DOMAIN.pot $I18NPATH/locales/*/LC_MESSAGES/$DOMAIN.po
