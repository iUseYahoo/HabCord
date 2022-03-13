import pyautogui
import discord
from discord.ext import commands

BOT_TOKEN = "" # <<< enter bot token here << IT IS NEEDED FOR THE BOT TO RUN
PREFIX = "" # <<< enter your prefix here <<<

client = commands.Bot(command_prefix=PREFIX)

hab_msg_box_location = 555,555 # Use the source forge auto clicker
# click set location and it will tell you the location of where you clicked
# then enter it above

def sendmsg(msg):
  pyautogui.click(hab_msg_box_location)
  pyautogui.write(msg)
  pyautogui.press("enter")
  

@client.event
async def on_ready():
  print("\n== BOT IS ONLINE==\n")
  
@client.command
async def msg(ctx, *, msg):
  sendmsg(msg)
  await ctx.reply(f"User: <@{ctx.author.id}>\nMessage: `{msg}`")

client.run(BOT_TOKEN)
