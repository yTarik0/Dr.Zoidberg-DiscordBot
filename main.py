# DiscordBot 2023 "Zoidberg" by yTarik0 and 1momo7
# Author: @yTarik0
# Version @v1.1 {BETA}
# Date: @06.02.2023
# Bot:  @Dr.Zoidberg


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
client = commands.Bot(command_prefix='/', intents=intents, application_id="Your_Application_ID")

# blacklisted words
blacklist = [
    "anus",
    "anal", "biatch", "bitch",
    "cum", "cock",
    "dick", "dick",
    "faggot", "fatass",
    "gay" "goyim",
    "gypsy", "gipsy",
    "homo",
    "hurensohn",
    "hure",
    "lesbo",
    "lesbe",
    "negress",
    "negro",
    "nig",
    "nig-nog",
    "nigga",
    "nigger",
    "nigg4",
    "neger",
    "nigguh",
    "neger",
    "nutte",
    "nuttensohn",
    "penis",
    "prostitute",
    "pussie",
    "pussy",
    "schlampe",
    "slut",
    "schwuchtel",
    "schwanz",
    "tits",
    "titt",
    "whore"]


@client.event
async def on_ready():
    pclient.loop.create_task(status_task())
    print("ボットはオンラインです, online")
    synced = await client.tree.sync()
    print("Slash CMDs Synced " + str(len(synced)) + " Commands")


# <------Joining Member------->
@client.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined the Server")
    channel = client.get_channel("Your-Channel-Id")
    server = member.guild
    embed = discord.Embed(title=f"**Welcome {member.name}**👋" ,
                          color=discord.Color.blue())
    embed.add_field(name="📚**Rules**",value="Please make sure that you read the rules")
    embed.add_field(name="❓**Support**",value="If you have any questions open a ticket ")
    embed.add_field(name="🍿**Enjoy**",value=f"Have Fun and enjoy chatting and talking on the Server **{server.name}**")
    embed.thumbnail(url=member.avatar.url)
    embed.set_footer(text="⭐  • Dr.Zoidberg | Systems")
    await channel.send(embed=embed)


@client.event
async def on_member_remove(member):
    channel = client.get_channel("Your-Channel-Id")
    server = member.guild
    print("Recognised that a member called " + member.name + " left")
    embed=discord.Embed(title=f"**{member.name}  just left the Server {server.name}👋**",
                        color=discord.Color.red())
    embed.set_footer(text="⭐  • Dr.Zoidberg | Systems")
    embed.thumbnail(url=member.avatar.url)
    await channel.send(embed=embed)


@client.event
async def on_message(message):



    # <-------Direct Message Awnser ----- coming soon--------->

    # guild = message.guild
    # if not guild in message.content:
    # embed = discord.Embed(title="**I'm Sorry I can't handle Direct Messages**", color=discord.Colour.random())
    # embed.add_field(name="🔰**github**", value="http://github.comytarik0\r\nhttp://github.com/1momo7")
    # embed.add_field(name="❓**No Idea?**", value=".help")
    # await message.channel.send(embed=embed)

    # <---------automatic mute using blacklisted word--------->
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
                embed.set_footer(text="⭐ • Dr.Zoidberg | Systems")
                await message.channel.send(embed=embed)



# <---------ban command---------->
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
        embed.set_footer(text="⭐ • Dr.Zoidberg | Systems")
        await interaction.response.send_message(embed=embed)

    else:
        embed = discord.Embed(title="**You don't have the permission for that Command**", color=discord.Colour.random())
        embed.set_footer(text="⭐ • Dr.Zoidberg | Systems")
        await interaction.response.send_message(embed=embed, ephemeral=True)


