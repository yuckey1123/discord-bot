import random
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

TOKEN = 'MTAxNjYxMjIxNDE0NjMzNDc1MA.GNHhyK.9nC3ClOneyBGJw4qKIeOIEG86a8ZTW6OYpKTTU'

intents = discord.Intents.all()
# intents.message_content = True
# bot = discord.Client(intents=intents)
# bot = discord.Client(intents=discord.Intents.all())
bot = commands.Bot(command_prefix='#', intents=intents)

slash_client = SlashCommand(bot)

ults = [
    "消えてもらおうか！！！",
    "まだ終わりじゃないわ！！！",
    "見てなよ！！！",
    "俺がやる！！！",
    "俺はハンターだ！！！",
    "邪魔をしないで！！！",
    "さあ行こう！！！",
    "よし行くぞ！！！",
    "カウントダウン開始！！！",
    "パーティタイム！！！",
    "狩りの時間よ！！！",
    "逃がしはしない！！！",
    "上から来るぞ！！！",
    "アルティメットはまだ！"
    ]

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.__version__)
    print('------')
    await bot.change_presence(activity=discord.Game("意識の高い人生"))

@bot.event
async def on_message(message):
    if message.content.startswith("おはよう"):
        if bot.user != message.author:
            m = message.author.name + "さん！おはようございます！\nよい一日を！"
            await message.channel.send(m)
    if message.content.startswith("おやすみ"):
        if bot.user != message.author:
            m = message.author.name + "さん！おやすみなさい！\nまた明日！"
            await message.channel.send(m)
    if message.content.startswith("/ult"):
        if bot.user != message.author:
            m = ults[random.randint(0, len(ults))]
            await message.channel.send(m)

bot.run(TOKEN)
