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
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import qgis.utils
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from pcrastermapstackvisualisationdialog import PcrasterMapstackVisualisationDialog
from Animationdialog import AnimationDialog
from TSSvisualizationdialog import TSSVisualizationDialog
# Import modules
import os.path
import os,  glob
import time
import sys
import string

class PcrasterMapstackVisualisation:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'pcrastermapstackvisualisation_{}.qm'.format(locale))
        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = PcrasterMapstackVisualisationDialog()
        self.dlg2 = AnimationDialog()
        self.dlg3 = TSSVisualizationDialog()

        # Mapstack series visualization
        QObject.connect( self.dlg.ui.pushButton_7, SIGNAL( "clicked()" ), self.DisplayTSSnames)
        QObject.connect( self.dlg.ui.pushButton_6, SIGNAL( "clicked()" ), self.TSSgraphs)
        
        QObject.connect( self.dlg.ui.btnBaseDir_3, SIGNAL( "clicked()" ), self.selectDir ) #link the button to the function of selecting the directory
        QObject.connect( self.dlg.ui.btnBaseDir_3, SIGNAL( "clicked()" ), self.loadMapStackCoreName ) #link the button to the function of selecting the directory
        QObject.connect( self.dlg.ui.pushButton_5, SIGNAL( "clicked()" ), self.actionStart)
        QObject.connect( self.dlg2.ui.pushButton_2, SIGNAL( "clicked()" ), self.ActionAnim)
        QObject.connect( self.dlg2.ui.pushButton_3, SIGNAL( "clicked()" ), self.actionNext)
        QObject.connect( self.dlg2.ui.pushButton, SIGNAL( "clicked()" ), self.actionPrevious)
        
        QObject.connect( self.dlg2.ui.pushButton_4, SIGNAL( "clicked()" ), self.actionStart)
        QObject.connect( self.dlg2.ui.pushButton_5, SIGNAL( "clicked()" ), self.actionLast)
        QObject.connect(self.dlg.ui.comboBox, SIGNAL("currentIndexChanged (const QString&)"), self.changelist) #Change the list of mapstacks
        
        #Close dialogs widgets
        QObject.connect( self.dlg.ui.pushButton, SIGNAL( "clicked()" ), self.close1)
        QObject.connect( self.dlg3.ui.pushButton, SIGNAL( "clicked()" ), self.close2)
        QObject.connect( self.dlg2.ui.pushButton_6, SIGNAL( "clicked()" ), self.close3)
        
    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/pcrastermapstackvisualisation/Myicon.png"),
            u"Mapstacks_visualisation", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&PCRaster Mapstacks Viewer", self.action)
        self.iface.addPluginToRasterMenu(u"&PCRaster Mapstacks Viewer", self.action)
        
    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&PCRaster Time series Viewer", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        
    def close1(self):
        self.dlg.close()

    def TSSview(self):
        self.dlg3.move(10, 300)
        self.dlg3.show()# show the dialog   
        
    def close2(self):
        self.dlg3.close()
        self.dlg.show()
    
    def AnimationDlg (self):
        self.dlg2.move(200, 200)
        self.dlg2.show()# show the dialog
    
    def close3(self):
        self.dlg2.close()
        self.dlg.show()
        
    # Selecting the directory containg files 
    def selectDir( self ):
        self.dlg.hide()
        settings = QSettings()
        path = QFileDialog.getExistingDirectory( self.iface.mainWindow(), "Select a directory")
        if path: self.dlg.ui.txtBaseDir2_5.setText( path )
        self.dlg.show()
        
    def actionRemove(self):
        layers = self.iface.legendInterface().layers()
        layer = qgis.utils.iface.activeLayer()
        self.PrincipalLayer = layer.name()
        for layer in layers :
            if layer.name() == self.PrincipalLayer : pass
            else : self.iface.legendInterface().moveLayer( layer, 0 )
        self.iface.legendInterface().removeGroup(0)
                
    def AddLayer(self, input):        
        layerPath = os.path.join(self.dataDir, input)
        fileInfo = QFileInfo(layerPath)
        baseName = fileInfo.baseName()
        layer = QgsRasterLayer(layerPath, baseName)
        uri = os.path.join(self.dataDir, 'MyFile.qml')
        layer.loadNamedStyle(uri)
        QgsMapLayerRegistry.instance().addMapLayer(layer)
        
    def loadFiles(self, filename):
        self.dataDir = str(self.dlg.ui.txtBaseDir2_5.text())
        os.chdir(self.dataDir )
        file_list =  glob.glob(filename)
        for index in file_list:
            list = index.split(".")
            if (len(list) < 2) :
                file_list.remove(index)
        for index in file_list:
            if index.endswith(".tss"):
                file_list.remove(index)
        for index in file_list:
            if index.endswith(".xml") or index.endswith(".aux.xml") :
                file_list.remove(index)
        for index in file_list:
            if index.endswith(".tss"):
                file_list.remove(index)
        file_list.sort()
        return file_list
        
    def loadMapStackCoreName(self):
        self.dataDir = str(self.dlg.ui.txtBaseDir2_5.text())
        files= os.listdir(self.dataDir)
        self.dlg.ui.comboBox.clear()
        self.dlg.ui.comboBox_2.clear()
        MyList=[]
        MyList2 =[]
        MyList3 = []
        for index in files:
            list = index.split(".")
            if (len(list)==2) and (len(list[0])== 8) and (len(list[1])== 3) and (list[1].isdigit()):
                MyList.append(index)
            if index.endswith(".tss"):
                MyList3.append(index)
        for index in MyList:
            list = index.split(".")
            words = list[0].replace("0", "")
            MyList2.append(words)
        FinalList = []
        for i in MyList2:
            if i not in FinalList:
                FinalList.append(i)
        self.dlg.ui.comboBox.addItems(FinalList)
        self.dlg.ui.comboBox_2.addItems(MyList3)

    def DisplayTSSnames(self):
        self.dataDir = str(self.dlg.ui.txtBaseDir2_5.text())
        if not self.dataDir : pass
        else:
            os.chdir(self.dataDir )
            if not self.dlg.ui.comboBox.currentText(): pass
            else:
                filename = '*'+str(self.dlg.ui.comboBox.currentText())+'*'
                file_list = self.loadFiles(filename) 
                self.dlg.ui.listWidget.clear()
                for index, file in enumerate(file_list):
                    self.dlg.ui.listWidget.addItem(file)
            
    def changelist(self):
        self.dlg.ui.listWidget.clear()
            
    def ActionAnim(self):
        self.actionRemove()
        Group = self.iface.legendInterface().addGroup("group_foo")       
        import numpy
        numpy.seterr(divide='ignore', invalid='ignore', over='ignore')
        self.dataDir = str(self.dlg.ui.txtBaseDir2_5.text())
        os.chdir(self.dataDir )
        filename = '*'+str(self.dlg.ui.comboBox.currentText())+'*'
        file_list = self.loadFiles(filename)    
        legend = self.iface.legendInterface() 
        self.dlg2.ui.pushButton_6.setEnabled(False)
        for index, file in enumerate(file_list):
            canvas = qgis.utils.iface.mapCanvas()
            import Styling
            Styling.style1(file_list[index], 'value', self.dataDir, file_list )
            uri = os.path.join(self.dataDir, 'MyFile.qml')
            self.iface.addRasterLayer(file, os.path.basename(str(file))).loadNamedStyle(uri)
            canvas.refresh()
            canvas.zoomToFullExtent()   
            rlayer = qgis.utils.iface.activeLayer()
            legend.moveLayer( rlayer, 0 )
            time.sleep(float(self.dlg2.ui.txtBaseDir2_5.text()))
        self.dlg2.ui.pushButton_6.setEnabled(True)

    def actionStart(self):
        import Styling
        self.dlg.hide()     
        self.iface.messageBar().clearWidgets ()
        layers = self.iface.legendInterface().layers()
        for layer in layers : 
            if self.iface.legendInterface().isLayerVisible(layer) : self.iface.legendInterface().setLayerVisible(layer, False)
        import numpy
        numpy.seterr(divide='ignore', invalid='ignore', over='ignore')
        self.dataDir = str(self.dlg.ui.txtBaseDir2_5.text())
        if not self.dataDir : 
            QMessageBox.information( self.iface.mainWindow(),"Info", "Please select a directory first")  
            self.dlg.show()
        else : 
            os.chdir(self.dataDir )
            filename = '*'+str(self.dlg.ui.comboBox.currentText())+'*'
            file_list = self.loadFiles(filename)
            if not self.dlg.ui.comboBox.currentText():
                QMessageBox.information( self.iface.mainWindow(),"Info", "The are no PCRaster mapstacks in this directory")
                self.dlg.show()