# <------kick command----->
@client.tree.command(name="kick", description="kick a user")
async def kick(interaction: discord.Interaction, user: discord.User, reason: str = None):
    channel = interaction.channel
    server = interaction.guild
    if interaction.user.guild_permissions.kick_members:
        await user.kick(reason=reason)
        embed = discord.Embed(title=f"**{user.name} was kicked by {interaction.user.name}**",
                              color=discord.Colour.random())
        embed.add_field(name="📆**Date **", value=interaction.created_at.strftime("%Y-%m-%d"))
        embed.add_field(name="🆔**User ID**", value=user.id)
        embed.add_field(name="💬**Reason**", value=reason)
        embed.set_thumbnail(url=server.icon.url)
        embed.set_footer(text="⭐ • Dr.Zoidberg | Systems")
        await interaction.response.send_message(embed=embed)

    else:
        embed = discord.Embed(title="**You don't have the permission for that Command**",
                              color=discord.Colour.random())
        embed.set_footer(text="⭐ • Dr.Zoidberg | Systems")
        await interaction.response.send_message(embed=embed, ephemeral=True)


# <------help command---------->
@client.tree.command(name="help", description="help command")
async def help(interaction: discord.Interaction):
    embed = discord.Embed(title="**Command-List for Zoidberg-Bot**", color=discord.Colour.random())
    embed.add_field(name="🌐**help**", value="list of all commands")
    embed.add_field(name="🎭**avatar**", value="shows a users avatar")
    embed.add_field(name="ℹ️**serverinfo**", value="gives info about the server")
    embed.add_field(name="⚙️**admin**", value="list all admin commands")
    embed.add_field(name="ℹ️**userainfo**", value="gives information about an user")
    embed.add_field(name="🔰**roles**", value="list all server roles"
    embed.set_footer(text="⭐ • Dr.Zoidberg | Systems")
    await interaction.response.send_message(embed=embed)



# <---------serverinfo command---------->
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
    embed.set_footer(text="⭐ • Dr.Zoidberg | Systems")
    await interaction.response.send_message(embed=embed)


# <---------admin info command--------->
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
        embed.set_footer(text="⭐ • Dr.Zoidberg | Systems")
        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title="**You don't have the permission for that Command**",
                              color=discord.Colour.random())
        embed.set_footer(text="⭐ • Dr.Zoidberg | Systems")
        await interaction.response.send_message(embed=embed)


# <----------basic clear command---------->
@client.tree.command(name="clear", description="clears chat messages")
async def clear(interaction: discord.Interaction, amount: int = 0):
    channel = interaction.channel
    if interaction.user.guild_permissions.manage_messages:
        try:
            await channel.purge(limit=amount + 1)
            embed = discord.Embed(title=f"{interaction.user.name} cleared {amount} Messages",
                                  color=discord.Colour.random())
            embed.add_field(name="🆔 **User ID**", value=interaction.user.id)
            embed.add_field(name="📆**Cleared Messages At**", value=interaction.created_at.strftime("%Y-%m-%d %H:%M:%S"))
            embed.set_footer(text="⭐ • Dr.Zoidberg | Systems")
            await channel.send(embed=embed)
        except ValueError:
            embed = discord.Embed(title="**Please enter a valid number of messages to delete.**",
                                  color=discord.Colour.random())
            embed.set_footer(text="⭐ • Dr.Zoidberg | Systems")
            await interaction.response.send_message(embed=embed, ephemeral=True)

    else:
        embed = discord.Embed(title="**You don't have the permission for that Command**",
                              color=discord.Colour.random())
        embed.set_footer(text="⭐ • Dr.Zoidberg | Systems")
        await interaction.response.send_message(embed=embed, ephemeral=True)


# <------role-command-list-all-roles-------->
@client.tree.command(name="roles", description="lists you all roles")
async def roles(interaction: discord.Interaction):
    server = interaction.guild
    rolelist = []
    for role in server.roles:
        if role.name != "@everyone":
            rolelist.append(role.mention)
    b = ",".join(rolelist)

    embed = discord.Embed(title="**All Discord Roles:**",
                          color=discord.Colour.random())
    embed.add_field(name=f"**🔰Roles:**({len(rolelist)})", value="".join([b]))
    embed.set_footer(text="⭐ • Dr.Zoidberg | Systems")
    await interaction.response.send_message(embed=embed)

