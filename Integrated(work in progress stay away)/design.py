# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ALS_windows.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(789, 1188)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.StatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.StatusLabel.setGeometry(QtCore.QRect(30, 1060, 100, 39))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.StatusLabel.setFont(font)
        self.StatusLabel.setObjectName("StatusLabel")
        self.CameraImage = QtWidgets.QLabel(self.centralwidget)
        self.CameraImage.setGeometry(QtCore.QRect(863, 1043, 16, 27))
        self.CameraImage.setText("")
        self.CameraImage.setObjectName("CameraImage")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(18, 726, 189, 27))
        self.label_14.setObjectName("label_14")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 720, 235, 33))
        self.lineEdit.setObjectName("lineEdit")
        self.RunPumpOneButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.RunPumpOneButton_2.setGeometry(QtCore.QRect(470, 710, 91, 46))
        self.RunPumpOneButton_2.setObjectName("RunPumpOneButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 770, 301, 91))
        self.textEdit.setObjectName("textEdit")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(18, 18, 553, 145))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 1, 0, 1, 1)
        self.PumpOneRate = QtWidgets.QLineEdit(self.layoutWidget)
        self.PumpOneRate.setObjectName("PumpOneRate")
        self.gridLayout_5.addWidget(self.PumpOneRate, 1, 1, 1, 1)
        self.GetCurrentPumpRateButton = QtWidgets.QPushButton(self.layoutWidget)
        self.GetCurrentPumpRateButton.setObjectName("GetCurrentPumpRateButton")
        self.gridLayout_5.addWidget(self.GetCurrentPumpRateButton, 1, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 2, 0, 1, 1)
        self.PumpTwoRate = QtWidgets.QLineEdit(self.layoutWidget)
        self.PumpTwoRate.setObjectName("PumpTwoRate")
        self.gridLayout_5.addWidget(self.PumpTwoRate, 2, 1, 1, 1)
        self.SetPumpRateButton = QtWidgets.QPushButton(self.layoutWidget)
        self.SetPumpRateButton.setObjectName("SetPumpRateButton")
        self.gridLayout_5.addWidget(self.SetPumpRateButton, 2, 2, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 560, 485, 138))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Pump1DirLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.Pump1DirLabel.setObjectName("Pump1DirLabel")
        self.gridLayout_3.addWidget(self.Pump1DirLabel, 0, 0, 1, 1)
        self.PumpOneDirection = QtWidgets.QLineEdit(self.layoutWidget1)
        self.PumpOneDirection.setObjectName("PumpOneDirection")
        self.gridLayout_3.addWidget(self.PumpOneDirection, 0, 1, 1, 1)
        self.Pump2DirLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.Pump2DirLabel.setObjectName("Pump2DirLabel")
        self.gridLayout_3.addWidget(self.Pump2DirLabel, 1, 0, 1, 1)
        self.PumpTwoDirection = QtWidgets.QLineEdit(self.layoutWidget1)
        self.PumpTwoDirection.setObjectName("PumpTwoDirection")
        self.gridLayout_3.addWidget(self.PumpTwoDirection, 1, 1, 1, 1)
        self.GetPumpDirectionsButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.GetPumpDirectionsButton.setObjectName("GetPumpDirectionsButton")
        self.gridLayout_3.addWidget(self.GetPumpDirectionsButton, 2, 0, 1, 1)
        self.SetPumpDirectionsButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.SetPumpDirectionsButton.setObjectName("SetPumpDirectionsButton")
        self.gridLayout_3.addWidget(self.SetPumpDirectionsButton, 2, 1, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 180, 454, 171))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.PumpOneVolumeLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.PumpOneVolumeLabel.setObjectName("PumpOneVolumeLabel")
        self.gridLayout_4.addWidget(self.PumpOneVolumeLabel, 0, 0, 1, 1)
        self.PumpOneVolume = QtWidgets.QLineEdit(self.layoutWidget2)
        self.PumpOneVolume.setObjectName("PumpOneVolume")
        self.gridLayout_4.addWidget(self.PumpOneVolume, 1, 0, 1, 1)
        self.GetSetVolumeButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.GetSetVolumeButton.setObjectName("GetSetVolumeButton")
        self.gridLayout_4.addWidget(self.GetSetVolumeButton, 1, 1, 2, 1)
        self.PumpOneVolumeLabel_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.PumpOneVolumeLabel_2.setObjectName("PumpOneVolumeLabel_2")
        self.gridLayout_4.addWidget(self.PumpOneVolumeLabel_2, 2, 0, 1, 1)
        self.PumpTwoVolume = QtWidgets.QLineEdit(self.layoutWidget2)
        self.PumpTwoVolume.setObjectName("PumpTwoVolume")
        self.gridLayout_4.addWidget(self.PumpTwoVolume, 3, 0, 1, 1)
        self.SetPumpVolumeButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.SetPumpVolumeButton.setObjectName("SetPumpVolumeButton")
        self.gridLayout_4.addWidget(self.SetPumpVolumeButton, 3, 1, 1, 1)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 490, 314, 48))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.RunPumpOneButton = QtWidgets.QPushButton(self.layoutWidget3)
        self.RunPumpOneButton.setObjectName("RunPumpOneButton")
        self.gridLayout_11.addWidget(self.RunPumpOneButton, 0, 0, 1, 1)
        self.RunPumpTwoButton = QtWidgets.QPushButton(self.layoutWidget3)
        self.RunPumpTwoButton.setObjectName("RunPumpTwoButton")
        self.gridLayout_11.addWidget(self.RunPumpTwoButton, 0, 1, 1, 1)
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(30, 370, 152, 93))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)
        self.SetPhaseButton = QtWidgets.QPushButton(self.layoutWidget4)
        self.SetPhaseButton.setObjectName("SetPhaseButton")
        self.gridLayout.addWidget(self.SetPhaseButton, 1, 0, 1, 2)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget4)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 0, 1, 1, 1)
        self.layoutWidget5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(340, 370, 160, 164))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.layoutWidget5)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.ResetButton = QtWidgets.QPushButton(self.layoutWidget5)
        self.ResetButton.setObjectName("ResetButton")
        self.gridLayout_10.addWidget(self.ResetButton, 0, 0, 1, 1)
        self.PumpStopButton = QtWidgets.QPushButton(self.layoutWidget5)
        self.PumpStopButton.setObjectName("PumpStopButton")
        self.gridLayout_10.addWidget(self.PumpStopButton, 1, 0, 1, 1)
        self.RunBothButton = QtWidgets.QPushButton(self.layoutWidget5)
        self.RunBothButton.setObjectName("RunBothButton")
        self.gridLayout_10.addWidget(self.RunBothButton, 2, 0, 1, 1)
        self.layoutWidget6 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget6.setGeometry(QtCore.QRect(20, 880, 479, 121))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.layoutWidget6)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_4.setObjectName("label_4")
        self.gridLayout_7.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.PumpOneDIsPensedVolume = QtWidgets.QLineEdit(self.layoutWidget6)
        self.PumpOneDIsPensedVolume.setObjectName("PumpOneDIsPensedVolume")
        self.gridLayout_2.addWidget(self.PumpOneDIsPensedVolume, 0, 1, 1, 1)
        self.PumpTwoDisPensedVolume = QtWidgets.QLineEdit(self.layoutWidget6)
        self.PumpTwoDisPensedVolume.setObjectName("PumpTwoDisPensedVolume")
        self.gridLayout_2.addWidget(self.PumpTwoDisPensedVolume, 1, 1, 1, 1)
        self.ResetVolumeButton = QtWidgets.QPushButton(self.layoutWidget6)
        self.ResetVolumeButton.setObjectName("ResetVolumeButton")
        self.gridLayout_2.addWidget(self.ResetVolumeButton, 0, 2, 2, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(530, 190, 224, 216))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.SyringePumpPortLabel = QtWidgets.QLabel(self.layoutWidget_2)
        self.SyringePumpPortLabel.setObjectName("SyringePumpPortLabel")
        self.gridLayout_12.addWidget(self.SyringePumpPortLabel, 0, 0, 1, 1)
        self.SyringePumpPortSelection = QtWidgets.QComboBox(self.layoutWidget_2)
        self.SyringePumpPortSelection.setObjectName("SyringePumpPortSelection")
        self.SyringePumpPortSelection.addItem("")
        self.SyringePumpPortSelection.addItem("")
        self.SyringePumpPortSelection.addItem("")
        self.SyringePumpPortSelection.addItem("")
        self.SyringePumpPortSelection.addItem("")
        self.gridLayout_12.addWidget(self.SyringePumpPortSelection, 1, 0, 1, 1)
        self.VoltageControlPortLabel = QtWidgets.QLabel(self.layoutWidget_2)
        self.VoltageControlPortLabel.setObjectName("VoltageControlPortLabel")
        self.gridLayout_12.addWidget(self.VoltageControlPortLabel, 2, 0, 1, 1)
        self.VoltageControlPortSelection = QtWidgets.QComboBox(self.layoutWidget_2)
        self.VoltageControlPortSelection.setEditable(False)
        self.VoltageControlPortSelection.setObjectName("VoltageControlPortSelection")
        self.VoltageControlPortSelection.addItem("")
        self.VoltageControlPortSelection.addItem("")
        self.VoltageControlPortSelection.addItem("")
        self.VoltageControlPortSelection.addItem("")
        self.VoltageControlPortSelection.addItem("")
        self.gridLayout_12.addWidget(self.VoltageControlPortSelection, 3, 0, 1, 1)
        self.SetCOMPortsButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.SetCOMPortsButton.setObjectName("SetCOMPortsButton")
        self.gridLayout_12.addWidget(self.SetCOMPortsButton, 4, 0, 1, 1)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.CameraImage.raise_()
        self.StatusLabel.raise_()
        self.lineEdit.raise_()
        self.label_14.raise_()
        self.RunPumpOneButton_2.raise_()
        self.textEdit.raise_()
        self.layoutWidget_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 38))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(False)
        self.statusbar.setAutoFillBackground(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.VoltageControlPortSelection.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "In-sity Pump&Voltage Control"))
        self.StatusLabel.setText(_translate("MainWindow", "Status:"))
        self.label_14.setText(_translate("MainWindow", "Manual Serial Input"))
        self.RunPumpOneButton_2.setText(_translate("MainWindow", "print"))
        self.label_9.setText(_translate("MainWindow", "Pumping Rate (MM, UM)"))
        self.label_10.setText(_translate("MainWindow", "Pump1Rate"))
        self.GetCurrentPumpRateButton.setText(_translate("MainWindow", "Get Current Rate"))
        self.label_11.setText(_translate("MainWindow", "Pump2Rate"))
        self.SetPumpRateButton.setText(_translate("MainWindow", "Set Rate"))
        self.Pump1DirLabel.setText(_translate("MainWindow", "Pump1 Direction:"))
        self.Pump2DirLabel.setText(_translate("MainWindow", "Pump2 Direction:"))
        self.GetPumpDirectionsButton.setText(_translate("MainWindow", "Get Current Direction"))
        self.SetPumpDirectionsButton.setText(_translate("MainWindow", "Set Direction (INF WDR)"))
        self.PumpOneVolumeLabel.setText(_translate("MainWindow", "Pump 1 Vol (ml)"))
        self.GetSetVolumeButton.setText(_translate("MainWindow", "Get Current Volume"))
        self.PumpOneVolumeLabel_2.setText(_translate("MainWindow", "Pump 2 Vol (ml)"))
        self.SetPumpVolumeButton.setText(_translate("MainWindow", "Set Volume"))
        self.RunPumpOneButton.setText(_translate("MainWindow", "Run Pump 1"))
        self.RunPumpTwoButton.setText(_translate("MainWindow", "Run Pump 2"))
        self.label_13.setText(_translate("MainWindow", "Phase"))
        self.SetPhaseButton.setText(_translate("MainWindow", "Set Phase"))
        self.ResetButton.setText(_translate("MainWindow", "Reset Program"))
        self.PumpStopButton.setText(_translate("MainWindow", "STOP"))
        self.RunBothButton.setText(_translate("MainWindow", "Run Both"))
        self.label_4.setText(_translate("MainWindow", "Dispensed Volume (ml)"))
        self.ResetVolumeButton.setText(_translate("MainWindow", "Reset Volume"))
        self.label_5.setText(_translate("MainWindow", "Pump1"))
        self.label_6.setText(_translate("MainWindow", "Pump2"))
        self.SyringePumpPortLabel.setText(_translate("MainWindow", "New Era Syringe Pump"))
        self.SyringePumpPortSelection.setItemText(0, _translate("MainWindow", "COM1"))
        self.SyringePumpPortSelection.setItemText(1, _translate("MainWindow", "COM2"))
        self.SyringePumpPortSelection.setItemText(2, _translate("MainWindow", "COM3"))
        self.SyringePumpPortSelection.setItemText(3, _translate("MainWindow", "COM4"))
        self.SyringePumpPortSelection.setItemText(4, _translate("MainWindow", "COM5"))
        self.VoltageControlPortLabel.setText(_translate("MainWindow", "1867B Voltage Control"))
        self.VoltageControlPortSelection.setItemText(0, _translate("MainWindow", "COM1"))
        self.VoltageControlPortSelection.setItemText(1, _translate("MainWindow", "COM2"))
        self.VoltageControlPortSelection.setItemText(2, _translate("MainWindow", "COM3"))
        self.VoltageControlPortSelection.setItemText(3, _translate("MainWindow", "COM4"))
        self.VoltageControlPortSelection.setItemText(4, _translate("MainWindow", "COM5"))
        self.SetCOMPortsButton.setText(_translate("MainWindow", "Set COM Ports"))

