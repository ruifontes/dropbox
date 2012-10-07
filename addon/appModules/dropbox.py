# -*- coding: utf-8 -*-
# Dropbox appModule for NVDA
# Make preferences tabs accessible and allow pressing escape to quit the preferences dialog.
# Copyright (C) 2012 Filaos, Patrick ZAJDA <patrick@zajda.fr> and other contributors
# This file is covered by the GNU General Public License.
# You can read the licence by clicking Help->Licence in the NVDA menu
# or by visiting http://www.gnu.org/licenses/old-licenses/gpl-2.0.html

import addonHandler,appModuleHandler
import api
import NVDAObjects
import controlTypes
import winUser
import ui

# We initialize translations
addonHandler.initTranslation()

# List of Dropbox preferences tabs
# Tab texts are translatables
listPageTab=(_("General"),_("Account"),_("Bandwidth"),_("Proxies"),_("Advanced"))

def getPageTabActive (h):
	""" Get the handle of the active tab
	@param h the handle of the tab page """
	firstChild,next=5,2
	GetWindow=winUser.getWindow
	h=winUser.user32.GetParent(h)
	h=GetWindow(GetWindow(h,next),next)
	h=GetWindow(h,firstChild)
	i=1
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
	index=listPageTab.index (getPageTabActive(h))
	if sens =="next":
		index+=1
	else:
		index-=1

	index %= len(listPageTab )

	(x,y,l,h) = NVDAObjects.IAccessible.getNVDAObjectFromEvent(h,-4,0).location
	x=x+(1,3,5,7,9)[index]*l/10
	y=y+h/2
	winUser.setCursorPos (x,y)
	winUser.mouse_event(winUser.MOUSEEVENTF_LEFTDOWN,0,0,None,None)
	winUser.mouse_event (winUser.MOUSEEVENTF_LEFTUP,0,0,None,None)

	#announces the new tab
	ui.message (listPageTab[index])

class AppModule(appModuleHandler.AppModule):
	# The tab page handle
	tabPageHandle = 0
	# The Cancel button
	cancelButton = None

	def event_NVDAObject_init(self, obj):
		if obj.name == u'buttonPanel':
			obj.role=controlTypes.ROLE_TABCONTROL
			self.tabPageHandle = obj.windowHandle
			obj.name=getPageTabActive(self.tabPageHandle)
		elif obj.name == _('Cancel') and obj.windowClassName == u'Button':
			self.cancelButton = obj

	def script_clickButtonCancel (self,gesture):
		if api.getFocusObject().windowText == u'DropboxTrayIcon' or api.getFocusObject().windowClassName == u'#32768':
			gesture.send()
			return
		if self.cancelButton == None:
			ui.message(_("Cancel button not found"))
			gesture.send()
		else:
			(x,y,l,h) = self.cancelButton.IAccessibleObject.accLocation (0)
			winUser.setCursorPos (x,y)
			winUser.mouse_event(winUser.MOUSEEVENTF_LEFTDOWN,0,0,None,None)
			winUser.mouse_event (winUser.MOUSEEVENTF_LEFTUP,0,0,None,None)
	script_clickButtonCancel.__doc__=_("Click on the Cancel button of the Dropbox preferences dialog")

	def script_sayPageTabActive(self,gesture,):
		ui.message (getPageTabActive(self.tabPageHandle))
	script_sayPageTabActive.__doc__=_("Announce the active tab of the Dropbox preferences dialog")

	def script_priorPageTab(self,gesture):
		changePageTab(self.tabPageHandle,"prior")
	script_priorPageTab.__doc__=_("Activate the prior tab of the Dropbox preferences dialog")

	def script_nextPageTab (self,gesture):
		changePageTab(self.tabPageHandle,"next")
	script_nextPageTab.__doc__=_("Activate the next tab of the Dropbox preferences dialog")

	__gestures={
"kb:control+tab":"nextPageTab",
"kb:control+shift+tab":"priorPageTab",
"kb:control+alt+t":"sayPageTabActive",
"kb:escape":"clickButtonCancel"
}
