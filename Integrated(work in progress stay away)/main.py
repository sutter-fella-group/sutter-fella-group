from design import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
import sys
import serial
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import *
import cv2
import time
import numpy as np
#import uvc_radiometry
import os

class CamThread(QThread):
    changePixmap = pyqtSignal(QImage)

    def run(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                p = convertToQtFormat.scaled(480, 360, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
    
    
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
        self.voltage_ser_open = False
        self.pump_ser_open = False
        self.PumpOneisRunning = False            
        self.PumpTwoisRunning = False
        self.setupUi(self)

        self.SetCOMPortsButton.clicked.connect(self.OpenCOMPorts)
        #self.StartCamCaptureButton.clicked.connect(self.CameraStart)
        self.SetPumpDirectionsButton.clicked.connect(self.SetDirections)
        self.GetPumpDirectionsButton.clicked.connect(self.GetDirections)
        self.RunPumpOneButton.clicked.connect(lambda: self.RunPump("00"))
        self.RunPumpTwoButton.clicked.connect(lambda: self.RunPump("01"))

        self.RunBothButton.clicked.connect(self.RunBoth)
        self.PumpStopButton.clicked.connect(self.StopPump)
        self.GetSetVolumeButton.clicked.connect(self.GetVolume)
        self.SetPumpVolumeButton.clicked.connect(self.SetVolume)
        self.th = CamThread(self)
        self.th.changePixmap.connect(self.setImage)


        #initialize Values
        self.PumpOneVolume.setText("1")
        self.PumpTwoVolume.setText("1")
        self.PumpOneRate.setText("0.1")
        self.PumpTwoRate.setText("0.1")


        self.updatethread_1 = UpdateVolumeOneThread(self.PumpOneVolume,self.PumpOneRate)
        self.updatethread_1.Volume1update.connect(self.UpdateDispensedVolume1)
        self.updatethread_2 = UpdateVolumeTwoThread(self.PumpTwoVolume,self.PumpTwoRate)
        self.updatethread_2.Volume2update.connect(self.UpdateDispensedVolume2)
        

    def setImage(self, image):
        self.CameraImage.setPixmap(QPixmap.fromImage(image))

    def UpdateDispensedVolume1(self,volume):
        self.PumpOneDIsPensedVolume.setText(str(volume))
    def UpdateDispensedVolume2(self,volume):
        self.PumpTwoDisPensedVolume.setText(str(volume))

    def ConnectPumpSerial(self,input_port):
        ser = serial.Serial(
            port=input_port,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS
        )
        global pump_ser
        self.pump_ser_open = True
        pump_ser = ser

        #initialize the pause after priming
        self.SetProgramPhase('00','02')
        self.SetProgramPhase('01','02')
        self.SerialInput("00 FUN PAS 00",pump_ser)
        self.SerialInput("01 FUN PAS 00",pump_ser)

        #initialize the pause after dispense
        self.SetProgramPhase('00','04')
        self.SetProgramPhase('01','04')
        self.SerialInput("00 FUN PAS 2",pump_ser)
        self.SerialInput("01 FUN PAS 2",pump_ser)
        

    def SerialInput(self,input_command,ser):
        ser.write(input_command + '\r\n')
        out = ''
        time.sleep(0.1)
        while ser.inWaiting() > 0:
            out += ser.read(1)
        if out != '':
            print(out)
            return out
        ser.flushInput()
        ser.flush()

    def GetProgramPhase(self,address):
        phase = self.SerialInput(address + ' PHN', pump_ser)
        self.PushStatus("Current Phase is" + str(phase))

    def SetProgramPhase(self,address,phase):
        self.SerialInput(address + ' PHN '+ phase, pump_ser)

    def OpenCOMPorts(self):
        #if self.pump_ser_open == True:
        if True:
            self.PushStatus("Pump COM Port Already open")
        else:
            Pump_Port = self.SyringePumpPortSelection.currentText()
            self.ConnectPumpSerial(Pump_Port)
            self.PushStatus("Pump COM Port open")

    def SetDirections(self):
        Pump_One_Direction = self.PumpOneDirection.text()
        self.SerialInput("00 DIR "+ Pump_One_Direction,pump_ser)
        Pump_Two_Direction = self.PumpTwoDirection.text()
        self.SerialInput("01 DIR "+ Pump_Two_Direction,pump_ser)
        self.PushStatus("Directions set")

    def GetDirections(self):
        dir1 = self.SerialInput("00 DIR",pump_ser)
        dir2 = self.SerialInput("01 DIR",pump_ser)
        self.PumpOneDirection.setText(dir1)
        self.PumpTwoDirection.setText(dir2)

    def GetVolume(self):
        self.SetProgramPhase('00','03')
        self.SetProgramPhase('01','03')
        vol1 = self.SerialInput("00 VOL",pump_ser)
        self.PumpOneVolume.setText(vol1)
        vol2 = self.SerialInput("01 VOL",pump_ser)
        self.PumpOneVolume.setText(vol2)



    def SetVolume(self):
        self.SetProgramPhase('00','03')
        self.SetProgramPhase('01','03')
        vol1 = self.PumpOneVolume.text()
        vol2 = self.PumpTwoVolume.text()
        self.SerialInput("00 VOL" + vol1,pump_ser)
        self.SerialInput("00 VOL" + vol2,pump_ser)

    def RunPump(self,address):
        if self.pump_ser_open == True:
            self.SerialInput(address + " RUN",pump_ser)
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
        global flag_stop
        if flag_stop != True:
            self.SerialInput('STP',pump_ser)
            self.PushStatus('paused')
            flag_stop = True
        else:
            self.PushStatus('Already paused')

    def SetPrimeVolume(self):
        self.SetProgramPhase('00','01')
        self.SetProgramPhase('01','01')
        vol1 = self.PumpOnePrimeVolumeInput_2.text()
        vol2 = self.PumpTwoPrimeVolumeInput.text()
        self.SerialInput("00 VOL" + vol1,pump_ser)
        self.SerialInput("01 VOL" + vol2,pump_ser)
        self.PushStatus("Priming volume set")

    def PrimePump(self):
        self.SetProgramPhase('00','01')
        self.SetProgramPhase('01','01')
        self.SerialInput("RUN",pump_ser)
        self.SerialInput("RUN",pump_ser)
        self.PushStatus("Priming pumps")

    def CameraStart(self):
        #os.system('python3 uvc_radiometry.py')
        #os.system('python3 cameraexample.py')

        self.th.start()
        self.PushStatus("CameraStarted")

    def CameraStopped(self):
        print('CamerStopped')

    def PushStatus(self,status):
        self.StatusLabel.setText("Status: " + status)

    def SetVoltage(self,voltage):
        self.SerialInput('VOLT'+str(voltage),voltage_ser)
    
    def GetVoltage(self,voltage):
        self.SerialInput('GETD',voltage_ser)

    def SetHeating(self):
        if self.HeatingModeSelection.currentText() == '110C':
            RC = 100
            a = 0.4
            #while temp_substrate < 90
            while True:
                time_start = time.time()
                t = time.time()-time_start
                voltage_heating = np.sqrt(240*RC*(a*np.exp(-a*(t)))/(1+np.exp(-a*(t)))^2)
                self.SetVoltage(voltage_heating)
                time.sleep(0.1)

            #add in slow voltage for maintaining


            
def main():
    app = QtWidgets.QApplication(sys.argv)
    w = App()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
