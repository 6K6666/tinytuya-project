import tinytuya, discord, time
from configparser import ConfigParser

config = ConfigParser()  
bot = discord.Client()
config.read('config.ini')
prefix = "!"
token = ("PUT BOT TOKEN HERE")

@bot.event # Startup
async def on_ready():
    print(("I am running on " + bot.user.name))
    print(("With the ID: " + str(bot.user.id)))
    print("connected on " + str(len(bot.guilds)) + " servers:")

@bot.event
async def on_message(message):
    admin = config.get('settings', 'admin')
    if message.content.startswith(prefix + "shutdown"):
        if str(message.author.id) in admin:
            a = tinytuya.OutletDevice('16505438bcddc29c7d3d', '10.0.0.105', '63ea5d341f54cb10')
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
            a = tinytuya.OutletDevice('16505438bcddc29c7d3d', '10.0.0.105', '63ea5d341f54cb10')
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
            a = tinytuya.OutletDevice('16505438bcddc29c7d3d', '10.0.0.105', '63ea5d341f54cb10')
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