# -*- coding: utf-8 -*-
# Dropbox announcement Global Plugin for NVDA
# Copyright (C) 2014 Filaos, Patrick ZAJDA <patrick@zajda.fr> and other contributors
# This file is covered by the GNU General Public License.
# You can read the licence by clicking Help->Licence in the NVDA menu
# or by visiting http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# Shortcut: NVDA+Shift+D

import globalPluginHandler,addonHandler,scriptHandler
import ui
import NVDAObjects
import api
import winUser
import controlTypes

def findDropBoxObject():
	# We get the systray
	l=("shell_TrayWnd","TrayNotifyWnd","SysPager","ToolbarWindow32")
	h,FindWindowExA =0,winUser.user32.FindWindowExA
	for element in l:
		h=FindWindowExA(h,0,element,0)
		if not h:
			continue

		obj=NVDAObjects.IAccessible.getNVDAObjectFromEvent(h,-4,0)
		o = obj.firstChild
		while o:
			name=o.name
			if  name != None and name.lower().startswith("dropbox"):
				# dropbox object found , quit while loop
				break

			o=o.next

		if o:
			#dropbox object found, quit for loop
			break
	return o

# We keep it for the same reason as in the app module
# _addonDir = os.path.join(os.path.dirname(__file__), "..").decode("mbcs")
# _curAddon = addonHandler.Addon(_addonDir)
# _addonSummary = _curAddon.manifest['summary']

# We initialize translation support
addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# We initialize the scripts category shown on input gestures dialog
	# scriptCategory = unicode(_addonSummary)
	scriptCategory = u"Dropbox"

	def script_announceDropbox(self, gesture):
		o = findDropBoxObject()
		if not o :
			# Translators: the message presented when Dropbox tray icon was not found
			ui.message(_("drop box not found"))
			return

		name=o.name.split()
		repeatCount = scriptHandler.getLastScriptRepeatCount()
		if repeatCount ==0 :
			# announce dropbox state
			del (name[1])
			name=" ".join (name)
			ui.message (name)
			
		else:
				# activate dropbox icon
				# If we are already inside of the context menu, stop the script
				objFocused = api.getFocusObject()
				currentProcess = objFocused.appModule.appName.lower()
				if (currentProcess.lower() == u'dropbox' and objFocused.windowClassName.lower() == u'#32768') and objFocused.role in ({controlTypes.ROLE_POPUPMENU, controlTypes.ROLE_MENUITEM}):
					return
				else:
					try:
						o.doAction()
					except NotImplementedError:
						# Translators: the message reported when it is not possible to activate Dropbox context menu.
						ui.message(_("Unable to activate Dropbox context menu"))
	# Translators: message presented when user performes input help for the Shift+NVDA+D script
	script_announceDropbox.__doc__ = _("If pressed once, announces Dropbox status. If pressed twice, open the Dropbox context menu by clicking on its systray icon")

	__gestures={
		"kb:NVDA+alt+d": "announceDropbox",
	}

