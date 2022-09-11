import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(discord.__version__)
    print('------')
    await client.change_presence(activity=discord.Game(name="よりよい人生"))


@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)
    # 「おやすみ」で始まるか調べる
    if message.content.startswith("おやすみ"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おやすみなさい" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)

client.run(
    'MTAxNjYxMjIxNDE0NjMzNDc1MA.GSkv11.hfxjTBP09ObTzsVOKcfjRPrW3REyTI2lzUOSIM')
