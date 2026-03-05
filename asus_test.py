import wmi

w = wmi.WMI(namespace="root\\WMI")

print("Available WMI classes:\n")

for cls in w.classes:
    if "ASUS" in cls.upper() or "ATK" in cls.upper():
        print(cls)