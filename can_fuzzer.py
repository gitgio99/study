import random, time, csv
import can

bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

ids = [0x100, 0x200, 0x7DF, 0x300, 0x7E0]
with open('logs/fuzz_results.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['t', 'count', 'id', 'data'])
    for i in range(1000):
        arb = random.choice(ids)
        data = [random.randint(0,255) for _ in range(random.randint(0,8))]
        msg = can.Message(arbitration_id=arb, data=data, is_extended_id=False)
        bus.send(msg)
        writer.writerow([time.time(), i, hex(arb), data])
        print(f"[{i}] sent {hex(arb)} {data}")
        time.sleep(0.01)
