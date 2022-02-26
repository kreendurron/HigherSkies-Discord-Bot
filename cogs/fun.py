import nextcord
from nextcord.ext import commands


class Fun(commands.Cog): #Declares a cog name
  """Commands for The Bible Reading Challenge""" #Description of cog

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print('The Fun Cog is locked, loaded and ready.')

  @commands.command()
  async def test(self, ctx):

    embed = nextcord.Embed(title="test", description="Test description")
    await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Fun(bot))