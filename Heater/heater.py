import time
import datetime
import serial
from heaterUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
import sys
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import *
import visa
from simple_pid import PID
import numpy as np
import csv
import random
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QSizePolicy

#initialize globals
time_start_acquisition = 0
pyrometer_temp = 20
target_temp = 100
voltage_ser_open = False
flag_heating_running = False
flag_temp_capture_running = False
time_heating_start = 0
flag_actuator_on = False

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        #self.plot([random.random() for i in range(25)])
    def plot(self,data_x,data_y):
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.plot(data_x,data_y, 'r-')
        ax.set_title('Temperature Plot')
        self.draw()

class GetTempThread(QThread):
    temperature = pyqtSignal(float)
    def __init__(self,device):
        super(GetTempThread, self).__init__()
        self.Keysight_34972A  = device
    def run(self):
        global pyrometer_temp
        global flag_temp_capture_running
        global time_start_acquisition
        self.Keysight_34972A.write('*CLS')
        while flag_temp_capture_running == True:
            time.sleep(0.5)
            temp_acquired = self.Keysight_34972A.query('READ?')
            temp_acquired = temp_acquired.split(',')
            pyrometer_temp= np.round(float(temp_acquired[3])*20,2)
            self.temperature.emit(pyrometer_temp)#,float(pyrometer_temp[1]),float(pyrometer_temp[2]),float(pyrometer_temp[3])])

class ExportThread(QThread):
    def __init__(self):
        super(ExportThread, self).__init__()
    def run(self):
        global flag_temp_capture_running
        global pyrometer_temp
        currentDT = datetime.datetime.now()
        time_string = currentDT.strftime("%Y-%m-%d-%H-%M-%S")
        #time_string = str(currentDT)[0:10]+'-'+str(currentDT)[11:-1]
        csvfile= open(time_string+'.csv', 'w', newline='')
        DataWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        DataWriter.writerow(str(pyrometer_temp))
        while flag_temp_capture_running == True:
            time.sleep(0.5)
            currentDT = datetime.datetime.now()
            time_string = str(currentDT)[0:10]+'-'+str(currentDT)[11:-1]
            DataWriter.writerow([time_string,str(pyrometer_temp)])
            csvfile.flush()

class HeatingThread(QThread):
    def __init__(self,ser,PushStatus,voltage_heating):
        super(HeatingThread, self).__init__()
        global voltage_ser_open
        self.voltage_ser = ser
        self.PushStatus = PushStatus
        self.voltage_heating = voltage_heating

    def run(self):
        if voltage_ser_open == False:
            self.PushStatus('Please open COM first')
        else:
            self.SetHeating()
            self.PushStatus('Heating started')
    
    def SerialInput(self,input_command,ser):
        temp_command = input_command + '\r\n'
        ser.write(temp_command.encode())
        out = ''
        time.sleep(0.1)
        while ser.inWaiting() > 0:
            out += ser.read(1).decode()
            time.sleep(0.01)
        if out != '':
            return out
        ser.flush()

    def SetHeating(self):
        global pyrometer_temp
        global flag_heating_running
        global time_heating_start
        global flag_actuator_on
        global target_temp
        while True:
            while pyrometer_temp < target_temp-10:
                    while flag_actuator_on == False:  
                        readings = self.GetCurrentReading()
                        if readings is None:
                            pass
                        else:
                            time_heating_start = time.time()
                            if readings[5:9] != '0000':
                                flag_actuator_on = True
                    self.voltage_heating = self.voltage_heating.zfill(3)
                    self.SetVoltage(self.voltage_heating)
            while flag_heating_running == True:
                self.pid = PID(2.8,0.4,0.2,setpoint=target_temp)
                self.pid.sample_time = 0.1
                self.PushStatus('Switching to PID mode')
                self.voltage_heating = self.pid(pyrometer_temp)
                self.voltage_heating = int(np.round(self.voltage_heating,1)*10)
                self.SetVoltage(str(self.voltage_heating).zfill(3))
            self.SetVoltage('010')
            while flag_heating_running == False:
                self.PushStatus('Heating stopped')

    def GetCurrentReading(self):
        readings = self.SerialInput('GETD',self.voltage_ser)
        return readings

    def SetVoltage(self,voltage):
        self.SerialInput('VOLT'+voltage,self.voltage_ser)

