import wmi
import time

w = wmi.WMI(namespace="root\\WMI")

controller = w.AsusAtkWmi_WMNB()[0]

print("Testing keyboard brightness...")

for level in range(4):
    print("Setting level:", level)
    
    # ASUS keyboard brightness control
    controller.DEVS(0x00120057, level)
    
    time.sleep(2)