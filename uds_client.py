import can
import time

bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

req = can.Message(arbitration_id=0x7DF, data=[0x02, 0x10, 0x01], is_extended_id=False)  # Session Control
bus.send(req)
print("Sent request:", req)
resp = bus.recv(timeout=1.0)
print("Recv:", resp)
