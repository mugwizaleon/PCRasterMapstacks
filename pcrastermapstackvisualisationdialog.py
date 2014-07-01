# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PcrasterMapstackVisualisationDialog
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
"""

from PyQt4 import QtCore, QtGui
from ui_pcrastermapstackvisualisation import Ui_PcrasterMapstackVisualisation
# create the dialog for zoom to point


class PcrasterMapstackVisualisationDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        # Set up the user interface from Designer.
        self.ui = Ui_PcrasterMapstackVisualisation()
        self.ui.setupUi(self)



