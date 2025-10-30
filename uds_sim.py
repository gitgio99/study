import can
import time

bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

print("UDS SIM started - listening on vcan0")
while True:
    msg = bus.recv()
    if not msg:
        continue
    print("RX:", hex(msg.arbitration_id), msg.data)
    # 브로드캐스트 진단 요청(예시 ID 0x7DF) -> ECU 응답 0x7E8
    if msg.arbitration_id == 0x7DF:
        # 예: Session Control (SID 0x10) 요청에 대해 Positive(0x50) 응답
        resp = can.Message(arbitration_id=0x7E8, data=[0x03, 0x50, 0x01], is_extended_id=False)
        bus.send(resp)
        print("Sent:", hex(resp.arbitration_id), resp.data)
