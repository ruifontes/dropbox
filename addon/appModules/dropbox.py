# -*- coding: utf-8 -*-
# Dropbox appModule for NVDA
# Make preferences tabs accessible.
# Authors: Filaos, Patrick ZAJDA <patrick@zajda.fr>

import addonHandler,appModuleHandler,NVDAObjects,controlTypes,winUser

from ui import message
from api import getFocusObject

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
	if index >=5:
		index =0
	elif index<=-1:
		index=4

	(x,y,l,h) = NVDAObjects.IAccessible.getNVDAObjectFromEvent(h,-4,0).IAccessibleObject.accLocation (0)
	x=x+(1,3,5,7,9)[index]*l/10
	y=y+h/2
	winUser.setCursorPos (x,y)
	winUser.mouse_event(winUser.MOUSEEVENTF_LEFTDOWN,0,0,None,None)
	winUser.mouse_event (winUser.MOUSEEVENTF_LEFTUP,0,0,None,None)

	#announces the new tab
	message (listPageTab[index])

class AppModule(appModuleHandler.AppModule):
	# The tab page handle
	tabPageHandle = 0

	def script_clickButtonCancel (self,gesture):
		h=getFocusObject().windowHandle
		GetParent =winUser.user32.GetParent
		while GetParent(h) and winUser.isWindowEnabled(GetParent (h)):
			h=GetParent(h)

		FindWindowExA=winUser.user32.FindWindowExA
		while FindWindowExA (h,None,"Button",_("Cancel"))==False :
			h=winUser.getWindow (h,5)
			if not h :
				gesture.send()
				return
		h=FindWindowExA(h,None,"Button",_("Cancel"))
		NVDAObjects.IAccessible.getNVDAObjectFromEvent (h,-4,0).IAccessibleObject.accDoDefaultAction (0)

	def event_NVDAObject_init(self, obj):
		if obj.name == u'buttonPanel':
			obj.role=controlTypes.ROLE_TABCONTROL
			self.tabPageHandle = obj.windowHandle
			obj.name=getPageTabActive(self.tabPageHandle)

	def script_sayPageTabActive(self,gesture,):
		message (getPageTabActive(self.tabPageHandle))

	def script_priorPageTab(self,gesture):
		changePageTab(self.tabPageHandle,"prior")

	def script_nextPageTab (self,gesture):
		changePageTab(self.tabPageHandle,"next")

	__gestures={
"kb:control+tab":"nextPageTab",
"kb:control+shift+tab":"priorPageTab",
"kb:control+alt+t":"sayPageTabActive",
"kb:escape":"clickButtonCancel"
}
