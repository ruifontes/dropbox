# -*- coding: utf-8 -*-
# Dropbox announcement Global Plugin for NVDA
# Copyright (C) 2014 Filaos, Patrick ZAJDA <patrick@zajda.fr>, Rui Fontes and other contributors
# This file is covered by the GNU General Public License.
# You can read the licence by clicking Help->Licence in the NVDA menu
# or by visiting http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# Shortcut: NVDA+Alt+D
# Some portion have been directly copied from the systraylist addon
# copyright (C) Rui Fontes and other contributors

import ctypes
import globalPluginHandler
import addonHandler
import scriptHandler
import ui
import NVDAObjects
import api
import windowUtils
import winUser
import controlTypes
from typing import Callable


# We initialize translation support
addonHandler.initTranslation()
_: Callable[[str], str]
# Constents for roles to keep compatibility
if hasattr(controlTypes, 'ROLE_POPUPMENU'):
	POPUP_MENU = controlTypes.ROLE_POPUPMENU
else:
	POPUP_MENU = controlTypes.Role.POPUPMENU
if hasattr(controlTypes, 'ROLE_MENUITEM'):
	MENU_ITEM = controlTypes.ROLE_MENUITEM
else:
	POPUP_MENU = controlTypes.Role.MENUITEM


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# We initialize the scripts category shown on input gestures dialog
	scriptCategory = u"Dropbox"

	def _findAccessibleLeafsFromWindowClassPath(self, windowClassPath):
		# Create a list of systray icons
		# Copied from systray list add-on from Rui Fontes
		h, FindWindowEx = 0, winUser.user32.FindWindowExW
		for element in windowClassPath:
			h = FindWindowEx(h, 0, element, 0)
		trayObjects = []
		trayObject = NVDAObjects.IAccessible.getNVDAObjectFromEvent(h, -4, 1)
		# When trayObject.next is None it means that there is no more objects on the systray.
		while trayObject is not None:
			if trayObject.name:
				trayObjects.append(trayObject)
			trayObject = trayObject.next
		return trayObjects

	def _findAccessibleLeafsFromWindowClassPath11(self, windowClassPath):
		# Create a list of systray icons
		# Copied from Systray list NVDA add-on
		h = 0
		for className in windowClassPath:
			h = ctypes.windll.user32.FindWindowExA(h, 0, className, 0)
			# if not h:
			# 	break
		obj = NVDAObjects.IAccessible.getNVDAObjectFromEvent(h, -4, 0).firstChild.children
		trayObjects = []
		for trayObject in obj:
			trayObjects.append(trayObject)
		return trayObjects

	def _findAccessibleLeafsFromWindowClassPath11_22h2(self):
		"""
		Create a list of systray icons
		Copied from Systray list add-on
		"""
		# Starting to find the handle of the Shell_TrayWnd window
		h = winUser.FindWindow("Shell_TrayWnd", None)
		# Now, lets get the handle of Windows.UI.Input.InputSite.WindowClass window, where the icons reside...
		hwnd = windowUtils.findDescendantWindow(
			h, visible=None, controlID=None, className="Windows.UI.Input.InputSite.WindowClass"
		)
		# Now, lets get all objects in this window and its location
		obj = NVDAObjects.IAccessible.getNVDAObjectFromEvent(hwnd, -4, 0).children
		trayObjects = []
		# We start in the second object because the first object do not interesse us...
		o = 1
		while o in range(len(obj)):
			trayObjects.append(obj[o])
			o = o + 1
		return trayObjects

	def _findDropbox(self):
		path = ("shell_TrayWnd", "TrayNotifyWnd", "SysPager", "ToolbarWindow32")
		path11 = ("shell_TrayWnd", "TrayNotifyWnd", "Windows.UI.Composition.DesktopWindowContentBridge")
		try:
			from winVersion import getWinVer, WinVersion
			global win11_22h2
			win11_22h2 = getWinVer() >= WinVersion(major=10, minor=0, build=22621)
			win11 = getWinVer() >= WinVersion(major=10, minor=0, build=22000)
		except ImportError:
			win11 = False
		if win11_22h2:
			objects = self._findAccessibleLeafsFromWindowClassPath11_22h2()
		elif win11:
			objects = self._findAccessibleLeafsFromWindowClassPath11(path11)
		else:
			objects = self._findAccessibleLeafsFromWindowClassPath(path)
		for trayIcon in objects:
			iconName = trayIcon.name
			if iconName is not None and "dropbox" in iconName.lower():
				# dropbox object found
				return trayIcon
		return None

	def script_announceDropbox(self, gesture):
		trayIcon = self._findDropbox()
		if not trayIcon:
			# Translators: the message presented when Dropbox tray icon was not found
			ui.message(_("drop box not found"))
			return

		name = trayIcon.name.split()
		repeatCount = scriptHandler.getLastScriptRepeatCount()
		if repeatCount == 0:
			# announce dropbox state
			if win11_22h2:
				del(name[0:3])
			del(name[1])
			name = " ".join(name)
			ui.message(name)

		else:
			# activate dropbox icon
			# If we are already inside of the context menu, stop the script
			objFocused = api.getFocusObject()
			currentProcess = objFocused.appModule.appName.lower()
			if (
				(currentProcess.lower() == u'dropbox' and objFocused.windowClassName.lower() == u'#32768')
				and objFocused.role in ({POPUP_MENU, MENU_ITEM})
			):
				return
			else:
				try:
					trayIcon.doAction()
				except NotImplementedError:
					# Translators: the message reported when it is not possible to activate Dropbox context menu.
					ui.message(_("Unable to activate Dropbox context menu"))
	# Translators: message presented when user performes input help for the Shift+NVDA+D script
	script_announceDropbox.__doc__ = _(
		"If pressed once, announces Dropbox status. "
		"If pressed twice, open the Dropbox context menu by clicking on its systray icon"
	)

	__gestures = {
		"kb:NVDA+alt+d": "announceDropbox",
	}
