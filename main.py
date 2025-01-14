import discord
import os
import datetime
from discord.ext import commands, tasks

# intents object
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# channels
billDatesChannel = 1328684407837425787
dueChannel = 1328684473734139934

# electric bill is due every 2 months
electric_due_months = {1, 3, 5, 7, 9, 11}


@bot.event
async def on_ready():
  print(f"Logged in as {bot.user}")

  checkBillDates.start()
  """
  if channel:
    await channel.send("this channel")
  """


# run once every 24 hours
@tasks.loop(hours=24)
async def checkBillDates():
  now = datetime.datetime.now()

  # check if its the 14th of the month
  if now.day == 14:
    # wifi is every 14th of the month
    await sendWifiDue()

    # electric every 2 months
    if now.month in electric_due_months:
      await sendElectricDue()


# send wifi bill due message
async def sendWifiDue():
  channel = bot.get_channel(dueChannel)
  if channel:
    await channel.send("🛜 **The WiFi bill is due today** 🛜")


async def sendElectricDue():
  """
  Sends the Electric bill due reminder message to the 'due now' channel.
  """
  channel = bot.get_channel(dueChannel)
  if channel:
    await channel.send("⚡ **The Electric bill is due today** ⚡")


@bot.command()
# displays date of when wifi bills are due
async def wifibill(ctx):
  # create embedded message
  embed = discord.Embed(title="🛜 Wifi Bill Dates",
                        description="**📅 Due 14th of every month**",
                        color=discord.Color.orange())

  # send the embed in the same channel where the command was used
  await ctx.send(embed=embed)


@bot.command()
# displays date of when electric bills are due
async def electricbill(ctx):
  # create embedded message
  embed = discord.Embed(
      title="⚡ Electric Bill Dates",
      description="**Every 2 months on the 14th (Estimate)**",
      color=discord.Color.blue())

  embed.add_field(name="📅 14/01/2025", value="\u200b", inline=False)
  embed.add_field(name="📅 14/03/2025", value="\u200b", inline=False)
  embed.add_field(name="📅 14/05/2025", value="\u200b", inline=False)
  embed.add_field(name="📅 14/07/2025", value="\u200b", inline=False)
  embed.add_field(name="📅 14/09/2025", value="\u200b", inline=False)
  embed.add_field(name="📅 14/11/2025", value="\u200b", inline=False)

  # send the embed in the same channel where the command was used
  await ctx.send(embed=embed)


# run bot with token
token = os.environ['TOKEN']
bot.run(token)
