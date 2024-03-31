import discord
import fade
from discord.ext import commands
from PIL import Image
import requests
from io import BytesIO
import json

with open('config.json', 'r') as f:
    config = json.load(f)

bot = commands.Bot(command_prefix=config['prefix'], intents=discord.Intents.all())
bot.size = {}

@bot.event
async def on_ready():
    banner = """
                                             
          ███▄ ▄███▓ ██▓ ███▄    █  ██▓ ▄▄▄     ▄▄▄█████▓ █    ██  ██▀███  ▓█████      ▄████ ▓█████  ███▄    █ 
         ▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▓██▒▒████▄   ▓  ██▒ ▓▒ ██  ▓██▒▓██ ▒ ██▒▓█   ▀     ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
         ▓██    ▓██░▒██▒▓██  ▀█ ██▒▒██▒▒██  ▀█▄ ▒ ▓██░ ▒░▓██  ▒██░▓██ ░▄█ ▒▒███      ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
         ▒██    ▒██ ░██░▓██▒  ▐▌██▒░██░░██▄▄▄▄██░ ▓██▓ ░ ▓▓█  ░██░▒██▀▀█▄  ▒▓█  ▄    ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
         ▒██▒   ░██▒░██░▒██░   ▓██░░██░ ▓█   ▓██▒ ▒██▒ ░ ▒▒█████▓ ░██▓ ▒██▒░▒████▒   ░▒▓███▀▒░▒████▒▒██░   ▓██░
         ░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░▓   ▒▒   ▓▒█░ ▒ ░░   ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░░ ▒░ ░    ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
         ░  ░      ░ ▒ ░░ ░░   ░ ▒░ ▒ ░  ▒   ▒▒ ░   ░    ░░▒░ ░ ░   ░▒ ░ ▒░ ░ ░  ░     ░   ░  ░ ░  ░░ ░░   ░ ▒░
         ░      ░    ▒ ░   ░   ░ ░  ▒ ░  ░   ▒    ░       ░░░ ░ ░   ░░   ░    ░      ░ ░   ░    ░      ░   ░ ░ 
                ░    ░           ░  ░        ░  ░           ░        ░        ░  ░         ░    ░  ░         ░                              
                                                                                                 
                                          ╔═════════════════════════╗        
                                          ║     dsc.gg/nitromc      ║   
                                          ╚═════════════════════════╩
  -> By: ritooff
  -> Github: https://github.com/RitoOFF
    """
    await bot.tree.sync()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Miniature Generator"), status=discord.Status.do_not_disturb)

    faded_banner = fade.purplepink(banner)
    print(faded_banner)

@bot.command(name="miniature", description="Allows you to generate your thumbnail")    
async def miniature(ctx):
    await ctx.send("```What size do you want your miniature to be? (width x height)\nExample: 500x500```")
    size_msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    size_str = size_msg.content.strip()
    try:
        width, height = map(int, size_str.split('x'))
        bot.size[ctx.author.id] = (width, height)
        await ctx.send("```Please send your image :```")
        image_msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.attachments)
        image_url = image_msg.attachments[0].url
        await create_miniature(ctx, image_url, width, height)
    except ValueError:
        await ctx.send("```Please enter a valid size in 'width x height' format\nExample: 500x500```")

async def create_miniature(ctx, image_url, width, height):
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    resized_image = image.resize((width, height))

    with BytesIO() as img_bytes:
        resized_image.save(img_bytes, format="PNG")
        img_bytes.seek(0)
        file = discord.File(img_bytes, filename="miniature.png")

    embed = discord.Embed(title="Result :", color=0x6359FF)
    embed.set_image(url="attachment://miniature.png")

    await ctx.send(file=file, embed=embed)

bot.run(config['token'])
