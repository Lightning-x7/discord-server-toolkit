print("Discord Server Toolkit is starting!")
print("My first GitHub project!")
# ---------------------------------------
import discord
from discord.ext import commands
import os

# ==============================

# DISCORD SERVER TOOLKIT

# A multipurpose Discord utility bot

# ==============================

BOT_NAME = "Discord Server Toolkit"
BOT_VERSION = "0.1.0"
EMBED_COLOR = 0xFF7F50  # Coral

Configure bot permissions and intents

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
command_prefix="!",
intents=intents,
help_command=None
)

# ==============================

# EVENTS

# ==============================

@bot.event
async def on_ready():
print("=" * 35)
print(f"{BOT_NAME} is online!")
print(f"Logged in as: {bot.user}")
print(f"Bot ID: {bot.user.id}")
print(f"Version: {BOT_VERSION}")
print("=" * 35)

# ==============================

# GENERAL COMMANDS

# ==============================

@bot.command()
async def ping(ctx):
"""Check the bot's latency."""
latency = round(bot.latency * 1000)

embed = discord.Embed(
    title="🏓 Pong!",
    description=f"Latency: `{latency}ms`",
    color=EMBED_COLOR
)

await ctx.send(embed=embed)

@bot.command()
async def botinfo(ctx):
"""Display information about the bot."""
embed = discord.Embed(
title=f"🤖 {BOT_NAME}",
description="A multipurpose Discord server utility bot.",
color=EMBED_COLOR
)

embed.add_field(name="Version", value=BOT_VERSION)
embed.add_field(name="Library", value="discord.py")
embed.add_field(name="Prefix", value="`!`")

embed.set_footer(text="Discord Server Toolkit")

await ctx.send(embed=embed)

@bot.command()
async def serverinfo(ctx):
"""Display information about the current server."""
guild = ctx.guild

if guild is None:
    await ctx.send("This command can only be used in a server.")
    return

embed = discord.Embed(
    title=f"📊 {guild.name}",
    color=EMBED_COLOR
)

embed.add_field(
    name="Members",
    value=str(guild.member_count or "Unknown"),
    inline=True
)

embed.add_field(
    name="Channels",
    value=str(len(guild.channels)),
    inline=True
)

embed.add_field(
    name="Roles",
    value=str(len(guild.roles)),
    inline=True
)

if guild.icon:
    embed.set_thumbnail(url=guild.icon.url)

embed.set_footer(text=f"Server ID: {guild.id}")

await ctx.send(embed=embed)

@bot.command()
async def userinfo(ctx, member: discord.Member = None):
"""Display information about a server member."""
member = member or ctx.author

embed = discord.Embed(
    title=f"👤 {member}",
    color=EMBED_COLOR
)

embed.set_thumbnail(url=member.display_avatar.url)

embed.add_field(
    name="User ID",
    value=str(member.id),
    inline=False
)

embed.add_field(
    name="Account Created",
    value=discord.utils.format_dt(member.created_at, style="D"),
    inline=False
)

if member.joined_at:
    embed.add_field(
        name="Joined Server",
        value=discord.utils.format_dt(member.joined_at, style="D"),
        inline=False
    )

await ctx.send(embed=embed)

# ==============================

# HELP COMMAND

# ==============================

@bot.command()
async def help(ctx):
"""Display available commands."""
embed = discord.Embed(
title="📚 Discord Server Toolkit",
description="Here are the currently available commands:",
color=EMBED_COLOR
)

embed.add_field(
    name="🏓 General",
    value="`!ping` — Check bot latency\n"
          "`!botinfo` — View bot information\n"
          "`!serverinfo` — View server information\n"
          "`!userinfo [member]` — View member information",
    inline=False
)

embed.set_footer(text=f"Version {BOT_VERSION}")

await ctx.send(embed=embed)

# ==============================

# STARTUP

# ==============================

if name == "main":
token = os.getenv("DISCORD_BOT_TOKEN")

if not token:
    raise RuntimeError(
        "Missing DISCORD_BOT_TOKEN environment variable!"
    )

bot.run(token)