# <-------unmute-command---------->
@client.tree.command(name="unmute", description="unmutes a user from the chat")
async def unmute_user(interaction: discord.Interaction, user: discord.User, reason: str = None):
    channel = interaction.channel
    if interaction.user.guild_permissions.manage_messages:
        await channel.set_permissions(user, send_messages=True)
        embed = discord.Embed(
            title=f"**{user.name} has been unmuted by {interaction.user.name}**",
            color=discord.Colour.random())
        embed.add_field(name="🆔**User ID**", value=user.id)
        embed.add_field(name="💬**Reason**", value=reason)
        embed.add_field(name="📆**Unmuted on**", value=interaction.created_at.strftime("%Y-%m-%d %H:%M:%S"))
        embed.set_footer(text="⭐  • Dr.Zoidberg | Systems")
        await interaction.response.send_message(embed=embed)

# <-------mute-command------->
@client.tree.command(name="mute", description="mutes a user from the chat")
async def mute_user(interaction: discord.Interaction, user: discord.User, reason: str = None, time: int = 0):
    channel = interaction.channel
    if interaction.user.guild_permissions.manage_messages:
        await channel.set_permissions(user, send_messages=False)
        embed = discord.Embed(
            title=f"**{user.name} has been muted by {interaction.user.name}**",
            color=discord.Colour.red())
        embed.add_field(name="🆔**User ID**", value=user.id)
        embed.add_field(name="💬**Reason**", value=reason)
        embed.add_field(name="📆**Muted on**", value=interaction.created_at.strftime("%Y-%m-%d %H:%M:%S"))
        embed.add_field(name="🕒**Muted for**", value=f"{time} seconds")
        embed.set_footer(text="⭐  • Dr.Zoidberg | Systems")
        await interaction.response.defer()
        await interaction.followup.send(embed=embed)
        await asyncio.sleep(time)
        await channel.set_permissions(user, send_messages=True)

#<------info command------>
# for getting userinfo

@client.tree.command(name="userinfo", description="gives information about a user")
async def userinfo(interaction: discord.Interaction, user: discord.User):

    rolelist = []
    for role in user.roles:
        if role.name != "@everyone":
            rolelist.append(role.mention)
    b = ",".join(rolelist)

    embed = discord.Embed(title=f"**User Info about {user}**",
                          color=discord.Colour.purple())
    embed.add_field(name="🆔**User ID**", value=user.id)
    embed.add_field(name="📆**Created at**",value=user.created_at.strftime("%Y-%m-%d"))
    embed.add_field(name="🕗**Joined at**", value=user.joined_at.strftime("%Y-%m-%d"))
    embed.add_field(name=f"🔰**Role:** ({len(rolelist)})",value="".join([b]))
    embed.add_field(name=f"🎖**Top-Role**",value=user.top_role.mention)
    embed.add_field(name=f"🏆**Booster**",value=f'{"Yes" if user.premium_since else "No"}')
    embed.add_field(name="🤖**Bot**",value=f"{'Yes' if user.bot else 'No'}")
    embed.set_thumbnail(url=user.avatar.url)
    embed.set_footer(text="⭐  • Dr.Zoidberg | Systems")
    await interaction.response.send_message(embed=embed)


#<-------Avatar-Command------------>
# shows a discord users avatar  as "big" format in the chat
@client.tree.command(name="avatar", description="prints the users avatar")
async def avatar(interaction: discord.Interaction, user: discord.User):
    userAvatarUrl = user.avatar.url
    embed = discord.Embed(title=f"**{user}s Avatar:**",color=discord.Colour.yellow()).set_image(url=user.avatar.url)
    embed.set_footer(text="⭐  • Dr.Zoidberg | Systems")
    await interaction.response.send_message(embed=embed)
                    
# <-----Change Status------->
@client.event
async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('/help'), status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('github.com/yTarik0'), status=discord.Status.online)
        await asyncio.sleep(3)

client.run("Your-DiscordBot-Token")
