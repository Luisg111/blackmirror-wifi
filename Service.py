from tkinter import StringVar
from bluez_peripheral.gatt.service import Service
from bluez_peripheral.gatt.characteristic import characteristic, CharacteristicFlags as CharFlags
import wifiutils
import struct

#Version 1.1 - 19.04.2022
#Author: Luis Gutzeit
#some parts of this code have been taken from the official documentation of bluez_peripheral

#this service handles the transfer of wifi data
class WifiService(Service):
    ssid = ""
    psk = ""

    def __init__(self):
        super().__init__("844F", True)

    #method to change wifi credentials
    def setWifi(self):
        #print("Wifi wird gestartet mit")
        #print("SSID: "+self.ssid)
        #print("PSK: "+self.psk)
        try:
            wifiutils.setWifi(self.ssid,self.psk)
        except Exception as e:
            print(e)

    #characteristic to change ssid    
    @characteristic("2C33", CharFlags.WRITE).setter
    def ssidCharacteristic(self, value,options):
        try:
            stringValue = value.decode("utf-8")
            #print("ssid: "+ stringValue+"\n")
            self.ssid = stringValue
        except:
            print("ssid: received invalid message")
        
    #characteristic to change psk/key 
    @characteristic("2C34", CharFlags.WRITE).setter
    def pskCharacteristic(self, value,options):
        try:
            stringValue = value.decode("utf-8")
            #print("psk: "+ stringValue + "\n")
            self.psk = stringValue
        except: 
            print("psk: received invalid message")
        self.setWifi()


