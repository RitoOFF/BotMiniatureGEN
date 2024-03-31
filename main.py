import discord
import fade
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import json

with open('config.json', 'r') as f:
    config = json.load(f)

bot = commands.Bot(command_prefix=config['prefix'], intents=discord.Intents.all())
bot.size = {}
bot.image_url = {}
bot.title = {}
bot.size_title = {}
bot.position = {}
bot.font = {}


class SizeButton(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="1920x1080", style=discord.ButtonStyle.blurple)    
    async def first(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message("```Send your image: ```")
        bot.size[interaction.user.id] = (1920, 1080)
        image_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user and message.attachments)
        bot.image_url[interaction.user.id] = image_msg.attachments[0].url

        await interaction.channel.send("```Send your title: ```")
        title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.title[interaction.user.id] = title_msg.content

        await interaction.channel.send("```Send the size of text: ```")
        size_title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.size_title[interaction.user.id] = size_title_msg.content
 
        file_1 = discord.File("font/1_font.png", filename="1_font.png")
        file_2 = discord.File("font/2_font.png", filename="2_font.png")
        file_3 = discord.File("font/3_font.png", filename="3_font.png")
        
   
        await interaction.channel.send(file=file_1)
        await interaction.channel.send(file=file_2)
        await interaction.channel.send(file=file_3, view=FontButton())
        

class FontButton(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="Something", style=discord.ButtonStyle.blurple)    
    async def font_1(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        font_path = "font/1_font.ttf"
        bot.font[interaction.user.id] = font_path
        await interaction.channel.send("```What position you choose ?```", view=PositionButton()) 
    @discord.ui.button(label="Demon Panic", style=discord.ButtonStyle.blurple)    
    async def font_2(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        font_path = "font/2_font.oft"
        bot.font[interaction.user.id] = font_path   
        await interaction.channel.send("```What position you choose ?```", view=PositionButton()) 
    @discord.ui.button(label="Minecraft", style=discord.ButtonStyle.blurple)    
    async def font_3(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        font_path = "font/3_font.ttf"
        bot.font[interaction.user.id] = font_path 
        await interaction.channel.send("```What position you choose ?```", view=PositionButton())        


class PositionButton(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    async def send_confirmation_message(self, interaction: discord.Interaction, position: str) -> None:
        await interaction.response.send_message(f"```The position is set on {position}```")

    async def send_create_miniature(self, interaction: discord.Interaction, position: str) -> None:
        bot.position[interaction.user.id] = position
        await create_miniature(
            interaction,
            bot.image_url[interaction.user.id],
            1920,
            1080,
            bot.title[interaction.user.id],
            bot.position[interaction.user.id],
            bot.size_title[interaction.user.id],
            bot.font[interaction.user.id]
        )

    @discord.ui.button(label="Top Right", style=discord.ButtonStyle.blurple)    
    async def top_right(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self.send_confirmation_message(interaction, "top right")
        await self.send_create_miniature(interaction, "top_right")

    @discord.ui.button(label="Top Left", style=discord.ButtonStyle.blurple)    
    async def top_left(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self.send_confirmation_message(interaction, "top left")
        await self.send_create_miniature(interaction, "top_left")

    @discord.ui.button(label="Top Center", style=discord.ButtonStyle.blurple)    
    async def top_center(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self.send_confirmation_message(interaction, "top center")
        await self.send_create_miniature(interaction, "top_center")

    @discord.ui.button(label="Middle Right", style=discord.ButtonStyle.blurple)    
    async def middle_right(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self.send_confirmation_message(interaction, "middle right")
        await self.send_create_miniature(interaction, "middle_right")

    @discord.ui.button(label="Middle", style=discord.ButtonStyle.blurple)    
    async def middle(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self.send_confirmation_message(interaction, "middle")
        await self.send_create_miniature(interaction, "middle")

    @discord.ui.button(label="Middle Left", style=discord.ButtonStyle.blurple)    
    async def middle_left(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self.send_confirmation_message(interaction, "middle left")
        await self.send_create_miniature(interaction, "middle_left")

    @discord.ui.button(label="Bottom Right", style=discord.ButtonStyle.blurple)    
    async def bottom_right(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self.send_confirmation_message(interaction, "bottom right")
        await self.send_create_miniature(interaction, "bottom_right")

    @discord.ui.button(label="Bottom Center", style=discord.ButtonStyle.blurple)    
    async def bottom_center(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self.send_confirmation_message(interaction, "bottom center")
        await self.send_create_miniature(interaction, "bottom_center")

    @discord.ui.button(label="Bottom Left", style=discord.ButtonStyle.blurple)    
    async def bottom_left(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self.send_confirmation_message(interaction, "bottom left")
        await self.send_create_miniature(interaction, "bottom_left")

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
    await ctx.send("```What size you choose ?```",view=SizeButton())

async def create_miniature(interaction, image_url, width, height, title, position, titlesize, font):
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    resized_image = image.resize((width, height))

    draw = ImageDraw.Draw(resized_image)
    font = ImageFont.truetype(font, size=int(titlesize))
    text_bbox = draw.textbbox((0, 0), title, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    if position == "top_left":
        position_x = 0
        position_y = 0
    elif position == "top_center":
        position_x = (width - text_width) // 2
        position_y = 0
    elif position == "top_right":
        position_x = width - text_width
        position_y = 0
    elif position == "middle_left":
        position_x = 0
        position_y = (height - text_height) // 2
    elif position == "middle":
        position_x = (width - text_width) // 2
        position_y = (height - text_height) // 2
    elif position == "middle_right":
        position_x = width - text_width
        position_y = (height - text_height) // 2
    elif position == "bottom_left":
        position_x = 0
        position_y = height - text_height
    elif position == "bottom_center":
        position_x = (width - text_width) // 2
        position_y = height - text_height
    elif position == "bottom_right":
        position_x = width - text_width
        position_y = height - text_height

    draw.text((position_x, position_y), title, fill=(255, 255, 255), font=font)

    with BytesIO() as img_bytes:
        resized_image.save(img_bytes, format="PNG")
        img_bytes.seek(0)
        file = discord.File(img_bytes, filename="miniature.png")

    embed = discord.Embed(title="Result :", color=0x6359FF)
    embed.set_image(url="attachment://miniature.png")

    channel = interaction.channel
    await channel.send(file=file, embed=embed)

bot.run(config['token'])