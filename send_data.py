import bluetooth
import time

bd_addr = "C4:8E:8F:BC:5A:18"
port = 1
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

def data(map_environment, direction):
    sock.send("map: " + str(map_environment) + "\n direction: " + str(direction))
    # time.sleep(5)
    
