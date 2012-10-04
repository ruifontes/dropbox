# -*- coding: utf-8 -*-
# Dropbox appModule for NVDA
# Make preferences tabs accessible.
# Authors: mainly Filaos, Patrick ZAJDA <patrick@zajda.fr> to make it translatable

import appModuleHandler,NVDAObjects,controlTypes,addonHandler,winUser

from ui import message
#from winUser  import  mouse_event,MOUSEEVENTF_LEFTUP,MOUSEEVENTF_LEFTDOWN,isWindowVisible,setCursorPos,setFocus,getWindowText,isWindowEnabled
from api import getFocusObject

# We initialize translations
addonHandler.initTranslation()

# List of Dropbox preferences tabs
# Tab texts are translatables
listPageTab=(_("General"),_("Account"),_("Bandwidth"),_("Proxies"),_("Advanced"))

def getHandlePageTab():
	""" Get the tab pannel handle """
	FindWindowExA=winUser.user32.FindWindowExA
	h=int ()
	for i in range (4):
		h=FindWindowExA(h,None,"wxWindowClassNR",None)
	return h

def getPageTabActive ():
	""" Get the handle of the active tab """
	firstChild,next=5,2
	GetWindow=winUser.getWindow
	h=getHandlePageTab()
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

def changePageTab (sens):
	""" Change the active tab
	@param sens : string, next or prior """
	#index =getPageTabActive ()[-1]
	index=listPageTab.index (getPageTabActive())
	if sens =="next":
		index+=1
	else:
		index-=1
	if index >=5:
		index =0
	elif index<=-1:
		index=4

	(x,y,l,h) = NVDAObjects.IAccessible.getNVDAObjectFromEvent(getHandlePageTab(),-4,0).IAccessibleObject.accLocation (0)
	x=x+(1,3,5,7,9)[index]*l/10
	y=y+h/2
	winUser.setCursorPos (x,y)
	winUser.mouse_event(winUser.MOUSEEVENTF_LEFTDOWN,0,0,None,None)
	winUser.mouse_event (winUser.MOUSEEVENTF_LEFTUP,0,0,None,None)

	#announces the new tab
	message (listPageTab[index])



class AppModule(appModuleHandler.AppModule):
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
		if obj.windowHandle ==getHandlePageTab() or obj.name == u'buttonPanel':
			obj.name=getPageTabActive()
			obj.role=controlTypes.ROLE_TABCONTROL

	def script_sayPageTabActive(self,gesture,):
		message (getPageTabActive())

	def script_priorPageTab(self,gesture):
		changePageTab("prior")

	def script_nextPageTab (self,gesture):
		changePageTab("next")

	__gestures={
"kb:control+tab":"nextPageTab",
"kb:control+shift+tab":"priorPageTab",
"kb:control+alt+t":"sayPageTabActive",
"kb:escape":"clickButtonCancel"
}
