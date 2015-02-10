# -*- coding: utf-8 -*-
# Dropbox appModule for NVDA
# Improves accessibility of the Dropbox Metro app for Windows 8
# Copyright (C) 2015 Filaos, Patrick ZAJDA <patrick@zajda.fr> and other contributors
# Windows 8 compatibility contributed by David Parduhn <xkill85@gmx.net>
# This file is covered by the GNU General Public License.
# You can read the licence by clicking Help->Licence in the NVDA menu
# or by visiting http://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import addonHandler,appModuleHandler

# We keep it in the case it would finally be necessary to change add-on summary by language
# _addonDir = os.path.join(os.path.dirname(__file__), "..").decode("mbcs")
# _curAddon = addonHandler.Addon(_addonDir)
# _addonSummary = _curAddon.manifest['summary']

# We initialize translations
addonHandler.initTranslation()

# Class for Dropbox items in the metro app
class dropboxitem(UIA.ListItem):
	def _get_name(self):
		l = list()
		obj = self.firstChild
		if obj.name != u'': l.append(obj.name)
		while (obj != self.lastChild):
			if obj.role == controlTypes.ROLE_STATICTEXT:
				if obj.name != u'': l.append(obj.name)
			obj = obj.next
		return '; '.join(l)

class AppModule(appModuleHandler.AppModule):
	# We set the scripts category shown on input gestures dialog
	# scriptCategory = unicode(_addonSummary)
	scriptCategory = u"Dropbox"

	def chooseNVDAObjectOverlayClasses(self, obj, CLSList):
		if obj.role == controlTypes.ROLE_LISTITEM:
			CLSList.insert(0, dropboxitem)
