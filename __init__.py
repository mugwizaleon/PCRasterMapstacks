# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PcrasterMapstackVisualisation
                                 A QGIS plugin
 PCRaster Mapstack visualisation
                             -------------------
        begin                : 2014-06-28
        copyright            : (C) 2014 by Leon
        email                : mugwizal@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load PcrasterMapstackVisualisation class from file PcrasterMapstackVisualisation
    from pcrastermapstackvisualisation import PcrasterMapstackVisualisation
    return PcrasterMapstackVisualisation(iface)
