#versionInfo.py
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2006-2018 NV Access Limited
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

"""
This module contains localizable version information such as description, copyright and About messages etc.
As there are localizable strings at module level, this can only be imported once localization is set up via languageHandler.initialize.
To access version information for programmatic version checks before languageHandler.initialize, use the buildVersion module which contains all the non-localizable version information such as major and minor version, and version string etc.
"""

import os
from buildVersion import *

longName = "NonVisual Desktop Access"
description = "A free and open source screen reader for Microsoft Windows"
url = "https://www.nvaccess.org/"
copyrightYears = "2006-2020"
copyright = "Copyright (C) {years} NVDA Contributors".format(
	years=copyrightYears)
aboutMessage = "about"
	

