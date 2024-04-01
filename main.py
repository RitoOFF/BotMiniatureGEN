import discord
import fade
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import json
import asyncio
import random

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

bot = commands.Bot(command_prefix=config['prefix'], intents=discord.Intents.all())
bot.size = {}
bot.image_url = {}
bot.title = {}
bot.size_title = {}
bot.position = {}
bot.font = {}
bot.type = {}
bot.element = {}

created_miniature_channels = set()

class ElementButton(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="1", style=discord.ButtonStyle.blurple)    
    async def first(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        bot.element[interaction.user.id] = "element/fortnite/1.png"
        await interaction.response.send_message("```Send your title: ```")
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
    @discord.ui.button(label="2", style=discord.ButtonStyle.blurple)    
    async def second(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        bot.element[interaction.user.id] = "element/fortnite/2.png"
        await interaction.response.send_message("```Send your title: ```")
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
    @discord.ui.button(label="3", style=discord.ButtonStyle.blurple)    
    async def their(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        bot.element[interaction.user.id] = "element/fortnite/3.png"
        await interaction.response.send_message("```Send your title: ```")
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
    @discord.ui.button(label="4", style=discord.ButtonStyle.blurple)    
    async def foor(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        bot.element[interaction.user.id] = "element/fortnite/4.png"
        await interaction.response.send_message("```Send your title: ```")
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
    @discord.ui.button(label="5", style=discord.ButtonStyle.blurple)    
    async def five(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        bot.element[interaction.user.id] = "element/fortnite/5.png"
        await interaction.response.send_message("```Send your title: ```")
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
    @discord.ui.button(label="6", style=discord.ButtonStyle.blurple)    
    async def six(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        bot.element[interaction.user.id] = "element/fortnite/6.png"
        await interaction.response.send_message("```Send your title: ```")
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
    @discord.ui.button(label="7", style=discord.ButtonStyle.blurple)    
    async def seven(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        bot.element[interaction.user.id] = "element/fortnite/7.png"
        await interaction.response.send_message("```Send your title: ```")
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
    @discord.ui.button(label="8", style=discord.ButtonStyle.blurple)    
    async def eight(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        bot.element[interaction.user.id] = "element/fortnite/8.png"
        await interaction.response.send_message("```Send your title: ```")
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
    @discord.ui.button(label="9", style=discord.ButtonStyle.blurple)    
    async def nine(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        bot.element[interaction.user.id] = "element/fortnite/9.png"
        await interaction.response.send_message("```Send your title: ```")
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

class TypeMiniatureButton(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="Fortnite", style=discord.ButtonStyle.blurple)    
    async def fortnite(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message("```Choose your elements on your miniature: ```")
        bot.type[interaction.user.id] = "fortnite"
 
        file_1 = discord.File("element/fortnite/choose/1.png", filename="1_fortnite.png")
        file_2 = discord.File("element/fortnite/choose/2.png", filename="2_fortnite.png")
        file_3 = discord.File("element/fortnite/choose/3.png", filename="3_fortnite.png")
        file_4 = discord.File("element/fortnite/choose/4.png", filename="4_fortnite.png")
        file_5 = discord.File("element/fortnite/choose/5.png", filename="5_fortnite.png")
        file_6 = discord.File("element/fortnite/choose/6.png", filename="6_fortnite.png")
        file_7 = discord.File("element/fortnite/choose/7.png", filename="7_fortnite.png")
        file_8 = discord.File("element/fortnite/choose/8.png", filename="8_fortnite.png")
        file_9 = discord.File("element/fortnite/choose/9.png", filename="9_fortnite.png")

        await interaction.channel.send(files=[file_1, file_2, file_3, file_4, file_5, file_6, file_7, file_8, file_9], view=ElementButton())
    @discord.ui.button(label="Minecraft", style=discord.ButtonStyle.blurple)    
    async def minecraft(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.channel.send("```Send your title: ```")
        title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.title[interaction.user.id] = title_msg.content

        await interaction.channel.send("```Send the size of text: ```")
        size_title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.size_title[interaction.user.id] = size_title_msg.content
 
        file_1 = discord.File("font/1_font.png", filename="1_font.png")
        file_2 = discord.File("font/2_font.png", filename="2_font.png")
        file_3 = discord.File("font/3_font.png", filename="3_font.png")
    @discord.ui.button(label="Valorant", style=discord.ButtonStyle.blurple)    
    async def valorant(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
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
        
   
        await interaction.channel.send(file=file_1)
        await interaction.channel.send(file=file_2)
        await interaction.channel.send(file=file_3, view=FontButton())    

class SizeButton(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="Miniature", style=discord.ButtonStyle.blurple)    
    async def first(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message("```Send your background: ```")
        bot.size[interaction.user.id] = (1920, 1080)
        image_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user and message.attachments)
        bot.image_url[interaction.user.id] = image_msg.attachments[0].url

        await interaction.channel.send("```Choose the type of miniature```", view=TypeMiniatureButton())
        

class FontButton(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="Something", style=discord.ButtonStyle.blurple)    
    async def font_1(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"```The font is set on Something```")
        font_path = "font/1_font.ttf"
        bot.font[interaction.user.id] = font_path
        await interaction.channel.send("```What position you choose ?```", view=PositionButton()) 
    @discord.ui.button(label="Demon Panic", style=discord.ButtonStyle.blurple)    
    async def font_2(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"```The font is set on Demon Panic ```")
        font_path = "font/2_font.oft"
        bot.font[interaction.user.id] = font_path   
        await interaction.channel.send("```What position you choose ?```", view=PositionButton()) 
    @discord.ui.button(label="Minecraft", style=discord.ButtonStyle.blurple)    
    async def font_3(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"```The font is set on Minecraft```")
        font_path = "font/3_font.ttf"
        bot.font[interaction.user.id] = font_path 
        file = discord.File("img/position.png", filename="position.png")
        await interaction.channel.send("```What position you choose ?```",file=file, view=PositionButton())        


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
            bot.font[interaction.user.id],
            bot.type[interaction.user.id],
            bot.element[interaction.user.id]
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

@bot.event
async def on_raw_reaction_add(payload):
    if payload.member.bot:
        return

    channel = await bot.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)

    if str(payload.emoji) == "🛒":
        category_id = config['category_shop']
        category = bot.get_channel(category_id)

        if category and isinstance(category, discord.CategoryChannel):
            existing_miniatures = sum(1 for channel in category.channels if channel.name.startswith("miniature-"))
            next_miniature_name = f"miniature-{existing_miniatures + 1}"

            guild = bot.get_guild(payload.guild_id)
            owner = await guild.fetch_member(payload.user_id)
            new_channel = await category.create_text_channel(name=next_miniature_name)
            created_miniature_channels.add(owner.id)
            await new_channel.set_permissions(guild.default_role, read_messages=False)
            await new_channel.set_permissions(owner, read_messages=True, send_messages=True)
            await new_channel.send("```What types you choose ?```", view=SizeButton())
            reply_message = await message.reply(f"```A miniature channel has been created!``` {new_channel.mention}")
            await asyncio.sleep(5)
            await reply_message.delete()
        else:
            print("Could not find the specified category.")

@bot.command(name="miniature", description="Allows you to generate your thumbnail")    
async def miniature(ctx):

 
    if ctx.author.id in created_miniature_channels:
        await ctx.send("```You already have an active miniature channel.```")
        return
    
    if ctx.author.id != ctx.guild.owner_id:
        await ctx.send("```Only the server owner can use this command.```")
        return
    message = await ctx.send(config['message'])
    await message.add_reaction("🛒")
    await message.add_reaction("🤝")
    await message.add_reaction("🎯")
    await message.add_reaction("🧷")
    await message.add_reaction("⭐")

async def create_miniature(interaction, image_url, width, height, title, position, titlesize, font, type, element):
    response = requests.get(image_url)
    background_image = Image.open(BytesIO(response.content))

    background_image = background_image.resize((width, height))

    if type == "fortnite":
        overlay_image = Image.open(element)  


        overlay_width, overlay_height = overlay_image.size
        

        if overlay_width > width or overlay_height > height:
            print("L'image d'overlay est trop grande et sera redimensionnée.")
            overlay_image = overlay_image.resize((width, height))


        background_image.paste(overlay_image, (0, 0), overlay_image)

    
    draw = ImageDraw.Draw(background_image)
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
        background_image.save(img_bytes, format="PNG")
        img_bytes.seek(0)
        file = discord.File(img_bytes, filename="DEVDEN-deminiature.png")

    await interaction.channel.send(f"The result for you {interaction.user} : ",file=file)

    category_result_id = config["category_result"]
    category_result_channel = interaction.guild.get_channel(category_result_id)

    if category_result_channel:
        await category_result_channel.send(file=file)
    else:
        print("Could not find the specified result category channel.")

    await asyncio.sleep(30)
    await interaction.channel.delete()
    created_miniature_channels.remove(interaction.user.id)

bot.run(config['token'])