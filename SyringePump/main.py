from design import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
import sys
import serial
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import *
import time
import numpy as np
import os

flag_running = True
vol1 = 0
vol2 = 0
class UpdateVolumeOneThread(QThread):
    Volume1update    = pyqtSignal(object)
    Volume2update    = pyqtSignal(object)
    def __init__(self,PumpOneVolume,PumpOneRate):
        super(UpdateVolumeOneThread, self).__init__()
        self.PumpOneVolume = PumpOneVolume
        self.PumpOneRate = PumpOneRate
    def run(self):
        self.UpdateLCD()
    def UpdateLCD(self):
        time_start = time.time()
        Volume1 = 0
        while Volume1 < float(self.PumpOneVolume.text()):
            Volume1 = (time.time()-time_start)*float(self.PumpOneRate.text())
            self.Volume1update.emit(np.round(Volume1,2))
            time.sleep(0.1)

class UpdateVolumeTwoThread(QThread):
    Volume2update    = pyqtSignal(object)
    def __init__(self,PumpTwoVolume,PumpTwoRate):
        super(UpdateVolumeTwoThread, self).__init__()
        self.PumpTwoVolume = PumpTwoVolume
        self.PumpTwoRate = PumpTwoRate

    def run(self):
        self.UpdateLCD2()

    def UpdateLCD2(self):
        time_start = time.time()
        Volume2 = 0
        while Volume2 < float(self.PumpTwoVolume.text()):
            Volume2 = (time.time()-time_start)*float(self.PumpTwoRate.text())  
            self.Volume2update.emit(np.round(Volume2,2)) 
            time.sleep(0.1)
             