class App(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)
        #initialize the flags
        global voltage_ser_open
        global flag_heating_running
        global flag_temp_capture_running
        #default ramping temperature
        self.voltage_heating = '150'
        #map the gui
        self.SetCOMPortsButton.clicked.connect(self.OpenCOMPorts)
        self.StartStopHeatingButton.clicked.connect(self.StartHeating)
        self.pushButton.clicked.connect(self.SetRampVoltage)
        #self.SetPIDButton.clicked.connect(self.SetPID)
        self.GetTempButton.clicked.connect(self.TempCapture)
        #Set the Keysight Config USE DEFAULT! Everything already set
        self.rm = visa.ResourceManager()
        self.Keysight_34972A =  self.rm.open_resource('USB0::0x0957::0x2007::MY57005122::0::INSTR')
        #set the temperature measuring thread
        self.th = GetTempThread(self.Keysight_34972A)
        self.th.temperature.connect(self.SetTempText)
        self.th.temperature.connect(self.PlotData)
        #set the heating thread
        self.ExportThread = ExportThread()
        #set the plotting arrays
        self.time_plot = np.array([], dtype = np.float32)
        self.temp_plot = np.array([], dtype = np.float32)
        #initialize the heater window
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Heating Program')
        self.plotter = PlotCanvas(self, width=5, height=4)
        self.plotter.move(450,190)

    def SetRampVoltage(self):
        self.voltage_heating = self.lineEdit.text()+'0'
        self.PushStatus('initial ramp voltage set to:' + self.lineEdit.text())

    # configure the serial connections (the parameters differs on the computer you are connecting to)
    def ConnectVoltageSerial(self, input_port):
        global voltage_ser_open
        ser = serial.Serial(
            port=input_port,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS
        )
        voltage_ser_open = True
        self.voltage_ser = ser
        self.heatingthread = HeatingThread(self.voltage_ser,self.PushStatus,self.voltage_heating)

    def TempCapture(self):
        global flag_temp_capture_running
        global time_start_acquisition
        if time_start_acquisition == 0:
            time_start_acquisition = time.time()

        if flag_temp_capture_running == False:
            flag_temp_capture_running = True
            self.th.start()
            self.ExportThread.start()
            self.PushStatus('temp acquisition started')
        else:
            flag_temp_capture_running = False
            self.PushStatus('temp acquisition stopped')

    def StartHeating(self):
        global flag_heating_running
        global target_temp
        if self.HeatingModeSelection.currentText() == '100C':
            target_temp = 102
            self.heatingthread.start()
        elif self.HeatingModeSelection.currentText() == '140C':
            target_temp = 143
            self.heatingthread.start()
        if flag_temp_capture_running  == False:
            self.TempCapture()
        if flag_heating_running == True:
            flag_heating_running = False
        else:
            flag_heating_running = True

    def SetTempText(self,temp):
        self.PyrometerTemp.setText(str(temp))

    def OpenCOMPorts(self):
        if voltage_ser_open == True:
            self.PushStatus("Voltage COM Port Already open")
            pass
        else:
            voltage_port = self.VoltageControlPortSelection.currentText()
            self.ConnectVoltageSerial(voltage_port)
            self.PushStatus("Voltage COM Port open")

    def PushStatus(self,status):
        self.label_4.setText('Status: '+ status)

    def PlotData(self,temp):
        global time_start_acquisition
        self.temp_plot = np.append(self.temp_plot,temp)
        self.time_plot = np.append(self.time_plot,time.time()-time_start_acquisition)
        self.plotter.plot(self.time_plot,self.temp_plot)
def main():
    app = QtWidgets.QApplication(sys.argv)
    w = App()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
