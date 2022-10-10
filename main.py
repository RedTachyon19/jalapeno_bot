import discord
from discord.ext import commands
from discord import guild

from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import datetime
import os
import keep_alive

bot = commands.Bot(command_prefix="!j ")
slash = SlashCommand(bot, sync_commands=True)
bot.remove_command('help')

snipe_message_author = {}
snipe_message_content = {}
#snipe_message_file = {}


@bot.event
async def on_message_delete(message):

    ## the date and time need fixing to correspond to the corect time zones

    print(datetime.date.today())
    print(message.author)
    print(message.content)
    print()

    snipe_message_author[message.channel.id] = message.author
    snipe_message_content[message.channel.id] = message.content

    print(message.content)

    f = open("logs.txt", "a")
    f.write(message.content + "\n")
    f.write(str(message.author) + "\n")
    f.write(str(message.created_at) + "\n" + "\n")
    f.close()


@slash.slash(name='ping', description='replies with a pong', guild_ids=[])
async def ping(ctx: SlashContext):
    await ctx.send('pong')


#snipe command, press /snipe to reveal the latest deleted post
#@bot.command(name = 'snipe')
@slash.slash(name='snipe',
             description='restores most recently deleted messages',
             guild_ids=[])
async def snipe(ctx: SlashContext):
    channel = ctx.channel

    try:
        #This piece of code is run if the bot finds anything in the dictionary
        em = discord.Embed(name=f"Last deleted message in #{channel.name}",
                           description=snipe_message_content[channel.id])
        em.set_footer(
            text=f"This message was sent by {snipe_message_author[channel.id]}"
        )
        await ctx.send(embed=em)
    except:
        #This piece of code is run if the bot doesn't find anything in the dictionary
        await ctx.send(
            f"There are no recently deleted messages in #{channel.name}")


## purges chat of previous send messages based on certain amoung
@slash.slash(name = 'purge',
  description='purges the last sent messages',
  guild_ids=[901148844060995604, 821524088492392459, 974480494110584892])
@commands.has_role('Moderators')
async def purge(ctx, amount: int):
    await ctx.channel.purge(limit = amount)
    await ctx.send(str(amount) + ' messages purged by ' + ctx.author.mention)

@slash.slash(name = 'giverole',
  description = 'gives a member a specific role',
  guild_ids = [901148844060995604, 821524088492392459, 974480494110584892])
@commands.has_role('Moderators')
async def giverole(ctx, member: discord.Member, role: discord.Role):
  await ctx.send(ctx.author.mention + ' has given ' + member.mention + ' the role ' + str(role))
  await member.add_roles(role)

@slash.slash(name='ban',
  description = 'bans a certain user',
  guild_ids=[901148844060995604, 821524088492392459, 974480494110584892])
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
  await ctx.send(ctx.author.mention + ' has banned ' + member.mention)  
  await member.ban(reason = reason)
    
@slash.slash(name='whois',
  description = 'gives you information about a certain member',
  guild_ids=[901148844060995604, 821524088492392459, 974480494110584892])

async def whois(ctx, member : discord.Member):
  em = discord.Embed(
    title = "Member Info", 
    url = "https://discord.gg/VkF3z8WmEN", 
    description = "here is the information regarding a certain member", 
    color = 0x000000)

  em.add_field(name = "Member Name", value = member, inline = False)
  em.add_field(name = "Member ID", value = member.id, inline = False)
  em.add_field(name = "Time of Request", value = datetime.date.today(), inline = False)
  em.set_thumbnail(url = member.avatar_url)
  em.set_footer(icon_url = ctx.author.avatar_url, text = 'informtion requested by ' + str(ctx.author))
  await ctx.send(embed = em)

@slash.slash(name='invite',
  description='sends you an invite of this server',
  guild_ids=[901148844060995604])
async def invite(ctx):
    await ctx.send('https://discord.gg/VkF3z8WmEN')
  
keep_alive.keep_alive()
jalapeño_TOKEN = os.environ['jalapeno_TOKEN']
bot.run(jalapeño_TOKEN)
