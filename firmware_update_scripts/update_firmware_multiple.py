import serial.tools.list_ports
from serial import Serial
import subprocess, shlex
import os 
import time

dfu_filepath = "./capno_6_firmware_DFU_for_single_group.zip"

if not os.path.exists( dfu_filepath ): 
    raise ("DFU file is not found. Make sure you have entered correct path")

dfu_com = ""
dfu_baudrate = "115200"


ports = (list(serial.tools.list_ports.comports()))
nrf_ports = []
capnp_ports = []


for count, port in enumerate(ports):

    if "nRF52" in port.description and "Nordic" in port.manufacturer:
        nrf_ports.append(port)
        print ("Port: {}\tDFU Port: {}\tPID: {}\tVID: {}".format(count, port.name, port.pid, port.vid))


for port in nrf_ports: 
    dfu_com = port.name
    command = "nrfutil.exe dfu usb-serial -pkg {} -p {} -b {}".format( dfu_filepath, dfu_com, dfu_baudrate)
    command = shlex.split(command)

    print ("Programming: {}. Please wait...".format( port.name ))
    process = subprocess.Popen( command )
    process.wait()

    print ("Done programming.")


print ("Please wait. Checking if the programmed dongles are working fine...")
time.sleep(5)

ports = (list(serial.tools.list_ports.comports()))
for p in ports: 
    if p.vid == 3753 and p.pid == 49205:
        print ("Found CapnoTrainer P6.0 Dongle at {}".format(p.name))