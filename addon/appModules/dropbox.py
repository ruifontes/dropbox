# -*- coding: utf-8 -*-
# Dropbox appModule for NVDA
# Make preferences tabs accessible and allow pressing escape to quit the preferences dialog.
# Also improves accessibility of the Dropbox Metro app for Windows 8
# Copyright (C) 2014 Filaos, Patrick ZAJDA <patrick@zajda.fr> and other contributors
# Windows 8 compatibility contributed by David Parduhn <xkill85@gmx.net>
# This file is covered by the GNU General Public License.
# You can read the licence by clicking Help->Licence in the NVDA menu
# or by visiting http://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import addonHandler,appModuleHandler
import api
import NVDAObjects
import controlTypes
import winUser
import ui
# import os
from NVDAObjects import UIA

# We keep it in the case it would finally be necessary to change add-on summary by language
# _addonDir = os.path.join(os.path.dirname(__file__), "..").decode("mbcs")
# _curAddon = addonHandler.Addon(_addonDir)
# _addonSummary = _curAddon.manifest['summary']

# We initialize translations
addonHandler.initTranslation()

# List of Dropbox preferences tabs
# Tab texts are translatable
listPageTab=(
	# Translators: the name of the dropbox general tab.
	_("General"),
	# Translators: the name of the dropbox account tab.
	_("Account"),
	# Translators: the name of the dropbox bandwidth tab.
	_("Bandwidth"),
	# Translators: the name of the dropbox proxies tab.
	_("Proxies"),
	# Translators: the name of the dropbox advanced tab.
	_("Advanced")
)

def getPageTabActive (h):
	""" Get the handle of the active tab
	@param h the handle of the tab page """
	firstChild,next=5,2
	GetWindow=winUser.getWindow
	h=winUser.user32.GetParent(h)
	h=GetWindow(GetWindow(h,next),next)
	h=GetWindow(h,firstChild)
	i=0
	while winUser.isWindowVisible (h)==False:
		h=GetWindow(h,next)
		i+=1
		if not h :
			return
	return listPageTab[i-1]

def changePageTab (h,sens):
	""" Change the active tab
	@param h the handle of tab page
	@param sens : string, next or prior """
	#index =getPageTabActive ()[-1]
	index=listPageTab.index(getPageTabActive(h))
	if sens =="next":
		index+=1
	else:
		index-=1

	index %= len(listPageTab)

	(x, y, l, h) = NVDAObjects.IAccessible.getNVDAObjectFromEvent(h,-4,0).location
	x=x+(1,3,5,7,9)[index]*l/10
	y=y+h/2
	winUser.setCursorPos (x,y)
	winUser.mouse_event(winUser.MOUSEEVENTF_LEFTDOWN,0,0,None,None)
	winUser.mouse_event (winUser.MOUSEEVENTF_LEFTUP,0,0,None,None)

	#announces the new tab
	ui.message(listPageTab[index])

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

	def event_NVDAObject_init(self, obj):
		if obj.name == u'buttonPanel':
			obj.role=controlTypes.ROLE_TABCONTROL
			obj.name=getPageTabActive(obj.windowHandle)

	def chooseNVDAObjectOverlayClasses(self, obj, CLSList):
		if obj.role == controlTypes.ROLE_LISTITEM:
			CLSList.insert(0, dropboxitem)

	def script_clickButtonCancel (self,gesture):
		# Translators: the title of the dropbox preferences dialog, it is important to have the same capitalization/spelling as in the dropbox gui. If Dropbox hasn't been translated to your language yet, leave this blank or write the original text.
		if api.getFocusObject().windowText == u'DropboxTrayIcon' or api.getFocusObject().windowClassName == u'#32768' or api.getForegroundObject().name != _("Dropbox Preferences"):
			gesture.send()
			return
		cancelButton=api.getForegroundObject().simpleLastChild
		# Translators: the name of the dropbox preferences cancel button, it is important to have the same capitalization/spelling as in the dropbox gui. If Dropbox hasn't been translated to your language yet, leave this blank or write the original text.
		if cancelButton.name != _('Cancel'):
			cancelButton=cancelButton.simplePrevious if cancelButton.simplePrevious.name == _('Cancel') else None
		if cancelButton == None:
			ui.message(_("Cancel button not found"))
			gesture.send()
		else:
			(x,y,l,h) = cancelButton.IAccessibleObject.accLocation (0)
			winUser.setCursorPos (x,y)
			winUser.mouse_event(winUser.MOUSEEVENTF_LEFTDOWN,0,0,None,None)
			winUser.mouse_event (winUser.MOUSEEVENTF_LEFTUP,0,0,None,None)
	# Translators: message presented when user performs input help for this shortcut.
	script_clickButtonCancel.__doc__=_("Clicks the Cancel button of the Dropbox preferences dialog")

	def script_sayPageTabActive(self,gesture):
		if api.getFocusObject().windowText == u'DropboxTrayIcon' or api.getFocusObject().windowClassName == u'#32768' or api.getForegroundObject().name != _("Dropbox Preferences"):
			gesture.send()
			return
		tabPageHandle = api.getForegroundObject().simpleFirstChild.windowHandle
		ui.message(getPageTabActive(tabPageHandle))
	# Translators: message presented when user performs input help for this shortcut.
	script_sayPageTabActive.__doc__=_("announce active Dropbox preferences dialog tab")

	def script_priorPageTab(self,gesture):
		if api.getFocusObject().windowText == u'DropboxTrayIcon' or api.getFocusObject().windowClassName == u'#32768' or api.getForegroundObject().name != _("Dropbox Preferences"):
			gesture.send()
			return
		tabPage = api.getForegroundObject().simpleFirstChild
		tabPageHandle = tabPage.windowHandle
		changePageTab(tabPageHandle,"prior")
		objToFocus = tabPage.simpleNext
		while objToFocus.isFocusable == False or objToFocus.role == controlTypes.ROLE_GROUPING:
			objToFocus = objToFocus.simpleNext
		objToFocus.setFocus()
	# Translators: message presented when user performs input help for this shortcut.
	script_priorPageTab.__doc__=_("Activate previous Dropbox preferences dialog tab")

	def script_nextPageTab (self,gesture):
		if api.getFocusObject().windowText == u'DropboxTrayIcon' or api.getFocusObject().windowClassName == u'#32768' or api.getForegroundObject().name != _("Dropbox Preferences"):
			gesture.send()
			return
		tabPage = api.getForegroundObject().simpleFirstChild
		tabPageHandle = tabPage.windowHandle
		changePageTab(tabPageHandle,"next")
		objToFocus = tabPage.simpleNext
		while objToFocus.isFocusable == False or objToFocus.role == controlTypes.ROLE_GROUPING:
			objToFocus = objToFocus.simpleNext
		objToFocus.setFocus()
	# Translators: message presented when user performs input help for this shortcut.
	script_nextPageTab.__doc__=_("Activate next Dropbox preferences dialog tab")

	__gestures={
"kb:control+tab":"nextPageTab",
"kb:control+pageDown":"nextPageTab",
"kb:control+shift+tab":"priorPageTab",
"kb:control+pageUp":"priorPageTab",
"kb:control+alt+t":"sayPageTabActive",
"kb:escape":"clickButtonCancel"
}
