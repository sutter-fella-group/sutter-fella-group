# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Syringepump.ui'
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
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 1, 0, 1, 1)
        self.PumpOneRate = QtWidgets.QLineEdit(self.centralwidget)
        self.PumpOneRate.setObjectName("PumpOneRate")
        self.gridLayout_5.addWidget(self.PumpOneRate, 1, 1, 1, 1)
        self.GetCurrentPumpRateButton = QtWidgets.QPushButton(self.centralwidget)
        self.GetCurrentPumpRateButton.setObjectName("GetCurrentPumpRateButton")
        self.gridLayout_5.addWidget(self.GetCurrentPumpRateButton, 1, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 2, 0, 1, 1)
        self.PumpTwoRate = QtWidgets.QLineEdit(self.centralwidget)
        self.PumpTwoRate.setObjectName("PumpTwoRate")
        self.gridLayout_5.addWidget(self.PumpTwoRate, 2, 1, 1, 1)
        self.SetPumpRateButton = QtWidgets.QPushButton(self.centralwidget)
        self.SetPumpRateButton.setObjectName("SetPumpRateButton")
        self.gridLayout_5.addWidget(self.SetPumpRateButton, 2, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 5)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.PumpOneVolumeLabel = QtWidgets.QLabel(self.centralwidget)
        self.PumpOneVolumeLabel.setObjectName("PumpOneVolumeLabel")
        self.gridLayout_4.addWidget(self.PumpOneVolumeLabel, 0, 0, 1, 1)
        self.PumpOneVolume = QtWidgets.QLineEdit(self.centralwidget)
        self.PumpOneVolume.setObjectName("PumpOneVolume")
        self.gridLayout_4.addWidget(self.PumpOneVolume, 1, 0, 1, 1)
        self.GetSetVolumeButton = QtWidgets.QPushButton(self.centralwidget)
        self.GetSetVolumeButton.setObjectName("GetSetVolumeButton")
        self.gridLayout_4.addWidget(self.GetSetVolumeButton, 1, 1, 2, 1)
        self.PumpOneVolumeLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.PumpOneVolumeLabel_2.setObjectName("PumpOneVolumeLabel_2")
        self.gridLayout_4.addWidget(self.PumpOneVolumeLabel_2, 2, 0, 1, 1)
        self.PumpTwoVolume = QtWidgets.QLineEdit(self.centralwidget)
        self.PumpTwoVolume.setObjectName("PumpTwoVolume")
        self.gridLayout_4.addWidget(self.PumpTwoVolume, 3, 0, 1, 1)
        self.SetPumpVolumeButton = QtWidgets.QPushButton(self.centralwidget)
        self.SetPumpVolumeButton.setObjectName("SetPumpVolumeButton")
        self.gridLayout_4.addWidget(self.SetPumpVolumeButton, 3, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 1, 0, 1, 4)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.SyringePumpPortLabel = QtWidgets.QLabel(self.centralwidget)
        self.SyringePumpPortLabel.setObjectName("SyringePumpPortLabel")
        self.gridLayout_12.addWidget(self.SyringePumpPortLabel, 0, 0, 1, 1)
        self.SyringePumpPortSelection = QtWidgets.QComboBox(self.centralwidget)
        self.SyringePumpPortSelection.setObjectName("SyringePumpPortSelection")
        self.SyringePumpPortSelection.addItem("")
        self.SyringePumpPortSelection.addItem("")
        self.SyringePumpPortSelection.addItem("")
        self.SyringePumpPortSelection.addItem("")
        self.SyringePumpPortSelection.addItem("")
        self.gridLayout_12.addWidget(self.SyringePumpPortSelection, 1, 0, 1, 1)
        self.SetCOMPortsButton = QtWidgets.QPushButton(self.centralwidget)
        self.SetCOMPortsButton.setObjectName("SetCOMPortsButton")
        self.gridLayout_12.addWidget(self.SetCOMPortsButton, 2, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_12, 1, 4, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)
        self.SetPhaseButton = QtWidgets.QPushButton(self.centralwidget)
        self.SetPhaseButton.setObjectName("SetPhaseButton")
        self.gridLayout.addWidget(self.SetPhaseButton, 1, 0, 1, 2)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.ResetButton = QtWidgets.QPushButton(self.centralwidget)
        self.ResetButton.setObjectName("ResetButton")
        self.gridLayout_10.addWidget(self.ResetButton, 0, 0, 1, 1)
        self.PumpStopButton = QtWidgets.QPushButton(self.centralwidget)
        self.PumpStopButton.setObjectName("PumpStopButton")
        self.gridLayout_10.addWidget(self.PumpStopButton, 1, 0, 1, 1)
        self.RunBothButton = QtWidgets.QPushButton(self.centralwidget)
        self.RunBothButton.setObjectName("RunBothButton")
        self.gridLayout_10.addWidget(self.RunBothButton, 2, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_10, 2, 2, 2, 2)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.RunPumpOneButton = QtWidgets.QPushButton(self.centralwidget)
        self.RunPumpOneButton.setObjectName("RunPumpOneButton")
        self.gridLayout_11.addWidget(self.RunPumpOneButton, 0, 0, 1, 1)
        self.RunPumpTwoButton = QtWidgets.QPushButton(self.centralwidget)
        self.RunPumpTwoButton.setObjectName("RunPumpTwoButton")
        self.gridLayout_11.addWidget(self.RunPumpTwoButton, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_11, 3, 0, 1, 2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Pump1DirLabel = QtWidgets.QLabel(self.centralwidget)
        self.Pump1DirLabel.setObjectName("Pump1DirLabel")
        self.gridLayout_3.addWidget(self.Pump1DirLabel, 0, 0, 1, 1)
        self.PumpOneDirection = QtWidgets.QLineEdit(self.centralwidget)
        self.PumpOneDirection.setObjectName("PumpOneDirection")
        self.gridLayout_3.addWidget(self.PumpOneDirection, 0, 1, 1, 1)
        self.Pump2DirLabel = QtWidgets.QLabel(self.centralwidget)
        self.Pump2DirLabel.setObjectName("Pump2DirLabel")
        self.gridLayout_3.addWidget(self.Pump2DirLabel, 1, 0, 1, 1)
        self.PumpTwoDirection = QtWidgets.QLineEdit(self.centralwidget)
        self.PumpTwoDirection.setObjectName("PumpTwoDirection")
        self.gridLayout_3.addWidget(self.PumpTwoDirection, 1, 1, 1, 1)
        self.GetPumpDirectionsButton = QtWidgets.QPushButton(self.centralwidget)
        self.GetPumpDirectionsButton.setObjectName("GetPumpDirectionsButton")
        self.gridLayout_3.addWidget(self.GetPumpDirectionsButton, 2, 0, 1, 1)
        self.SetPumpDirectionsButton = QtWidgets.QPushButton(self.centralwidget)
        self.SetPumpDirectionsButton.setObjectName("SetPumpDirectionsButton")
        self.gridLayout_3.addWidget(self.SetPumpDirectionsButton, 2, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 4, 0, 1, 4)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout_6.addWidget(self.label_14, 5, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_6.addWidget(self.lineEdit, 5, 1, 1, 2)
        self.PrintCommandButton = QtWidgets.QPushButton(self.centralwidget)
        self.PrintCommandButton.setObjectName("PrintCommandButton")
        self.gridLayout_6.addWidget(self.PrintCommandButton, 5, 3, 1, 2)
        self.SerialOutput = QtWidgets.QTextEdit(self.centralwidget)
        self.SerialOutput.setObjectName("SerialOutput")
        self.gridLayout_6.addWidget(self.SerialOutput, 6, 0, 1, 2)
        self.GetPhaseButton = QtWidgets.QPushButton(self.centralwidget)
        self.GetPhaseButton.setObjectName("GetPhaseButton")
        self.gridLayout_6.addWidget(self.GetPhaseButton, 6, 2, 1, 3)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_7.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.PumpOneDIsPensedVolume = QtWidgets.QLineEdit(self.centralwidget)
        self.PumpOneDIsPensedVolume.setObjectName("PumpOneDIsPensedVolume")
        self.gridLayout_2.addWidget(self.PumpOneDIsPensedVolume, 0, 1, 1, 1)
        self.PumpTwoDisPensedVolume = QtWidgets.QLineEdit(self.centralwidget)
        self.PumpTwoDisPensedVolume.setObjectName("PumpTwoDisPensedVolume")
        self.gridLayout_2.addWidget(self.PumpTwoDisPensedVolume, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_7, 7, 0, 1, 2)
        self.StatusLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.StatusLabel.setFont(font)
        self.StatusLabel.setObjectName("StatusLabel")
        self.gridLayout_6.addWidget(self.StatusLabel, 8, 0, 1, 1)
        self.CameraImage = QtWidgets.QLabel(self.centralwidget)
        self.CameraImage.setText("")
        self.CameraImage.setObjectName("CameraImage")
        self.gridLayout_6.addWidget(self.CameraImage, 8, 5, 1, 1)
        self.CameraImage.raise_()
        self.StatusLabel.raise_()
        self.lineEdit.raise_()
        self.label_14.raise_()
        self.PrintCommandButton.raise_()
        self.SerialOutput.raise_()
        self.GetPhaseButton.raise_()
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "In-sity Pump&Voltage Control"))
        self.label_9.setText(_translate("MainWindow", "Pumping Rate (MM, UM)"))
        self.label_10.setText(_translate("MainWindow", "Pump1Rate"))
        self.GetCurrentPumpRateButton.setText(_translate("MainWindow", "Get Current Rate"))
        self.label_11.setText(_translate("MainWindow", "Pump2Rate"))
        self.SetPumpRateButton.setText(_translate("MainWindow", "Set Rate"))
        self.PumpOneVolumeLabel.setText(_translate("MainWindow", "Pump 1 Vol (ml)"))
        self.GetSetVolumeButton.setText(_translate("MainWindow", "Get Current Volume"))
        self.PumpOneVolumeLabel_2.setText(_translate("MainWindow", "Pump 2 Vol (ml)"))
        self.SetPumpVolumeButton.setText(_translate("MainWindow", "Set Volume"))
        self.SyringePumpPortLabel.setText(_translate("MainWindow", "New Era Syringe Pump"))
        self.SyringePumpPortSelection.setItemText(0, _translate("MainWindow", "COM1"))
        self.SyringePumpPortSelection.setItemText(1, _translate("MainWindow", "COM2"))
        self.SyringePumpPortSelection.setItemText(2, _translate("MainWindow", "COM3"))
        self.SyringePumpPortSelection.setItemText(3, _translate("MainWindow", "COM4"))
        self.SyringePumpPortSelection.setItemText(4, _translate("MainWindow", "COM5"))
        self.SetCOMPortsButton.setText(_translate("MainWindow", "Set COM Ports"))
        self.label_13.setText(_translate("MainWindow", "Phase"))
        self.SetPhaseButton.setText(_translate("MainWindow", "Set Phase"))
        self.ResetButton.setText(_translate("MainWindow", "Reset Program"))
        self.PumpStopButton.setText(_translate("MainWindow", "STOP"))
        self.RunBothButton.setText(_translate("MainWindow", "Run Both"))
        self.RunPumpOneButton.setText(_translate("MainWindow", "Run Pump 1"))
        self.RunPumpTwoButton.setText(_translate("MainWindow", "Run Pump 2"))
        self.Pump1DirLabel.setText(_translate("MainWindow", "Pump1 Direction:"))
        self.Pump2DirLabel.setText(_translate("MainWindow", "Pump2 Direction:"))
        self.GetPumpDirectionsButton.setText(_translate("MainWindow", "Get Current Direction"))
        self.SetPumpDirectionsButton.setText(_translate("MainWindow", "Set Direction (INF WDR)"))
        self.label_14.setText(_translate("MainWindow", "Manual Serial Input"))
        self.PrintCommandButton.setText(_translate("MainWindow", "print"))
        self.SerialOutput.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.GetPhaseButton.setText(_translate("MainWindow", "Get current Phase"))
        self.label_4.setText(_translate("MainWindow", "Dispensed Volume (ml)"))
        self.label_6.setText(_translate("MainWindow", "Pump2"))
        self.label_5.setText(_translate("MainWindow", "Pump1"))
        self.StatusLabel.setText(_translate("MainWindow", "Status:"))

