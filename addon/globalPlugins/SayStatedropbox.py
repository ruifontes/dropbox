# -*- coding: utf-8 -*-
# Dropbox announcement Global Plugin for NVDA
# Copyright (C) 2014 Filaos, Patrick ZAJDA <patrick@zajda.fr> and other contributors
# This file is covered by the GNU General Public License.
# You can read the licence by clicking Help->Licence in the NVDA menu
# or by visiting http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# Shortcut: NVDA+Alt+D

import globalPluginHandler
import addonHandler
import scriptHandler
import ui
import NVDAObjects
import api
import winUser
import controlTypes


def findDropBoxObject():
	# We get the systray
	windowClassList = (u"shell_TrayWnd", u"TrayNotifyWnd", u"SysPager", u"ToolbarWindow32")
	handle, FindWindowExW = 0, winUser.user32.FindWindowExW
	for element in windowClassList:
		handle = FindWindowExW(handle, 0, element, 0)
		if not handle:
			continue

		sysTray = NVDAObjects.IAccessible.getNVDAObjectFromEvent(handle, -4, 0)
		trayIcon = sysTray.firstChild
		while trayIcon:
			iconName = trayIcon.name
			if iconName is not None and iconName.lower().startswith("dropbox"):
				# dropbox object found , quit while loop
				break

			trayIcon = trayIcon.next

		if trayIcon:
			# dropbox object found, quit for loop
			break
	return trayIcon


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
		trayIcon = findDropBoxObject()
		if not trayIcon:
			# Translators: the message presented when Dropbox tray icon was not found
			ui.message(_("drop box not found"))
			return

		name = trayIcon.name.split()
		repeatCount = scriptHandler.getLastScriptRepeatCount()
		if repeatCount == 0:
			# announce dropbox state
			del (name[1])
			name = " ".join(name)
			ui.message(name)

		else:
			# activate dropbox icon
			# If we are already inside of the context menu, stop the script
			objFocused = api.getFocusObject()
			currentProcess = objFocused.appModule.appName.lower()
			if (
				(currentProcess.lower() == u'dropbox' and objFocused.windowClassName.lower() == u'#32768')
				and objFocused.role in ({controlTypes.ROLE_POPUPMENU, controlTypes.ROLE_MENUITEM})
			):
				return
			else:
				try:
					trayIcon.doAction()
				except NotImplementedError:
					# Translators: the message reported when it is not possible to activate Dropbox context menu.
					ui.message(_("Unable to activate Dropbox context menu"))
	# Translators: message presented when user performes input help for the Shift+NVDA+D script
	script_announceDropbox.__doc__ =\
	_(
		"If pressed once, announces Dropbox status. "
		"If pressed twice, open the Dropbox context menu by clicking on its systray icon"
	)

	__gestures = {
		"kb:NVDA+alt+d": "announceDropbox",
	}
