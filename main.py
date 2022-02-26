import os
from keep_alive import keep_alive
from nextcord.ext import commands


bot = commands.Bot(
	command_prefix=".",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 178927049698836480  # Change to your discord id!!!

@bot.command()
async def load(ctx,extension):
  bot.load_extension(f'cogs.{extension}')
  await ctx.send(f"The {extension} extension has been loaded")

@bot.command()
async def unload(ctx,extension):
  bot.unload_extension(f'cogs.{extension}')
  await ctx.send(f"The {extension} extension has been unloaded")

@bot.command(aliases=['r'])
async def reload(ctx,extension):
  bot.unload_extension(f'cogs.{extension}')
  await ctx.send(f"The {extension} extension has been unloaded")
  bot.load_extension(f'cogs.{extension}')
  await ctx.send(f"The {extension} extension has been reloaded")


for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_ready():
  print(f"{bot.user} is online!") #Checks when the bot is online and prints it to the console


keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("nextcord_BOT_SECRET") 
bot.run(token)  # Starts the bot