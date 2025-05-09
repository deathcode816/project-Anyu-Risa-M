from machine import I2C, Pin
from I2C_LCD import I2cLcd
import sys
import time

i2c = I2C(scl=Pin(14), sda=Pin(13), freq=400000)
devices = i2c.scan()

if len(devices) == 0:
    print("No I2C device found!")
    lcd = None
else:
    for device in devices:
        print("I2C addr: " + hex(device))
        lcd = I2cLcd(i2c, device, 2, 16)
        lcd.clear()
        lcd.putstr("ESP32 ready")

def process_commands(cmd):
    # Add special cases if you want
    if cmd.lower() == 'test':
        return 'works'
    return cmd  # Show whatever was sent

while True:
    try:
        line = sys.stdin.readline().strip()
        if line:
            response = process_commands(line)

            lcd.clear()
            lcd.move_to(0, 0)
            lcd.putstr(response[:16])  # Trim to 16 chars for LCD
            print("Displayed:", response)

    except Exception as e:
        print('Error:', e)

