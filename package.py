#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'package.ui'
#
# Created: Wed Sep  4 11:46:57 2019
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QAbstractItemView
import sys
#import design

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        self.resize(562, 564)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 561, 561))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 2, 1, 1)
        self.listView = QtGui.QListView(self.tab)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 5)
        self.label_2 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.listView_2 = QtGui.QListView(self.tab)
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        self.listView_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.gridLayout.addWidget(self.listView_2, 4, 0, 1, 5)
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 3, 4, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 3, 1, 1)
        self.label = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #####-----------------------------------------
        self.listview_init()
        self.pushButton.clicked.connect(self.clicked)
        self.pushButton_2.clicked.connect(self.clicked_2)

#-----------------event for button----------------
    def clicked(self):
        model = self.listView.model()
        model_2 = self.listView_2.model()
        rm = 0
        for row in range(model.rowCount()):
            item = model.item(row)
            if item.checkState() == QtCore.Qt.Checked:
                #------------------
                print item.text() #package name
                #-----------------------
                i = QtGui.QStandardItem(item)
                i.setCheckState(QtCore.Qt.Unchecked)
                model_2.appendRow(i)
                rm = row
        model.removeRow(rm)
                

    def clicked_2(self):
        model = self.listView.model()
        model_2 = self.listView_2.model()
        rm = 0
        for row in range(model_2.rowCount()):
            item = model_2.item(row)
            if item.checkState() == QtCore.Qt.Checked:
                i = QtGui.QStandardItem(item)
                i.setCheckState(QtCore.Qt.Unchecked)
                model.appendRow(i)
                rm = row
        model_2.removeRow(rm)

#------------------------------------------------

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "+", None))
        self.label_2.setText(_translate("Dialog", "restricted package list", None))
        self.pushButton_2.setText(_translate("Dialog", "-", None))
        self.label.setText(_translate("Dialog", "package list", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tab 2", None))

#####-------------------list init----------------------
    def listview_init(self):
        model = QtGui.QStandardItemModel()
        model2 = QtGui.QStandardItemModel()
        self.listView.setModel(model)
        self.listView_2.setModel(model2)

        entry = ['1', '2']
        for i in entry:
            item = QtGui.QStandardItem(i)
            item.setCheckable(True)
            model.appendRow(item)

        entry = ['3', '4']
        for i in entry:
            item = QtGui.QStandardItem(i)
            item.setCheckable(True)
            model2.appendRow(item)
#---------------------------------

class ExampleApp(QtGui.QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QtGui.QApplication(sys.argv)
    win = ExampleApp()
    win.show()
    app.exec_()

if __name__ == '__main__':
    main()
