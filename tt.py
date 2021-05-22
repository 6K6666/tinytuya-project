import tinytuya, discord, time, requests
from configparser import ConfigParser
from discord_webhook import DiscordWebhook

config = ConfigParser()  
bot = discord.Client()
config.read('config.ini')


# SET THESE GLOBAL VARIABLES

device_id = ("device ID of the tuya compatible device")
ip_address = ("ip address of the tuya compatible device")
local_key = ("local key of the tuya compatible device")
prefix = "!"
token = ("TOKEN HERE")
webhook = "WEBHOOK HERE"

# DISCORD BOT

@bot.event # Startup
async def on_ready():
    print(("I am running on " + bot.user.name))
    print(("With the ID: " + str(bot.user.id)))
    print("connected on " + str(len(bot.guilds)) + " servers")

@bot.event # Bot commands
async def on_message(message):
    admin = config.get('settings', 'admin')
    if message.content.startswith(prefix + "shutdown"):
        if str(message.author.id) in admin:
            a = tinytuya.OutletDevice(device_id, ip_address, local_key)
            a.set_version(3.3)
            a.turn_off()
            data = a.status() 
            print('set_status() result %r' % data)
            embed=discord.Embed(title="Success!", color=0x0000ff, description="Shutdown command successfully executed.")
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title="Error!", color=0xFF0000, description="You're not a bot admin. Only bot admins have access to this command.")
            await message.channel.send(embed=embed)

    if message.content.startswith(prefix + "restart"):
        if str(message.author.id) in admin:
            a = tinytuya.OutletDevice(device_id, ip_address, local_key)
            a.set_version(3.3)
            a.turn_off()
            data = a.status() 
            print('set_status() result %r' % data)
            time.sleep(5)
            a.turn_on()
            data = a.status() 
            print('set_status() result %r' % data)
            embed=discord.Embed(title="Success!", color=0x0000ff, description="Restart command successfully executed. The server *should* come back online shortly.")
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title="Error!", color=0xFF0000, description="You're not a bot admin. Only bot admins have access to this command.")
            await message.channel.send(embed=embed)

    if message.content.startswith(prefix + "start"):
        if str(message.author.id) in admin:
            a = tinytuya.OutletDevice(device_id, ip_address, local_key)
            a.set_version(3.3)
            a.turn_on()
            data = a.status() 
            print('set_status() result %r' % data)
            embed=discord.Embed(title="Success!", color=0x0000ff, description="Start command successfully executed. The server *should* come online shortly.")
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title="Error!", color=0xFF0000, description="You're not a bot admin. Only bot admins have access to this command.")
            await message.channel.send(embed=embed)

bot.run(token)

# while True: # uptime check and automatic restart || I added this for my own convienience. Uncomment if you know how to modify it to fit your needs and know what you're doing.
#    check = requests.get("https://voided.dev")
#    if check.status_code == 523:
#        a = tinytuya.OutletDevice(device_id, ip_address, local_key)
#        a.set_version(3.3)
#        a.turn_off()
#        data = a.status() 
#        print('set_status() result %r' % data)
#        time.sleep(5)
#        a.turn_on()
#        data = a.status() 
#        print('set_status() result %r' % data)
#        webhook = DiscordWebhook(url=webhook, content='')
#        response = webhook.execute()
#    time.sleep(3)
