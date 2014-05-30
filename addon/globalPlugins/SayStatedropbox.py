# -*- coding: utf-8 -*-
# Dropbox announcement Global Plugin for NVDA
# Copyright (C) 2014 Filaos, Patrick ZAJDA <patrick@zajda.fr> and other contributors
# This file is covered by the GNU General Public License.
# You can read the licence by clicking Help->Licence in the NVDA menu
# or by visiting http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# Shortcut: NVDA+Shift+D

import globalPluginHandler,IAccessibleHandler,addonHandler,scriptHandler
import ui
import NVDAObjects
import api
import winUser
import controlTypes
import wx
import time
from keyboardHandler import KeyboardInputGesture
import eventHandler
import speech

# We keep it for the same reason as in the app module
# _addonDir = os.path.join(os.path.dirname(__file__), "..").decode("mbcs")
# _curAddon = addonHandler.Addon(_addonDir)
# _addonSummary = _curAddon.manifest['summary']

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
	# We initialize the scripts category shown on input gestures dialog
	# scriptCategory = unicode(_addonSummary)
	scriptCategory = u"Dropbox"

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin,  self).__init__(*args, **kwargs)
		self.taskTimer = None

	def script_announceDropbox(self, gesture):
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

		def callback2 (o, repeat, oldSpeechMode):

			self.taskTimer = None
			oFocus = api.getFocusObject()
			role = oFocus.role
			name = oFocus.name
			if role == controlTypes.ROLE_BUTTON  and "dropbox" in name.lower():
				speech.speechMode = oldSpeechMode
				KeyboardInputGesture.fromName("Enter").send()
				KeyboardInputGesture.fromName("DownArrow").send()

			else:
				if repeat:
					KeyboardInputGesture.fromName("escape").send()
					time.sleep(0.2)
					rightMouseButton (o)
					self.taskTimer = wx.CallLater(300, callback2,o, repeat-1, oldSpeechMode)
					
				else:
					speech.speechMode = oldSpeechMode
					# Translators: message announced if it is impossible to find the Dropbox systray icon
					ui.message(_("Impossible to open DropBox context menu"))
				
				
		def callback(repeatCount):
			self.taskTimer = None
			o = findDropBoxObject()
			if not o :
				ui.message(_("drop box not found"))
				return

			name=o.name.split()
			if repeatCount ==0 :
				# announce dropbox state
				del (name[1])
				name=" ".join (name)
				ui.message (name)
				
			elif repeatCount == 1:
				# activate dropbox icon
				# If we are already inside of the context menu, stop the script
				objFocused = api.getFocusObject()
				currentProcess = objFocused.appModule.appName.lower()
				if (currentProcess.lower() == u'dropbox' and objFocused.windowClassName.lower() == u'#32768') and objFocused.role in ({controlTypes.ROLE_POPUPMENU, controlTypes.ROLE_MENUITEM}):
					eventHandler.queueEvent("gainFocus",objFocused)

				else:
					oldSpeechMode = speech.speechMode
					speech.speechMode = speech.speechMode_off
					rightMouseButton (o)
					self.taskTimer = wx.CallLater(200, callback2, o, 2, oldSpeechMode)

			else:
				# say Dropbox version
				ui.message(" ".join(name[0:2]))

			
		if self.taskTimer!= None:
			self.taskTimer.Stop()
			self.taskTimer = None
		# We get the number of call of this script
		repeatCount =scriptHandler.getLastScriptRepeatCount()
		self.taskTimer = wx.CallLater(400, callback, repeatCount)

	# Translators: message presented when user performes input help for the Shift+NVDA+D script
	script_announceDropbox.__doc__ = _("If pressed once, announces Dropbox status. If pressed twice, open the Dropbox context menu by clicking on its systray icon. If pressed three times, reports the Dropbox version")

	__gestures={
		"kb:NVDA+shift+d": "announceDropbox",
	}

