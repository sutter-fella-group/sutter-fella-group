import visa
import time
class test():
    def __init__(self):   
        self.rm = visa.ResourceManager()
        self.Keysight_34872A = self.rm.open_resource('USB0::0x0957::0x2007::MY57005122::0::INSTR')
        #print(self.Keysight_34872A.write('*IDN?'))
        #self.Keysight_34872A.write(':*CLS')
        #self.Keysight_34872A.write(':CONFigure:TEMPerature TCouple,T,(@101:103) ')
        #self.Keysight_34872A.write(':UNIT:TEMPerature C,(@101:103)')
        #self.Keysight_34872A.write(':SENSe:TEMPerature:NPLC 2,(@101:103)')
        #self.Keysight_34872A.write(':TRIGger:COUNt 1')
        #self.Keysight_34872A.write(':TRIGger:SOURce IMM') 
        
        self.Keysight_34872A.write(':ROUTe:SCAN (@101:104)')
        #self.Keysight_34872A.write(':INITiate')
        #self.Keysight_34872A.write('FORMat:READing:CHANnel 0')
        for i in range(1,10):
            print(self.Keysight_34872A.query(':READ?'))
            time.sleep(1)

if __name__ == "__main__":
    test()