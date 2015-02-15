# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
# add-on Name
	"addon-name" : "dropbox",
	# Add-on description
	"addon-summary" : "Dropbox",
	# Add-on description
	# Translators: Long description to be shown for this add-on on installation and add-on information
	"addon-description" : _("""Announces Dropbox status or open the Dropbox systray menu.
Shortcut: NVDA+Shift+D"""),
	# version
	"addon-version" : "4.0-dev",
	# Author(s)
	"addon-author" : "Patrick ZAJDA <patrick@zajda.fr>, Filaos and other contributors",
	# URL for the add-on documentation support
	"addon-url" : "http://addons.nvda-project.org/"
	# Documentation file name
	"addon_docFileName" : "readme.html",
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "appModules", "*.py"),
    os.path.join("addon", "globalPlugins", "*.py")]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py""]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
