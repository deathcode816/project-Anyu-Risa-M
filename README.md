# About Anyu Risa M project
My initial idea for this project was to allow a discord bot to interact with physical devices thorugh discord commands in the discord channel along with the ESP32, I believe using an ESP32 for this project isn't strictly required a average raspberry pi pico will be sufficient to do thought i haven't tested it out yet.

## Items I've used
- ESP32
- 1602IIC LCD
- 4 Jumper wires
- Breadboard
- USB A to USB C cable

- Discord bot
- Nextcord API
- PlatformIO IDE

## Setting it up
### Hardware Setup
- pin 14 to SCL
- pin 13 to SDA
- 5V to VDD
- GND to GND

note: make sure your VS studio code COM is properly connected, to check open device manager, go to ports and it should show something like 'USB-SERIAL CH340 (COM8)' make sure the com in visual studio code is the same

## Software Setup
### PlatformIO setup
- Install PlatformIO IDE extension in Visual studio code
- New project
- Select ESP32 Dev Module
- Arduino Framework
- other setting default

- put 'LiquidCrystal_I2C-1.1.2' inside lib

### Discord bot Setup
- [Use this person's helpful tutorial](https://www.youtube.com/watch?v=zrNloK9b1ro)

note: only the 'send messages' for the 'bot permission' should be enough for this project

### Anyu code
- paste the 'Anyu code' in main.cpp inside the src folder (feel free to rename the main.cpp file)
- make sure you put your Bot's token in client.run('Replace this sentence with your bot token')

To finnally run it, upload the 'main.cpp' then run 'Anyu.py' and message in the server your bot is in 'anyu print' followed by the sentence you want to display to the LCD and it should quickly display it
