import win32com.client

wmi = win32com.client.GetObject ("winmgmts:")
print("")

lst_devices = []

for usb in wmi.InstancesOf ("Win32_USBHub"):
    lst_devices.append(usb.DeviceID)
    print(usb.DeviceID) # Store this and check when another usb with Name = J-Link driver is plugged in 
    print(usb.Name) # J-Link driver
    print(usb.PNPDeviceID)
print("")

# while True:

# When connect button clicked, call this function

def CheckUsbDevices():
    # get list of current devices
    # filter through to devices that have Name = J-Link driver
    # search through device.JSON file if Id exists in it
    # if yes -> just say device connected and green circle
    # if not -> propmt user to enter name for new device
        # -> store device name and id in device.JSON