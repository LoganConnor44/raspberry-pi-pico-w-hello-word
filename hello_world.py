import sys
import network
import time
import urequests
from machine import Pin

def lightShow() :
    print("Internet Connection Made")
    print("Attempting To Request Public API Now")
    response = urequests.get("http://api.open-notify.org/astros.json").json()
    if response["message"] != "success" :
        print("Exiting : Improper Response Given")
        sys.exit()

    pin = Pin("LED", Pin.OUT)
    for astronaut in response["people"]:
        pin.toggle()
        # pin.off()
        print(astronaut['name'])
        time.sleep(2)


# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# wlan.connect(WIFI_NAME, WIFI_PASSWORD)

# if not wlan.isconnected() :
#     print("Exiting : No Internet Connection")
#     sys.exit()

