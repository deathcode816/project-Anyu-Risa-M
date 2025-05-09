
import discord #imports discord library
import serial #allows communication over COM port
import asyncio #allows asynce such as async def functions

#set up the serial communication
esp = serial.Serial('COM8', 115200, timeout=1)  #update com to where the esp32 is connected
awaitable_lock = asyncio.Lock()  #prevent multiple commands talking to esp32

#set up bot and their permissions
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event #(required command decorator) tells te framework where it belongs, @client event is used for message,login,disconnect
async def on_ready(): #async allows for other task to run without waiting for this to run
    print(f'Logged in as {client.user}') #prints when the bot is ready

@client.event #refer from above
async def on_message(message): #defines a base class 'message'
    if message.author == client.user: #if the author is the bot's client.user it does nothing
        return

    if message.content.lower().startswith('anyu print'): #predefined event names from the discord.py library, its a special event handler such as on_message, on_ready
        user_msg = message.content[10:].strip()  # this is linked to message.content above, it skips the 10 characters .strip() prevents unclear spaces

        if not user_msg: #condition if user_msg is absent after user_msg
            await message.channel.send("You didn't say anything after 'hey bot'!")
            return #do nothing if error

        try:
            async with awaitable_lock:  #asynce with prevent race conditions / preventing corruption due to multiple task writing in the port | awaitable_lock can be any
                esp.write((user_msg + "\n").encode()) #serial.write only allows bytes so encoding the message is nessesary
                await asyncio.sleep(0.5) #gives time for esp32 to respond
                response = esp.readline().decode().strip() #takes the response from esp.readline and decode from esp32 encoding it
        except Exception as e: #Exception is not specific but needs to exist to be safe (could cause KeyboardInteruppt, or System exit)
            response = f"Failed to send to ESP32: {e}"

        await message.channel.send(f"Sent: `{user_msg}`\nESP32 says: `{response}`") #prints if error occurs

client.run(TOKEN)
