import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='%')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")
@bot.command()
async def whoami(ctx)
  embed = discord.Embed(title="Python Bot", description="This is who made me!", color=0xeee657)
     embed.add_field(name="Code Author", "XXWolfBane#5559")
     embed.add_field(name="Guild owner", owner_id)
     
    await ctx.send(embed=embed)
    
bot.run('NDYzOTYwNDgwMzAyNjI4ODY0.Dh4AYg.l8hv8IV-B3MhZmyvMA94YpnN6oc')