#                return
            else:
                self.AnimationDlg()
                Styling.style1(filename, 'value', self.dataDir, file_list )
                s = QSettings()
                oldValidation = s.value( "/Projections/defaultBehaviour", "useGlobal" )
                s.setValue( "/Projections/defaultBehaviour", "useGlobal" )
                self.AddLayer(str(file_list[0]))
                s.setValue( "/Projections/defaultBehaviour", oldValidation )
                layer = qgis.utils.iface.activeLayer()
#                self.PrincipalLayer = layer.name()
#                print self.PrincipalLayer
                self.iface.legendInterface().setLayerExpanded(layer, True)
        
    def actionLast(self):
        self.actionRemove()
        self.dlg.hide()
        self.AnimationDlg()
        self.iface.messageBar().clearWidgets ()
        layers = self.iface.legendInterface().layers()
        for layer in layers : 
            if self.iface.legendInterface().isLayerVisible(layer) : self.iface.legendInterface().setLayerVisible(layer, False)
        import numpy
        numpy.seterr(divide='ignore', invalid='ignore', over='ignore')
        self.dataDir = str(self.dlg.ui.txtBaseDir2_5.text())
        os.chdir(self.dataDir )
        filename = '*'+str(self.dlg.ui.comboBox.currentText())+'*'
        file_list = self.loadFiles(filename)
        index = len(file_list) - 1
        canvas = qgis.utils.iface.mapCanvas()  
        import Styling
        Styling.style1(file_list[index], 'value', self.dataDir, file_list )
        uri = os.path.join(self.dataDir, 'MyFile.qml')
        self.iface.addRasterLayer(file_list[index], os.path.basename(str(file_list[index]))).loadNamedStyle(uri)
        canvas.refresh()
        canvas.zoomToFullExtent()

    def actionNext(self):
        self.actionRemove()
        self.iface.messageBar().clearWidgets ()
        import numpy
        numpy.seterr(divide='ignore', invalid='ignore', over='ignore')
        self.dataDir = str(self.dlg.ui.txtBaseDir2_5.text())
        os.chdir(self.dataDir )
        filename = '*'+str(self.dlg.ui.comboBox.currentText())+'*'
        file_list = self.loadFiles(filename)
        layer = qgis.utils.iface.activeLayer()
        self.PrincipalLayer = layer.name()
        if layer is None :
            index = 0
        elif layer.name() not in file_list:
            index = 0
        else :
            counter = file_list.index(layer.name())
            index = counter + 1
            if counter == len(file_list) - 1 :
                layers = self.iface.legendInterface().layers()
                self.iface.legendInterface().addGroup("group_foo")
                for layer in layers : 
                    if layer.name() == self.PrincipalLayer : pass
                    elif self.iface.legendInterface().isLayerVisible(layer) : self.iface.legendInterface().moveLayer( layer, 0 )
                index = 0  
        canvas = qgis.utils.iface.mapCanvas()  
        import Styling
        Styling.style1(file_list[index], 'value', self.dataDir, file_list )
        uri = os.path.join(self.dataDir, 'MyFile.qml')
        self.iface.addRasterLayer(file_list[index], os.path.basename(str(file_list[index]))).loadNamedStyle(uri)
        canvas.refresh()
        canvas.zoomToFullExtent()      
        
    def actionPrevious(self):
        self.actionRemove()
        self.iface.messageBar().clearWidgets ()
        import numpy
        numpy.seterr(divide='ignore', invalid='ignore', over='ignore')
        self.dataDir = str(self.dlg.ui.txtBaseDir2_5.text())
        os.chdir(self.dataDir )
        filename = '*'+str(self.dlg.ui.comboBox.currentText())+'*'
        file_list = self.loadFiles(filename)
        layer = qgis.utils.iface.activeLayer()
        self.PrincipalLayer = layer.name()
        if layer is None :
            index = len(file_list) - 1
        elif layer.name() not in file_list:
            index = len(file_list) - 1
        else :
            counter = file_list.index(layer.name())
            index = counter - 1
            if counter == 0 :
                layers = self.iface.legendInterface().layers()
                self.iface.legendInterface().addGroup("group_foo")
                for layer in layers : 
                    if layer.name() == self.PrincipalLayer : pass
                    elif self.iface.legendInterface().isLayerVisible(layer) : self.iface.legendInterface().moveLayer( layer, 0 )
                index = len(file_list) - 1
        canvas = qgis.utils.iface.mapCanvas()  
        import Styling
        Styling.style1(file_list[index], 'value', self.dataDir, file_list )
        uri = os.path.join(self.dataDir, 'MyFile.qml')
        self.iface.addRasterLayer(file_list[index], os.path.basename(str(file_list[index]))).loadNamedStyle(uri)
        canvas.refresh()
        canvas.zoomToFullExtent() 

    def TSSgraphs(self):# wtih matplotlib
        self.dlg.hide()
        filename = str(self.dlg.ui.comboBox_2.currentText())  
        self.dataDir = str(self.dlg.ui.txtBaseDir2_5.text())
        file = os.path.join (self.dataDir, filename)
        if os.path.isfile(file):
            self.TSSview()
            self.dataDir = str(self.dlg.ui.txtBaseDir2_5.text())
            os.chdir(self.dataDir )
            stripped = []
            stripper =  open(filename, 'r')
            st_lines = stripper.readlines()[4:]
            stripper.close()
            for lines in st_lines:
                stripped_line = " ".join(lines.split())
                stripped.append(stripped_line)
            data = "\n".join(stripped)
            data = data.split('\n')
            values = []
            dates = []
            years = 0
            yl = []
            for row in data:
                x, y = row.split()
                values.append(float(y))
                year = (int(x.translate(string.maketrans("\n\t\r", "   ")).strip()))
                dates.append(year)
                years = years +1
                yl.append(years)
            xlabels = yl
            self.dlg3.ui.widget.canvas.ax.clear()
            self.dlg3.ui.widget.canvas.ax.set_position([0.155,0.15,0.82,0.75])
            self.dlg3.ui.widget.canvas.ax.set_title(filename) 
            self.dlg3.ui.widget.canvas.ax.set_xlabel ('Time step')
            self.dlg3.ui.widget.canvas.ax.set_ylabel ('Values')
            self.dlg3.ui.widget.canvas.ax.plot(dates, values)
            self.dlg3.ui.widget.canvas.ax.set_xticks(dates)  
            self.dlg3.ui.widget.canvas.ax.set_xticklabels(xlabels, rotation=30, fontsize=10) 
            self.dlg3.ui.widget.canvas.draw()
        else: 
            QMessageBox.information( self.iface.mainWindow(),"Info", "The are no PCRaster timeseries this directory")     
            self.dlg.show()


