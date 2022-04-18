import os

def setWifi(ssid,psk):
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

    os.system("wpa_cli -i wlan0 reconfigure")

def deleteWifi():
    f = open("/etc/wpa_supplicant/wpa_supplicant.conf","w")
    f.write("""ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=DE""")
    f.close()

    os.system("wpa_cli -i wlan0 reconfigure")