# -*- coding: utf-8 -*-
# Dropbox announcement Global Plugin for NVDA
# Authors: Filaos, Patrick ZAJDA
# Shortcut: NVDA+Shift+D

import globalPluginHandler,IAccessibleHandler,addonHandler
import scriptHandler
from ui import message
import ctypes
import NVDAObjects
from api import getFocusObject
import winUser
import controlTypes

# We initialize translation support
addonHandler.initTranslation()

def rightMouseButton(o):
	#simulation du bouton droit de la souris
	#récupération de l'identifiant de l'objet ,car on ne pourra pas agir directement sur l'objet 
	IDChild =o.IAccessibleChildID
	#on remonte d'un niveau pour récupérer les coordonnées de l'objet ceci est une particularité
	o=o.parent
	#on récupère les coordonnées de l'objet enfant de o dont l'identifiant est IDChild
	(x,y,l,h)=o.IAccessibleObject.accLocation(IDChild)
	#on calcul le centre de l'objet enfant
	x,y=int (x+l/2),int (y+h/2)
	#on déplace le curseur
	winUser.setCursorPos (x,y)
	#on simule l'appuie sur le click droit de la souris 
	winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTDOWN,0,0,None,None)
	#on simule le relâchement du bouton droit de la souris
	winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTUP,0,0,None,None)

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def script_announceDropbox(self, gesture):
		l=("shell_TrayWnd","TrayNotifyWnd","SysPager","ToolbarWindow32")
		h,FindWindowExA =0,ctypes.windll.user32.FindWindowExA
		for element in l:
			h=FindWindowExA(h,0,element,0)

		o=NVDAObjects.IAccessible.getNVDAObjectFromEvent(h,-4,1)
		name=o.name
		while (name[0:7].lower()).find ("dropbox")==-1:
			o=o.next
			if not o :
				message(_("drop box not found"))
				return
			else:
				name=o.name


		name =name.split ()
		#stockage du nombre de fois que le script a été appelé
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
	script_announceDropbox.__doc__ = _("Announce Dropbox' status")

	__gestures={
		"kb:NVDA+shift+d": "announceDropbox",
	}

