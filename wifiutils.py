import os

#Version 1.1 - 19.04.2022
#Author: Luis Gutzeit

#sets the wifi in Linux to the specified ssid/psk
#attention: this removes all previosly defined wifi networks
def setWifi(ssid,psk):
    #write config file
    f = open("/etc/wpa_supplicant/wpa_supplicant.conf","w")
    f.write("""ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=DE""")
    f.write("\nnetwork={\n\tssid=\"")
    f.write(ssid)
    f.write("\"\n\tpsk=\"")
    f.write(psk)
    f.write("\"\n}")
    f.close()

    #reload config file
    os.system("wpa_cli -i wlan0 reconfigure")

#remove all Wifi networks
#attention: this removes all previosly defined wifi networks
def deleteWifi():
    #write config file
    f = open("/etc/wpa_supplicant/wpa_supplicant.conf","w")
    f.write("""ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=DE""")
    f.close()
    #reload config file
    os.system("wpa_cli -i wlan0 reconfigure")