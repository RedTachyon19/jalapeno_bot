import discord
from discord import default_permissions
import os
import datetime

bot = discord.Bot(
  intents = discord.Intents.all()
)

@bot.event
async def on_ready():
  print("jalapeno bot is online")

snipe_message_author = {}
snipe_message_content = {}

@bot.event
async def on_message_delete(message):
  ## the date and time need fixing to correspond to the corect time zones

  print(datetime.date.today())
  print(message.author)
  print(message.content)
  print()

  snipe_message_author[message.channel.id] = message.author
  snipe_message_content[message.channel.id] = message.content
  
  f = open("logs_2.txt", "a")
  f.write(message.content + "\n")
  f.write(str(message.author) + "\n")
  f.write(str(message.created_at) + "\n" + "\n")
  f.close()


  ## ghost ping detetor
  ghost_ping_mentions = ['@everyone', '@Moderators', '@&901871414355828836', '@RedTachyon19']
  for word in ghost_ping_mentions:
    if word in message.content:  
      ghost_ping_alert = discord.Embed(
        title = "Ghost-Ping Detected!", 
        url = "https://discord.gg/VkF3z8WmEN", 
        description = f"Date: {datetime.date.today()}", 
        color = 0x9f38f3)
      
      ghost_ping_alert.add_field(name = "Message Content", value = message.content, inline = False) 
      ghost_ping_alert.set_thumbnail(url = "https://media.tenor.com/uSK7LpYPV8MAAAAi/bot-antighostping.gif")
      ghost_ping_alert.set_footer(icon_url = message.author.avatar.url, text = f"Message Author: {message.author}")
      await message.channel.send(embed = ghost_ping_alert)

#snipe command
@bot.command(description = "restores the most recently deleted message")
async def snipe(ctx):
  
  try:
    embed = discord.Embed(
      name = f"Last deleted message in #{ctx.channel.name}", 
      description = snipe_message_content[ctx.channel.id]
    )
    embed.set_footer(
      text = f"This message was sent by {snipe_message_author[ctx.channel.id]}"
    )
    await ctx.respond(embed = embed)
    
  except:
    await ctx.respond(
      f"There are no recently deleted messages in #{ctx.channel.name}"
    )

#ping & latency command
@bot.command(description = "replies with pong!")
async def ping(ctx):  
  await ctx.respond(f"Pong! Latency is {bot.latency}")

#invite command
@bot.command(description='sends you an invite of this server')
async def invite(ctx):
  await ctx.respond("https://discord.gg/VkF3z8WmEN")

#who is command
@bot.command(description = 'gives you information about a certain member')
async def whois(ctx, *, member: discord.Member):

  embed = discord.Embed(
    title = "Member Info", 
    url = "https://discord.gg/VkF3z8WmEN", 
    description = f"Here is more information about {member.display_name}",
    color = 0x000000)

  embed.add_field(name = "Member Name", value = member, inline = False)
  embed.add_field(name = "Member ID", value = member.id, inline = False)
  embed.add_field(name = "Server Join Date", value = member.joined_at, inline = False)
  embed.add_field(name = "Date of Request", value = datetime.date.today(), inline = False)
  embed.set_thumbnail(url = member.display_avatar.url)
  embed.set_footer(icon_url = ctx.author.display_avatar.url, text = f"Request by {ctx.author}")
  await ctx.respond(embed = embed)

#give role command
@bot.command(
  description = 'gives a member a specific role'
)
@default_permissions(manage_roles = True)

async def giverole(ctx, member: discord.Member, role: discord.Role):
  await ctx.respond(ctx.author.mention + ' has given ' + member.mention + ' the role ' + str(role))
  await member.add_roles(role)

#purge command
@bot.command(
  name = 'purge',
  description='purges the last sent messages',
)
@default_permissions(manage_messages = True)
async def purge(ctx, amount: int):
    await ctx.channel.purge(limit = amount)
    await ctx.respond(str(amount) + ' messages purged by ' + ctx.author.mention)

jalapeno_TOKEN = os.environ['jalapeno_TOKEN']
bot.run(jalapeno_TOKEN)
