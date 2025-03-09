import discord
from discord.ext import commands
import requests
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# استبدل هذا بمفتاح API الخاص بك
API_KEY = os.getenv('45c7374414674fbb9dc3115c003c6 077')
TEAM_ID = "529"  # معرف فريق برشلونة في API-Football

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def matches(ctx):
    url = f"https://api.football-data.org/v4/teams/{TEAM_ID}/matches?status=SCHEDULED"
    headers = {
        "X-Auth-Token": API_KEY
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    if data["matches"]:
        matches_info = ""
        for match in data["matches"]:
            home_team = match["homeTeam"]["name"]
            away_team = match["awayTeam"]["name"]
            date = match["utcDate"]
            matches_info += f"**{home_team} vs {away_team}** - {date}\n"
        await ctx.send(f"المباريات القادمة لبرشلونة:\n{matches_info}")
    else:
        await ctx.send("لا توجد مباريات قادمة.")

@bot.command()
async def standings(ctx):
    url = f"https://api.football-data.org/v4/competitions/PD/standings"
    headers = {
        "X-Auth-Token": API_KEY
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    if data["standings"]:
        standings_info = ""
        for team in data["standings"][0]["table"]:
            rank = team["position"]
            name = team["team"]["name"]
            points = team["points"]
            standings_info += f"{rank}. {name} - {points} نقطة\n"
        await ctx.send(f"ترتيب الدوري الإسباني:\n{standings_info}")
    else:
        await ctx.send("لا يمكن الحصول على الترتيب حاليًا.")

@bot.command()
async def squad(ctx):
    url = f"https://api.football-data.org/v4/teams/{TEAM_ID}"
    headers = {
        "X-Auth-Token": API_KEY
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    if data["squad"]:
        squad_info = ""
        for player in data["squad"]:
            name = player["name"]
            position = player["position"]
            squad_info += f"{name} - {position}\n"
        await ctx.send(f"تشكيلة برشلونة:\n{squad_info}")
    else:
        await ctx.send("لا يمكن الحصول على التشكيلة حاليًا.")

# استبدل 'YOUR_BOT_TOKEN' بالتوكن الخاص بك
bot.run(os.getenv('MTM0ODMyMjk2ODg0NDg5ODMwNA.GNhgbK.Z60uswtnssqy35yMsJMLSCMh89AlysZuhzkpTo'))
