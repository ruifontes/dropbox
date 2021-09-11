# -*- coding: utf-8 -*-
# Dropbox appModule for NVDA
# Improves accessibility of the Dropbox Metro app for Windows 8
# Copyright (C) 2015 Filaos, Patrick ZAJDA <patrick@zajda.fr> and other contributors
# Windows 8 compatibility contributed by David Parduhn <xkill85@gmx.net>
# This file is covered by the GNU General Public License.
# You can read the licence by clicking Help->Licence in the NVDA menu
# or by visiting http://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import addonHandler
import appModuleHandler
from NVDAObjects import UIA
import controlTypes

# We keep it in the case it would finally be necessary to change add-on summary by language
# _addonDir = os.path.join(os.path.dirname(__file__), "..").decode("mbcs")
# _curAddon = addonHandler.Addon(_addonDir)
# _addonSummary = _curAddon.manifest['summary']

# We initialize translations
addonHandler.initTranslation()
# We define roles to keep compatibility with nvda<2022.1
if hasattr(controlTypes, 'ROLE_STATICTEXT'):
	STATIC_TEXT = controlTypes.ROLE_STATICTEXT
else:
	STATIC_TEXT = controlTypes.Role.STATICTEXT
if hasattr(controlTypes, 'ROLE_LISTITEM'):
	LIST_ITEM = controlTypes.ROLE_LISTITEM
else:
	LIST_ITEM = controlTypes.Role.LISTITEM


# Class for Dropbox items in the metro app
class dropboxitem(UIA. ListItem):
	def _get_name(self):
		dbxList = list()
		obj = self.firstChild
		if obj.name != u'':
			dbxList.append(obj.name)
		while (obj != self.lastChild):
			if obj.role == STATIC_TEXT:
				if obj.name != u'':
					dbxList.append(obj.name)
			obj = obj.next
		return '; '.join(dbxList)


class AppModule(appModuleHandler.AppModule):
	# We set the scripts category shown on input gestures dialog
	# scriptCategory = unicode(_addonSummary)
	scriptCategory = u"Dropbox"

	def chooseNVDAObjectOverlayClasses(self, obj, CLSList):
		if obj.role == LIST_ITEM:
			CLSList.insert(0, dropboxitem)