class App(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self):
        super(App, self).__init__()
        self.pump_ser_open = False
        self.PumpOneisRunning = False            
        self.PumpTwoisRunning = False
        self.setupUi(self)

        self.SetCOMPortsButton.clicked.connect(self.OpenCOMPorts)
        self.SetPumpDirectionsButton.clicked.connect(self.SetDirections)
        self.RunPumpOneButton.clicked.connect(lambda: self.RunPump("00"))
        self.RunPumpTwoButton.clicked.connect(lambda: self.RunPump("01"))
        self.RunBothButton.clicked.connect(self.RunBoth)
        self.PumpStopButton.clicked.connect(self.StopPump)
        self.SetPumpVolumeButton.clicked.connect(self.SetVolume)
        self.SetPhaseButton.clicked.connect(self.SetPhaseForBoth)
        self.SetPumpRateButton.clicked.connect(self.SetCurrentPumpRate)
        self.PrintCommandButton.clicked.connect(self.ManualInput)
        self.SetPurgeButton.clicked.connect(self.SetPurge)
        self.SetDispenseButton.clicked.connect(self.SetDispense)
        #initialize Values
        self.PumpOneVolume.setText("0.02")
        self.PumpTwoVolume.setText("0.05")
        self.PumpOneRate.setText("21")
        self.PumpTwoRate.setText("3")
        self.updatethread_1 = UpdateVolumeOneThread(self.PumpOneVolume,self.PumpOneRate)
        self.updatethread_1.Volume1update.connect(self.UpdateDispensedVolume1)
        self.updatethread_2 = UpdateVolumeTwoThread(self.PumpTwoVolume,self.PumpTwoRate)
        self.updatethread_2.Volume2update.connect(self.UpdateDispensedVolume2)

    def SetPurge(self):
        self.SetProgramPhase('01','2')
        self.SerialInput('01 FUN STP')
        self.SetProgramPhase('01','1')
        self.SerialInput('01 FUN RAT')
        self.SerialInput('01 RAT 4')
        self.SerialInput('01 VOL 1')

    def SetDispense(self):
        global vol1
        global vol2
        if vol1 != 0:
            self.SetProgramPhase('01','2')
            self.SerialInput('01 FUN RAT')
            self.SerialInput('01 RAT 20')
            self.SerialInput('01 DIR WDR')
            self.SerialInput('01 VOL '+str(vol2))
            self.SetProgramPhase('00','2')
            self.SerialInput('00 FUN RAT')
            self.SerialInput('00 RAT 3')
            self.SerialInput('00 DIR WDR')
            self.SerialInput('00 VOL '+str(vol1))
            self.SetProgramPhase('01','1')
            self.SerialInput('01 FUN RAT')
            self.SerialInput('01 RAT 20')
            self.SerialInput('01 DIR INF')
            self.SerialInput('01 VOL '+str(vol2))
            self.SetProgramPhase('00','1')
            self.SerialInput('00 FUN RAT')
            self.SerialInput('00 RAT 3')
            self.SerialInput('00 DIR INF')
            self.SerialInput('00 VOL '+str(vol1))
        else: 
            self.PushStatus('Dispense Rate Set')


    def UpdateDispensedVolume1(self,volume):
        self.PumpOneDIsPensedVolume.setText(str(volume))

    def UpdateDispensedVolume2(self,volume):
        self.PumpTwoDisPensedVolume.setText(str(volume))

    def Reset(self):
        self.SetProgramPhase('00','1')
        self.SetProgramPhase('01','1')

    def SetPhaseForBoth(self):
        self.SetProgramPhase('00',str(self.spinBox.value()))
        self.SetProgramPhase('01',str(self.spinBox.value()))
        
    def ConnectPumpSerial(self,input_port):
        ser = serial.Serial(
            port=input_port,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS
        )
        self.pump_ser_open = True
        self.pump_ser = ser
        self.ser = ser

        #initialize the pause after priming
        self.SetProgramPhase('00','2')
        time.sleep(0.1)
        self.SetProgramPhase('01','2')
        self.SerialInput("00 FUN PAS 00")
        time.sleep(0.1)
        self.SerialInput("01 FUN PAS 00")

        #initialize the pause after dispense
        #self.SetProgramPhase('00','4')
        #self.SetProgramPhase('01','4')
        #self.SerialInput("00 FUN PAS 01")
        #self.SerialInput("01 FUN PAS 01")

        #return to phase 1
        self.SetProgramPhase('00','1')
        time.sleep(0.1)
        self.SetProgramPhase('01','1')
        
    def SerialInput(self,input_command):
        if hasattr(self, 'ser'):
            temp_command = input_command + '\r\n'
            self.ser.write(temp_command.encode())
            out = ''
            time.sleep(0.1)
            while self.ser.inWaiting() > 0:
                out += self.ser.read(1).decode()
            if out != '':
                self.SerialOutput.append(out[1:-1])
                return out[1:-1]
            self.ser.flushInput()
            self.ser.flush()
        else:
            self.PushStatus('COM Port Not Open. GO OPEN')

    def ManualInput(self):
        self.SerialInput(self.lineEdit.text())

    def SetProgramPhase(self,address,phase):
        self.SerialInput(address + ' PHN '+ phase)

    def OpenCOMPorts(self):
        if self.pump_ser_open == True:
            self.PushStatus("Pump COM Port Already open")
        else:
            Pump_Port = self.SyringePumpPortSelection.currentText()
            self.ConnectPumpSerial(Pump_Port)
            self.PushStatus("Pump COM Port open")

    def SetDirections(self):
        Pump_One_Direction = self.PumpOneDirection.text()
        self.SerialInput("00 DIR "+ Pump_One_Direction)
        Pump_Two_Direction = self.PumpTwoDirection.text()
        self.SerialInput("01 DIR "+ Pump_Two_Direction)
        self.PushStatus("Directions set")
    #def GetDirections(self):
     #   dir1 = self.SerialInput("00 DIR")
     #   dir2 = self.SerialInput("01 DIR")
     #   self.PumpOneDirection.setText(dir1)
     #   self.PumpTwoDirection.setText(dir2)

    #def GetCurrentPumpRate(self):
      #  global rat1
      #  global rat2
      #  self.PumpOneRate.setText(rat1)
      #  self.PumpOneRate.setText(rat2)

    def SetCurrentPumpRate(self):
        rat1 = self.PumpOneRate.text()
        rat2 = self.PumpTwoRate.text()
        self.SerialInput("00 RAT "+rat1+" MM")
        self.SerialInput("01 RAT "+rat2+" MM")
        self.PushStatus('new rate set')

    #def GetVolume(self):
       # vol1 = self.SerialInput("00 VOL")
       # self.PumpOneVolume.setText(vol1)
       # vol2 = self.SerialInput("01 VOL")
       # self.PumpOneVolume.setText(vol2)

    def SetVolume(self):
        global vol1
        global vol2
        vol1 = self.PumpOneVolume.text()
        vol2 = self.PumpTwoVolume.text()
        self.PushStatus('new volume set')

    def RunPump(self,address):
        if self.pump_ser_open == True:
            self.SerialInput(address + " RUN")
        else:
            self.PushStatus("Port Not Open")
        if address == '00':
            self.updatethread_1.start()
        else:
            self.updatethread_2.start()
        
    def RunBoth(self):
        self.RunPump('00')
        self.RunPump('01')

    def StopPump(self):
        global flag_running
        if flag_running == True:
            self.SerialInput('01 STP')
            self.SerialInput('00 STP')
            self.PushStatus('stopped')
            flag_running = False
        else:
            self.PushStatus('Already paused')

    def PushStatus(self,status):
        self.StatusLabel.setText("Status: " + status)

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = App()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
