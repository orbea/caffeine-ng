#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2009 The Caffeine Developers
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


import os
from os.path import join, abspath, dirname, pardir
import gtk

VERSION = "0.3"
BASE_PATH = None

c = abspath(dirname(__file__))
while True:
    ls = os.listdir(c)
    if "bin" in ls and "share" in ls:
        BASE_PATH = c
        break
    
    c = join(c, pardir)


IMAGE_PATH = join(BASE_PATH, 'share', 'caffeine', 'images')
GLADE_PATH = join(BASE_PATH, 'share', 'caffeine', 'glade')
ICON_PATH  = join(BASE_PATH, 'share', 'icons')

FULL_ICON_PATH = join(IMAGE_PATH, "Full_Cup.svg")
EMPTY_ICON_PATH = join(IMAGE_PATH, "Empty_Cup.svg")

ICON_NAME = 'caffeine'
icon_theme = gtk.icon_theme_get_default()

def get_icon_pixbuf(size):
    global icon_theme
    global ICON_NAME
    
    iconInfo = icon_theme.lookup_icon(ICON_NAME, size,
        gtk.ICON_LOOKUP_NO_SVG)
    
    if iconInfo:
        # icon is found
        base_size = iconInfo.get_base_size()
        if base_size != size:
            ## No sizexsize icon in the users theme so use the default
            icon_theme = gtk.IconTheme()
            icon_theme.set_search_path((ICON_PATH,))
    else:
        icon_theme.append_search_path(ICON_PATH)
        iconInfo = icon_theme.lookup_icon(ICON_NAME, size,
            gtk.ICON_LOOKUP_NO_SVG)

    pixbuf = icon_theme.load_icon(ICON_NAME, size,
                gtk.ICON_LOOKUP_NO_SVG)

    return pixbuf


from caffeine.main import main