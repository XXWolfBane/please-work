@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Python Bot", description="I'm a new bot you expect me to have commands?", color=0xeee657)
     embed.add_field(name="If this works.")
     
    await ctx.send(embed=embed)
