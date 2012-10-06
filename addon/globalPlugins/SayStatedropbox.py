# -*- coding: utf-8 -*-
# Dropbox announcement Global Plugin for NVDA
# Authors: Filaos, Patrick ZAJDA <patrick@zajda.fr> and other contributors
# Shortcut: NVDA+Shift+D

import globalPluginHandler,IAccessibleHandler,addonHandler
import scriptHandler
from ui import message
import NVDAObjects
from api import getFocusObject
import winUser
import controlTypes

# We initialize translation support
addonHandler.initTranslation()

def rightMouseButton(o):
	""" make a right click
	@param o the object to click on"""
	# We get the object idea because we cannot act to the object dirrectly
	IDChild =o.IAccessibleChildID
	# We have to get the parent, this is a particularity.
	o=o.parent
	# We get the shild object location which has IDChild as id
	(x,y,l,h)=o.IAccessibleObject.accLocation(IDChild)
	#We calculate the center of the shild object
	x,y=int (x+l/2),int (y+h/2)
	# We move the cursor
	winUser.setCursorPos (x,y)
	# We make the right click event
	winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTDOWN,0,0,None,None)
	# Then, the release button event
	winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTUP,0,0,None,None)

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def script_announceDropbox(self, gesture):
		# We get the systray
		l=("shell_TrayWnd","TrayNotifyWnd","SysPager","ToolbarWindow32")
		h,FindWindowExA =0,winUser.user32.FindWindowExA
		for element in l:
			h=FindWindowExA(h,0,element,0)

		o=NVDAObjects.IAccessible.getNVDAObjectFromEvent(h,-4,1)
		name=o.name
		while not name.lower().startswith("dropbox"):
			o=o.next
			if not o :
				message(_("drop box not found"))
				return
			else:
				name=o.name


		name =name.split ()
		# We get the number of call of this script
		isSameScript =scriptHandler.getLastScriptRepeatCount()
		if isSameScript ==0 :
			del (name[1])
			name=" ".join (name)
		elif isSameScript ==1:
			name = " ".join(name[0:2])
		else:
			# If we are already inside of the context menu, stop the script
			objFocused = getFocusObject()
			currentProcess = objFocused.appModule.appName.lower()
			if (currentProcess.lower() == u'dropbox' and objFocused.windowClassName.lower() == u'#32768') and (objFocused.role == controlTypes.ROLE_POPUPMENU or objFocused.role == controlTypes.ROLE_MENUITEM):
				return
			else:
				rightMouseButton (o)
			return
		message (name)
	# Documentation
	script_announceDropbox.__doc__ = _("If pressed once, announces Dropbox status. If pressed twice, reports the Dropbox version. If pressed three times, open the Dropbox context menu by clicking on its systray icon")

	__gestures={
		"kb:NVDA+shift+d": "announceDropbox",
	}

