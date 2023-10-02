# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct, whenever possible.

# Since some strings in `addon_info` are translatable,
# we need to include them in the .po files.
# Gettext recognizes only strings given as parameters to the `_` function.
# To avoid initializing translations in this module we simply roll our own "fake" `_` function
# which returns whatever is given to it as an argument.
def _(arg):
	return arg


# Add-on information variables
addon_info = {
	# add-on Name
	"addon_name" : "dropbox",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary" : "Dropbox",
	# Add-on description
	# Translators: Long description to be shown for this add-on on installation and add-on information
	"addon_description" : _("""Announces Dropbox status or open the Dropbox systray menu.
Shortcut: NVDA+Alt+D"""),
	# version
	"addon_version" : "2023.10.01",
	# Author(s)
	"addon_author" : "Rui Fontes <rui.fontes@tiflotecnia.com>, Patrick ZAJDA, Filaos and other contributors",
	# URL for the add-on documentation support
	"addon_url" : "https://github.com/ruifontes/dropbox",
	# URL for the add-on repository where the source code can be found
	"addon_sourceURL": "https://github.com/ruifontes/dropbox",
	# Documentation file name
	"addon_docFileName" : "readme.html",
	# Minimum NVDA version supported (e.g. "2018.3.0", minor version is optional)
	"addon_minimumNVDAVersion" : "2019.3",
	# Last NVDA version supported/tested (e.g. "2018.4.0", ideally more recent than minimum version)
	"addon_lastTestedNVDAVersion" : "2024.1",
	# Add-on update channel (default is stable or None)
	"addon_updateChannel" : None,
	# Add-on license such as GPL 2
	"addon_license": "GPL V2",
	# URL for the license document the ad-on is licensed under
	"addon_licenseURL": "https://www.gnu.org/licenses/old-licenses/gpl-2.0.html",
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "globalPlugins", "dropbox", "*.py")]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []

# Base language for the NVDA add-on
# If your add-on is written in a language other than english, modify this variable.
# For example, set baseLanguage to "es" if your add-on is primarily written in spanish.
baseLanguage = "en"

# Markdown extensions for add-on documentation
# Most add-ons do not require additional Markdown extensions.
# If you need to add support for markup such as tables, fill out the below list.
# Extensions string must be of the form "markdown.extensions.extensionName"
# e.g. "markdown.extensions.tables" to add tables.
markdownExtensions = []
