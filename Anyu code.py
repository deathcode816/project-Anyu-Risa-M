# i dont even know what version this is now 3.1??
# this is the code for the bot

# imports
import nextcord # nextcord api
import serial # communicate to com8
import asyncio # used to allow other programms running while task is processing

# esp32
esp = serial.Serial('COM8', 115200, timeout=1)
awaitable_lock = asyncio.Lock()

# bot perms
intents = nextcord.Intents.default()

intents.message_content = True # state the bot permisison

client = nextcord.Client(intents=intents)

# bot login
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# bot function
@client.event

async def on_message(message): # requires intents.messages to be enabled, line 14 (doc messages on_message) DO NOT CHANGE ON_MESSAGE
    if message.author == client.user: 
        return
      
    if message.content.lower().startswith('anyu print'):
        user_msg = message.content[10:].strip()

        if not user_msg:
            await message.channel.send("You didn't say anything after \"anyu print\" :3")
            return

        if len(user_msg) > 32:
            await message.channel.send("Your sentence contains more than 32 characters :3")
            return

        try:
            async with awaitable_lock:
                esp.write((user_msg + "\n").encode())
                await asyncio.sleep(0.5) 
                response = esp.readline().decode().strip() 
        except Exception as e:
            response = f"Failed to send to ESP32: {e}"

        await message.channel.send(f"Sent: `{user_msg}`\nESP32 says: `{response}`")

        client.run('Replace this sentence with your bot token')
