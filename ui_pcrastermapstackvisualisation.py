# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pcrastermapstackvisualisation.ui'
#
# Created: Wed Jul  9 16:51:08 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PcrasterMapstackVisualisation(object):
    def setupUi(self, PcrasterMapstackVisualisation):
        PcrasterMapstackVisualisation.setObjectName(_fromUtf8("PcrasterMapstackVisualisation"))
        PcrasterMapstackVisualisation.resize(536, 326)
        self.txtBaseDir2_5 = QtGui.QLineEdit(PcrasterMapstackVisualisation)
        self.txtBaseDir2_5.setGeometry(QtCore.QRect(130, 10, 291, 31))
        self.txtBaseDir2_5.setObjectName(_fromUtf8("txtBaseDir2_5"))
        self.comboBox = QtGui.QComboBox(PcrasterMapstackVisualisation)
        self.comboBox.setGeometry(QtCore.QRect(20, 91, 221, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.line_19 = QtGui.QFrame(PcrasterMapstackVisualisation)
        self.line_19.setGeometry(QtCore.QRect(20, 270, 301, 20))
        self.line_19.setFrameShape(QtGui.QFrame.HLine)
        self.line_19.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_19.setObjectName(_fromUtf8("line_19"))
        self.line_5 = QtGui.QFrame(PcrasterMapstackVisualisation)
        self.line_5.setGeometry(QtCore.QRect(10, 200, 20, 81))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.pushButton_6 = QtGui.QPushButton(PcrasterMapstackVisualisation)
        self.pushButton_6.setGeometry(QtCore.QRect(250, 250, 61, 27))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_5 = QtGui.QPushButton(PcrasterMapstackVisualisation)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 210, 61, 27))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.label_17 = QtGui.QLabel(PcrasterMapstackVisualisation)
        self.label_17.setGeometry(QtCore.QRect(40, 250, 171, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setTextFormat(QtCore.Qt.AutoText)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.pushButton_7 = QtGui.QPushButton(PcrasterMapstackVisualisation)
        self.pushButton_7.setGeometry(QtCore.QRect(340, 60, 171, 27))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.line_6 = QtGui.QFrame(PcrasterMapstackVisualisation)
        self.line_6.setGeometry(QtCore.QRect(230, 200, 20, 81))
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.label_11 = QtGui.QLabel(PcrasterMapstackVisualisation)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 110, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setTextFormat(QtCore.Qt.AutoText)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_18 = QtGui.QLabel(PcrasterMapstackVisualisation)
        self.label_18.setGeometry(QtCore.QRect(20, 130, 231, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setTextFormat(QtCore.Qt.AutoText)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_16 = QtGui.QLabel(PcrasterMapstackVisualisation)
        self.label_16.setGeometry(QtCore.QRect(30, 210, 201, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setTextFormat(QtCore.Qt.AutoText)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.btnBaseDir_3 = QtGui.QPushButton(PcrasterMapstackVisualisation)
        self.btnBaseDir_3.setGeometry(QtCore.QRect(450, 10, 47, 30))
        self.btnBaseDir_3.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/pcrastermapstackvisualisation/dir.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBaseDir_3.setIcon(icon)
        self.btnBaseDir_3.setIconSize(QtCore.QSize(22, 22))
        self.btnBaseDir_3.setObjectName(_fromUtf8("btnBaseDir_3"))
        self.line_7 = QtGui.QFrame(PcrasterMapstackVisualisation)
        self.line_7.setGeometry(QtCore.QRect(310, 200, 20, 81))
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.comboBox_2 = QtGui.QComboBox(PcrasterMapstackVisualisation)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 150, 221, 27))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.line_18 = QtGui.QFrame(PcrasterMapstackVisualisation)
        self.line_18.setGeometry(QtCore.QRect(20, 190, 301, 20))
        self.line_18.setFrameShape(QtGui.QFrame.HLine)
        self.line_18.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_18.setObjectName(_fromUtf8("line_18"))
        self.label_15 = QtGui.QLabel(PcrasterMapstackVisualisation)
        self.label_15.setGeometry(QtCore.QRect(20, 71, 231, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setTextFormat(QtCore.Qt.AutoText)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.line_20 = QtGui.QFrame(PcrasterMapstackVisualisation)
        self.line_20.setGeometry(QtCore.QRect(20, 230, 301, 20))
        self.line_20.setFrameShape(QtGui.QFrame.HLine)
        self.line_20.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_20.setObjectName(_fromUtf8("line_20"))
        self.listWidget = QtGui.QListWidget(PcrasterMapstackVisualisation)
        self.listWidget.setGeometry(QtCore.QRect(340, 90, 171, 191))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.pushButton = QtGui.QPushButton(PcrasterMapstackVisualisation)
        self.pushButton.setGeometry(QtCore.QRect(190, 296, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(PcrasterMapstackVisualisation)
        QtCore.QMetaObject.connectSlotsByName(PcrasterMapstackVisualisation)

    def retranslateUi(self, PcrasterMapstackVisualisation):
        PcrasterMapstackVisualisation.setWindowTitle(QtGui.QApplication.translate("PcrasterMapstackVisualisation", "PcrasterMapstackVisualisation", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setToolTip(QtGui.QApplication.translate("PcrasterMapstackVisualisation", "Available PCRatser map series", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setToolTip(QtGui.QApplication.translate("PcrasterMapstackVisualisation", "Click to visualise", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("PcrasterMapstackVisualisation", "Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setToolTip(QtGui.QApplication.translate("PcrasterMapstackVisualisation", "Click to visualise", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("PcrasterMapstackVisualisation", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("PcrasterMapstackVisualisation", "visualisation of TSS Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("PcrasterMapstackVisualisation", "PCRaster mapstacks ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("PcrasterMapstackVisualisation", "Select Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("PcrasterMapstackVisualisation", "List of Time series files", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("PcrasterMapstackVisualisation", "visualisation of the mapstacks ", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBaseDir_3.setToolTip(QtGui.QApplication.translate("PcrasterMapstackVisualisation", "Select a base directory", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setToolTip(QtGui.QApplication.translate("PcrasterMapstackVisualisation", "Available PCRatser time series", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("PcrasterMapstackVisualisation", "List of corenames of the mapstacks ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("PcrasterMapstackVisualisation", "Close", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
