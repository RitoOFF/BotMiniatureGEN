import discord
import fade
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import requests
from io import BytesIO
import json
import asyncio
import time

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
bot.flou = {}
bot.border = {}
bot.overlay = {}
bot.color = {}

created_miniature_channels = set()
class ColorButton(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="1", style=discord.ButtonStyle.blurple)    
    async def first(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        bot.color[interaction.user.id] = 1
        await interaction.response.send_message("Send your title: ")
        title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.title[interaction.user.id] = title_msg.content

        await interaction.channel.send("Send the size of text: ")
        size_title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.size_title[interaction.user.id] = size_title_msg.content
 
        file1 = discord.File("img/font.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FontButton())  
    @discord.ui.button(label="2", style=discord.ButtonStyle.blurple)    
    async def second(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        bot.color[interaction.user.id] = 2
        await interaction.response.send_message("Send your title: ")
        title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.title[interaction.user.id] = title_msg.content

        await interaction.channel.send("Send the size of text: ")
        size_title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.size_title[interaction.user.id] = size_title_msg.content
 
        file1 = discord.File("img/font.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FontButton())    
    @discord.ui.button(label="3", style=discord.ButtonStyle.blurple)    
    async def three(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        bot.color[interaction.user.id] = 3
        await interaction.response.send_message("Send your title: ")
        title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.title[interaction.user.id] = title_msg.content

        await interaction.channel.send("Send the size of text: ")
        size_title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.size_title[interaction.user.id] = size_title_msg.content
 
        file1 = discord.File("img/font.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FontButton())      
    @discord.ui.button(label="4", style=discord.ButtonStyle.blurple)    
    async def foor(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        bot.color[interaction.user.id] = 4
        await interaction.response.send_message("Send your title: ")
        title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.title[interaction.user.id] = title_msg.content

        await interaction.channel.send("Send the size of text: ")
        size_title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.size_title[interaction.user.id] = size_title_msg.content
 
        file1 = discord.File("img/font.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FontButton())    
    @discord.ui.button(label="5", style=discord.ButtonStyle.blurple)    
    async def five(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        bot.color[interaction.user.id] = 5
        await interaction.response.send_message("Send your title: ")
        title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.title[interaction.user.id] = title_msg.content

        await interaction.channel.send("Send the size of text: ")
        size_title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.size_title[interaction.user.id] = size_title_msg.content
 
        file1 = discord.File("img/font.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FontButton())        
    @discord.ui.button(label="6", style=discord.ButtonStyle.blurple)    
    async def six(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        bot.color[interaction.user.id] = 6
        await interaction.response.send_message("Send your title: ")
        title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.title[interaction.user.id] = title_msg.content

        await interaction.channel.send("Send the size of text: ")
        size_title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.size_title[interaction.user.id] = size_title_msg.content
 
        file1 = discord.File("img/font.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FontButton())  
    @discord.ui.button(label="7", style=discord.ButtonStyle.blurple)    
    async def seven(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        bot.color[interaction.user.id] = 7
        await interaction.response.send_message("Send your title: ")
        title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.title[interaction.user.id] = title_msg.content

        await interaction.channel.send("Send the size of text: ")
        size_title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.size_title[interaction.user.id] = size_title_msg.content
 
        file1 = discord.File("img/font.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FontButton())        
    @discord.ui.button(label="8", style=discord.ButtonStyle.blurple)    
    async def eight(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        bot.color[interaction.user.id] = 8
        await interaction.response.send_message("Send your title: ")
        title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.title[interaction.user.id] = title_msg.content

        await interaction.channel.send("Send the size of text: ")
        size_title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.size_title[interaction.user.id] = size_title_msg.content
 
        file1 = discord.File("img/font.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FontButton())         
    @discord.ui.button(label="9", style=discord.ButtonStyle.blurple)    
    async def nine(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        bot.color[interaction.user.id] = 9
        await interaction.response.send_message("Send your title: ")
        title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.title[interaction.user.id] = title_msg.content

        await interaction.channel.send("Send the size of text: ")
        size_title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.size_title[interaction.user.id] = size_title_msg.content
 
        file1 = discord.File("img/font.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FontButton())  
    @discord.ui.button(label="10", style=discord.ButtonStyle.blurple)    
    async def ten(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        bot.color[interaction.user.id] = 10
        await interaction.response.send_message("Send your title: ")
        title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.title[interaction.user.id] = title_msg.content

        await interaction.channel.send("Send the size of text: ")
        size_title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.size_title[interaction.user.id] = size_title_msg.content
 
        file1 = discord.File("img/font.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FontButton())  

class BorderButton(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="1", style=discord.ButtonStyle.blurple)    
    async def first(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose your Color for the text")
        bot.border[interaction.user.id] = "element/other/border/border_1.png" 
        file1 = discord.File("img/color.png", filename="color.png")

        await interaction.channel.send(file=file1, view=ColorButton())  
    @discord.ui.button(label="2", style=discord.ButtonStyle.blurple)    
    async def second(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose your Color for the text")
        bot.border[interaction.user.id] = "element/other/border/border_2.png"
        file1 = discord.File("img/color.png", filename="color.png")

        await interaction.channel.send(file=file1, view=ColorButton())    
    @discord.ui.button(label="3", style=discord.ButtonStyle.blurple)    
    async def three(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose your Color for the text")
        bot.border[interaction.user.id] = "element/other/border/border_3.png"
        file1 = discord.File("img/color.png", filename="color.png")

        await interaction.channel.send(file=file1, view=ColorButton())      
    @discord.ui.button(label="4", style=discord.ButtonStyle.blurple)    
    async def foor(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose your Color for the text")
        bot.border[interaction.user.id] = "element/other/border/border_4.png"
        file1 = discord.File("img/color.png", filename="color.png")

        await interaction.channel.send(file=file1, view=ColorButton())    
    @discord.ui.button(label="5", style=discord.ButtonStyle.blurple)    
    async def five(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose your Color for the text")
        bot.border[interaction.user.id] = "element/other/border/border_5.png"
        file1 = discord.File("img/color.png", filename="color.png")

        await interaction.channel.send(file=file1, view=ColorButton())      
    @discord.ui.button(label="6", style=discord.ButtonStyle.blurple)    
    async def six(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose your Color for the text")
        bot.border[interaction.user.id] = "element/other/border/border_6.png"
        file1 = discord.File("img/color.png", filename="color.png")

        await interaction.channel.send(file=file1, view=ColorButton())  
    @discord.ui.button(label="7", style=discord.ButtonStyle.blurple)    
    async def seven(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose your Color for the text")
        bot.border[interaction.user.id] = "element/other/border/border_7.png"
        file1 = discord.File("img/color.png", filename="color.png")

        await interaction.channel.send(file=file1, view=ColorButton())      
    @discord.ui.button(label="8", style=discord.ButtonStyle.blurple)    
    async def eight(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose your Color for the text")
        bot.border[interaction.user.id] = "element/other/border/border_8.png"
        file1 = discord.File("img/color.png", filename="color.png")

        await interaction.channel.send(file=file1, view=ColorButton())       
    @discord.ui.button(label="9", style=discord.ButtonStyle.blurple)    
    async def nine(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose your Color for the text")
        bot.border[interaction.user.id] = "element/other/border/border_9.png"
        file1 = discord.File("img/color.png", filename="color.png")

        await interaction.channel.send(file=file1, view=ColorButton())  

class OverlayButton(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="1", style=discord.ButtonStyle.blurple)    
    async def first(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose your border")
        bot.overlay[interaction.user.id] = "element/other/overlay/overlay_1.png"
        file1 = discord.File("element/other/border/border.png", filename="border.png")

        await interaction.channel.send(file=file1, view=BorderButton())  
    @discord.ui.button(label="2", style=discord.ButtonStyle.blurple)    
    async def second(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose your border")
        bot.overlay[interaction.user.id] = "element/other/overlay/overlay_2.png"
        file1 = discord.File("element/other/border/border.png", filename="border.png")

        await interaction.channel.send(file=file1, view=BorderButton())  
    @discord.ui.button(label="3", style=discord.ButtonStyle.blurple)    
    async def three(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose your border")
        bot.overlay[interaction.user.id] = "element/other/overlay/overlay_3.png"
        file1 = discord.File("element/other/border/border.png", filename="border.png")

        await interaction.channel.send(file=file1, view=BorderButton())   
    @discord.ui.button(label="4", style=discord.ButtonStyle.blurple)    
    async def foor(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose your border")
        bot.overlay[interaction.user.id] = "element/other/overlay/overlay_4.png"
        file1 = discord.File("element/other/border/border.png", filename="border.png")

        await interaction.channel.send(file=file1, view=BorderButton())  
    @discord.ui.button(label="5", style=discord.ButtonStyle.blurple)    
    async def five(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose your border")
        bot.overlay[interaction.user.id] = "element/other/overlay/overlay_5.png"
        file1 = discord.File("element/other/border/border.png", filename="border.png")

        await interaction.channel.send(file=file1, view=BorderButton())    
    @discord.ui.button(label="6", style=discord.ButtonStyle.blurple)    
    async def six(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose your border")
        bot.overlay[interaction.user.id] = "element/other/overlay/overlay_6.png"
        file1 = discord.File("element/other/border/border.png", filename="border.png")

        await interaction.channel.send(file=file1, view=BorderButton())  
    @discord.ui.button(label="7", style=discord.ButtonStyle.blurple)    
    async def seven(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose your border")
        bot.overlay[interaction.user.id] = "element/other/overlay/overlay_7.png"
        file1 = discord.File("element/other/border/border.png", filename="border.png")

        await interaction.channel.send(file=file1, view=BorderButton())      
    @discord.ui.button(label="8", style=discord.ButtonStyle.blurple)    
    async def eight(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose your border")
        bot.overlay[interaction.user.id] = "element/other/overlay/overlay_8.png"
        file1 = discord.File("element/other/border/border.png", filename="border.png")

        await interaction.channel.send(file=file1, view=BorderButton())        
    @discord.ui.button(label="9", style=discord.ButtonStyle.blurple)    
    async def nine(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose your border")
        bot.overlay[interaction.user.id] = "element/other/overlay/overlay_9.png"
        file1 = discord.File("element/other/border/border.png", filename="border.png")

        await interaction.channel.send(file=file1, view=BorderButton())  

class FlouButton(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="1", style=discord.ButtonStyle.blurple)    
    async def first(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.flou[interaction.user.id] = 1
        file1 = discord.File("element/other/overlay/overlay.png", filename="overlay.png")

        await interaction.channel.send(file=file1, view=OverlayButton())  
    @discord.ui.button(label="2", style=discord.ButtonStyle.blurple)    
    async def second(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.flou[interaction.user.id] = 2
        file1 = discord.File("element/other/overlay/overlay.png", filename="overlay.png")

        await interaction.channel.send(file=file1, view=OverlayButton())  
    @discord.ui.button(label="3", style=discord.ButtonStyle.blurple)    
    async def three(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.flou[interaction.user.id] = 3
        file1 = discord.File("element/other/overlay/overlay.png", filename="overlay.png")

        await interaction.channel.send(file=file1, view=OverlayButton())   
    @discord.ui.button(label="4", style=discord.ButtonStyle.blurple)    
    async def foor(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.flou[interaction.user.id] = 4
        file1 = discord.File("element/other/overlay/overlay.png", filename="overlay.png")

        await interaction.channel.send(file=file1, view=OverlayButton())  
    @discord.ui.button(label="5", style=discord.ButtonStyle.blurple)    
    async def five(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.flou[interaction.user.id] = 5
        file1 = discord.File("element/other/overlay/overlay.png", filename="overlay.png")

        await interaction.channel.send(file=file1, view=OverlayButton())  
    @discord.ui.button(label="6", style=discord.ButtonStyle.blurple)    
    async def six(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.flou[interaction.user.id] = 6
        file1 = discord.File("element/other/overlay/overlay.png", filename="overlay.png")

        await interaction.channel.send(file=file1, view=OverlayButton())  
    @discord.ui.button(label="7", style=discord.ButtonStyle.blurple)    
    async def seven(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.flou[interaction.user.id] = 7
        file1 = discord.File("element/other/overlay/overlay.png", filename="overlay.png")

        await interaction.channel.send(file=file1, view=OverlayButton())  
    @discord.ui.button(label="8", style=discord.ButtonStyle.blurple)    
    async def eight(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.flou[interaction.user.id] = 8
        file1 = discord.File("element/other/overlay/overlay.png", filename="overlay.png")

        await interaction.channel.send(file=file1, view=OverlayButton())  
    @discord.ui.button(label="9", style=discord.ButtonStyle.blurple)    
    async def nine(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.flou[interaction.user.id] = 9
        file1 = discord.File("element/other/overlay/overlay.png", filename="overlay.png")

        await interaction.channel.send(file=file1, view=OverlayButton())  
class ElementFortiniteButton(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="1", style=discord.ButtonStyle.blurple)    
    async def first(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.element[interaction.user.id] = "element/fortnite/1.png" 
        file1 = discord.File("img/flou.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FlouButton())  
    @discord.ui.button(label="2", style=discord.ButtonStyle.blurple)    
    async def second(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.element[interaction.user.id] = "element/fortnite/2.png" 
        file1 = discord.File("img/flou.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FlouButton())  
    @discord.ui.button(label="3", style=discord.ButtonStyle.blurple)    
    async def their(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.element[interaction.user.id] = "element/fortnite/3.png" 
        file1 = discord.File("img/flou.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FlouButton())  
    @discord.ui.button(label="4", style=discord.ButtonStyle.blurple)    
    async def foor(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.element[interaction.user.id] = "element/fortnite/4.png" 
        file1 = discord.File("img/flou.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FlouButton())  
    @discord.ui.button(label="5", style=discord.ButtonStyle.blurple)    
    async def five(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.element[interaction.user.id] = "element/fortnite/5.png" 
        file1 = discord.File("img/flou.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FlouButton())  
    @discord.ui.button(label="6", style=discord.ButtonStyle.blurple)    
    async def six(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.element[interaction.user.id] = "element/fortnite/6.png" 
        file1 = discord.File("img/flou.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FlouButton())   
    @discord.ui.button(label="7", style=discord.ButtonStyle.blurple)    
    async def seven(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.element[interaction.user.id] = "element/fortnite/7.png" 
        file1 = discord.File("img/flou.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FlouButton())  
    @discord.ui.button(label="8", style=discord.ButtonStyle.blurple)    
    async def eight(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.element[interaction.user.id] = "element/fortnite/8.png" 
        file1 = discord.File("img/flou.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FlouButton())  
    @discord.ui.button(label="9", style=discord.ButtonStyle.blurple)    
    async def nine(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.element[interaction.user.id] = "element/fortnite/9.png" 
        file1 = discord.File("img/flou.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FlouButton())  

class ElementMinecraftButton(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="1", style=discord.ButtonStyle.blurple)    
    async def first(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.element[interaction.user.id] = "element/minecraft/1_minecraft.png" 
        file1 = discord.File("img/flou.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FlouButton())  
    @discord.ui.button(label="2", style=discord.ButtonStyle.blurple)    
    async def second(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.element[interaction.user.id] = "element/minecraft/2_minecraft.png" 
        file1 = discord.File("img/flou.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FlouButton())  
    @discord.ui.button(label="3", style=discord.ButtonStyle.blurple)    
    async def their(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.element[interaction.user.id] = "element/minecraft/3_minecraft.png" 
        file1 = discord.File("img/flou.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FlouButton())  
    @discord.ui.button(label="4", style=discord.ButtonStyle.blurple)    
    async def foor(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.element[interaction.user.id] = "element/minecraft/4_minecraft.png" 
        file1 = discord.File("img/flou.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FlouButton())  
    @discord.ui.button(label="5", style=discord.ButtonStyle.blurple)    
    async def five(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.element[interaction.user.id] = "element/minecraft/5_minecraft.png" 
        file1 = discord.File("img/flou.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FlouButton())  
    @discord.ui.button(label="6", style=discord.ButtonStyle.blurple)    
    async def six(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.element[interaction.user.id] = "element/minecraft/6_minecraft.png" 
        file1 = discord.File("img/flou.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FlouButton())   
    @discord.ui.button(label="7", style=discord.ButtonStyle.blurple)    
    async def seven(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.element[interaction.user.id] = "element/minecraft/7_minecraft.png" 
        file1 = discord.File("img/flou.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FlouButton())  
    @discord.ui.button(label="8", style=discord.ButtonStyle.blurple)    
    async def eight(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.element[interaction.user.id] = "element/minecraft/8_minecraft.png" 
        file1 = discord.File("img/flou.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FlouButton())  
    @discord.ui.button(label="9", style=discord.ButtonStyle.blurple)    
    async def nine(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"Choose the intensity on your blur")
        bot.element[interaction.user.id] = "element/minecraft/9_minecraft.png" 
        file1 = discord.File("img/flou.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FlouButton())  

class TypeMiniatureButton(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="Fortnite", style=discord.ButtonStyle.blurple)    
    async def fortnite(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message("Choose your elements on your miniature: ")
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

        await interaction.channel.send(files=[file_1, file_2, file_3, file_4, file_5, file_6, file_7, file_8, file_9], view=ElementFortiniteButton())
    @discord.ui.button(label="Minecraft", style=discord.ButtonStyle.blurple)    
    async def minecraft(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message("Choose your elements on your miniature: ")
        bot.type[interaction.user.id] = "minecraft"
 
        file_1 = discord.File("element/minecraft/choose/1.png", filename="1_minecraft.png")
        file_2 = discord.File("element/minecraft/choose/2.png", filename="2_minecraft.png")
        file_3 = discord.File("element/minecraft/choose/3.png", filename="3_minecraft.png")
        file_4 = discord.File("element/minecraft/choose/4.png", filename="4_minecraft.png")
        file_5 = discord.File("element/minecraft/choose/5.png", filename="5_minecraft.png")
        file_6 = discord.File("element/minecraft/choose/6.png", filename="6_minecraft.png")
        file_7 = discord.File("element/minecraft/choose/7.png", filename="7_minecraft.png")
        file_8 = discord.File("element/minecraft/choose/8.png", filename="8_minecraft.png")
        file_9 = discord.File("element/minecraft/choose/9.png", filename="9_minecraft.png")

        await interaction.channel.send(files=[file_1, file_2, file_3, file_4, file_5, file_6, file_7, file_8, file_9], view=ElementMinecraftButton())
    @discord.ui.button(label="Valorant", style=discord.ButtonStyle.blurple)    
    async def valorant(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.channel.send("Send your title: ")
        title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.title[interaction.user.id] = title_msg.content

        await interaction.channel.send("Send the size of text: ")
        size_title_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user)
        bot.size_title[interaction.user.id] = size_title_msg.content
 
        file1 = discord.File("img/font.png", filename="font.png")

        await interaction.channel.send(file=file1, view=FontButton())    

class SizeButton(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="Miniature", style=discord.ButtonStyle.blurple)    
    async def first(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message("Send your background: ")
        bot.size[interaction.user.id] = (1920, 1080)
        image_msg = await bot.wait_for('message', check=lambda message: message.author == interaction.user and message.attachments)
        bot.image_url[interaction.user.id] = image_msg.attachments[0].url

        await interaction.channel.send("Choose the type of miniature", view=TypeMiniatureButton())
        

class FontButton(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="1", style=discord.ButtonStyle.blurple)    
    async def font_1(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"The font is set on 1")
        font_path = "font/1_font.ttf"
        bot.font[interaction.user.id] = font_path
        await interaction.channel.send("What position you choose ?", view=PositionButton()) 
    @discord.ui.button(label="2", style=discord.ButtonStyle.blurple)    
    async def font_2(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"The font is set on 2")
        font_path = "font/2_font.ttf"
        bot.font[interaction.user.id] = font_path   
        await interaction.channel.send("What position you choose ?", view=PositionButton()) 
    @discord.ui.button(label="3", style=discord.ButtonStyle.blurple)    
    async def font_3(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"The font is set on 3")
        font_path = "font/3_font.ttf"
        bot.font[interaction.user.id] = font_path 
        file = discord.File("img/position.png", filename="position.png")
        await interaction.channel.send("What position you choose ?",file=file, view=PositionButton())        
    @discord.ui.button(label="4", style=discord.ButtonStyle.blurple)    
    async def font_4(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"The font is set on 4")
        font_path = "font/4_font.ttf"
        bot.font[interaction.user.id] = font_path 
        file = discord.File("img/position.png", filename="position.png")
        await interaction.channel.send("What position you choose ?",file=file, view=PositionButton())        
    @discord.ui.button(label="5", style=discord.ButtonStyle.blurple)    
    async def font_5(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message("The font is set on 5")
        font_path = "font/5_font.ttf"
        bot.font[interaction.user.id] = font_path 
        file = discord.File("img/position.png", filename="position.png")
        await interaction.channel.send("What position you choose ?",file=file, view=PositionButton())      
    @discord.ui.button(label="6", style=discord.ButtonStyle.blurple)    
    async def font_6(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message(f"The font is set on 6")
        font_path = "font/6_font.ttf"
        bot.font[interaction.user.id] = font_path 
        file = discord.File("img/position.png", filename="position.png")
        await interaction.channel.send("What position you choose ?",file=file, view=PositionButton())                  


class PositionButton(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    async def send_confirmation_message(self, interaction: discord.Interaction, position: str) -> None:
        await interaction.response.send_message(f"The position is set")

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
            bot.element[interaction.user.id],
            bot.flou[interaction.user.id],
            bot.border[interaction.user.id],
            bot.overlay[interaction.user.id],
            bot.color[interaction.user.id]
        )

    @discord.ui.button(label="1", style=discord.ButtonStyle.blurple)    
    async def top_left(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self.send_confirmation_message(interaction, "top left")
        await self.send_create_miniature(interaction, "top_left")

    @discord.ui.button(label="2", style=discord.ButtonStyle.blurple)    
    async def top_center(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self.send_confirmation_message(interaction, "top center")
        await self.send_create_miniature(interaction, "top_center")

    @discord.ui.button(label="3", style=discord.ButtonStyle.blurple)    
    async def top_right(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self.send_confirmation_message(interaction, "top right")
        await self.send_create_miniature(interaction, "top_right")    


    @discord.ui.button(label="4", style=discord.ButtonStyle.blurple)    
    async def middle_left(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self.send_confirmation_message(interaction, "middle left")
        await self.send_create_miniature(interaction, "middle_left")

    @discord.ui.button(label="5", style=discord.ButtonStyle.blurple)    
    async def middle(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self.send_confirmation_message(interaction, "middle")
        await self.send_create_miniature(interaction, "middle")

    @discord.ui.button(label="6", style=discord.ButtonStyle.blurple)    
    async def middle_right(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self.send_confirmation_message(interaction, "middle right")
        await self.send_create_miniature(interaction, "middle_right")

    @discord.ui.button(label="7", style=discord.ButtonStyle.blurple)    
    async def bottom_left(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self.send_confirmation_message(interaction, "bottom left")
        await self.send_create_miniature(interaction, "bottom_left")

    @discord.ui.button(label="8", style=discord.ButtonStyle.blurple)    
    async def bottom_center(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self.send_confirmation_message(interaction, "bottom center")
        await self.send_create_miniature(interaction, "bottom_center")

    @discord.ui.button(label="9", style=discord.ButtonStyle.blurple)    
    async def bottom_right(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await self.send_confirmation_message(interaction, "bottom right")
        await self.send_create_miniature(interaction, "bottom_right")

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
        guild = bot.get_guild(payload.guild_id)
        owner = await guild.fetch_member(payload.user_id)


        role_id = config["role_contributor"]

       
        role = discord.utils.get(owner.roles, id=role_id)
        if role:
            
            category_id = config['category_shop']
            category = bot.get_channel(category_id)
            if category:
                existing_miniature_channels = [ch for ch in category.channels if ch.name.startswith("miniature-") and owner in ch.members]
                if existing_miniature_channels:
                    return

            if category and isinstance(category, discord.CategoryChannel):
                existing_miniatures = sum(1 for channel in category.channels if channel.name.startswith("miniature-"))
                next_miniature_name = f"miniature-{existing_miniatures + 1}"

                new_channel = await category.create_text_channel(name=next_miniature_name)
                created_miniature_channels.add(owner.id)
                await new_channel.set_permissions(guild.default_role, read_messages=False)
                await new_channel.set_permissions(owner, read_messages=True, send_messages=True)
                await new_channel.send("What types you choose ?", view=SizeButton())
                reply_message = await message.reply(f"A miniature channel has been created! {new_channel.mention}")
                await asyncio.sleep(5)
                await reply_message.delete()
            else:
                print("Could not find the specified category.")
        else:
            reply_message = await message.reply("You must have at least 1 invitation to become a Contributor or upgrade to Premium by clicking on the emoji to access the Premium offer. 🌟")
            await asyncio.sleep(5)
            await reply_message.delete()
            return       

@bot.command(name="miniature", description="Allows you to generate your thumbnail")    
async def miniature(ctx):

 
    if ctx.author.id in created_miniature_channels:
        return
    
    if ctx.author.id != ctx.guild.owner_id:
        await ctx.send("Only the server owner can use this command.")
        return
    message = await ctx.send(config['message'])
    await message.add_reaction("🛒")
    await message.add_reaction("🤝")
    await message.add_reaction("👮")
    await message.add_reaction("🧷")
    await message.add_reaction("⭐")

async def create_miniature(interaction, image_url, width, height, title, position, titlesize, font, type, element, flou, border, overlay, color):
    try:
        response = requests.get(image_url)
        response.raise_for_status()

        background_image = Image.open(BytesIO(response.content))
        background_image = background_image.resize((width, height))
        background_image = background_image.filter(ImageFilter.GaussianBlur(flou))

        if type == "fortnite" or type == "minecraft":
            overlay_image = Image.open(element)  
            overlay_width, overlay_height = overlay_image.size

            if overlay_width != width or overlay_height != height:
                overlay_image = overlay_image.resize((width, height))
                
            background_image.paste(overlay_image, (0, 0), overlay_image)    

        overlay_image = Image.open(overlay)
        background_image.paste(overlay_image, (0, 0), overlay_image)    

        border_image = Image.open(border)
        background_image.paste(border_image, (0, 0), border_image)    

        base_image = Image.open("element/other/basic.png")
        background_image.paste(base_image, (0, 0), base_image)    

        draw = ImageDraw.Draw(background_image)
        try:
            titlesize_int = int(titlesize)
            if titlesize_int < 10 or titlesize_int > 300:
                titlesize_int = 150  
        except ValueError:
            titlesize_int = 150 

        font_title = ImageFont.truetype(font, size=titlesize_int)
        font_footer = ImageFont.truetype("font/1_font.ttf", size=35)  

        wrapped_title = title

        text_bbox_title = draw.textbbox((0, 0), wrapped_title, font=font_title)
        text_width_title = text_bbox_title[2] - text_bbox_title[0]
        text_height_title = text_bbox_title[3] - text_bbox_title[1]

        offset = 50

        if position == "top_left":
            position_x_title = offset
            position_y_title = offset
        elif position == "top_center":
            position_x_title = max((width - text_width_title) // 2, offset)
            position_y_title = offset
        elif position == "top_right":
            position_x_title = max(width - text_width_title - offset, offset)
            position_y_title = offset
        elif position == "middle_left":
            position_x_title = offset
            position_y_title = max((height - text_height_title) // 2, offset)
        elif position == "middle":
            position_x_title = max((width - text_width_title) // 2, offset)
            position_y_title = max((height - text_height_title) // 2, offset)
        elif position == "middle_right":
            position_x_title = max(width - text_width_title - offset, offset)
            position_y_title = max((height - text_height_title) // 2, offset)
        elif position == "bottom_left":
            position_x_title = offset
            position_y_title = max(height - text_height_title - offset, offset)
        elif position == "bottom_center":
            position_x_title = max((width - text_width_title) // 2, offset)
            position_y_title = max(height - text_height_title - offset, offset)
        elif position == "bottom_right":
            position_x_title = max(width - text_width_title - offset, offset)
            position_y_title = max(height - text_height_title - offset, offset)

        outline_width = 9
        outline_color = (0, 0, 0)
        draw.text((position_x_title - outline_width, position_y_title - outline_width), title, fill=outline_color, font=font_title)
        draw.text((position_x_title + outline_width, position_y_title - outline_width), title, fill=outline_color, font=font_title)
        draw.text((position_x_title - outline_width, position_y_title + outline_width), title, fill=outline_color, font=font_title)
        draw.text((position_x_title + outline_width, position_y_title + outline_width), title, fill=outline_color, font=font_title)
    
        draw.text((position_x_title, position_y_title), title, fill=(255, 255, 255), font=font_title)
    
        role_id = config["role_prenium"]

       
        role = discord.utils.get(interaction.user.roles, id=role_id)
        if role:
            print("prenium user")
        else:
            footer_text = "DevDen & Bot"  

            text_bbox_footer = draw.textbbox((0, 0), footer_text, font=font_footer)
            text_width_footer = text_bbox_footer[2] - text_bbox_footer[0]
            text_height_footer = text_bbox_footer[3] - text_bbox_footer[1]

            position_x_footer = (width - text_width_footer) // 2
            position_y_footer = height - text_height_footer - 10  
            draw.text((position_x_footer, position_y_footer), footer_text, fill=(255, 255, 255), font=font_footer)
    
        with BytesIO() as img_bytes:
            background_image.save(img_bytes, format="PNG")
            img_bytes.seek(0)
            file = discord.File(img_bytes, filename="DEVDEN-deminiature-render.png")
        with BytesIO() as img_bytes:
            background_image.save(img_bytes, format="PNG")
            img_bytes.seek(0)
            file1 = discord.File(img_bytes, filename="DEVDEN-deminiature.png")

        if role:
            print("prenium user")
        else:
            category_result_id = config["category_result"]
            category_result_channel = interaction.guild.get_channel(category_result_id)                            
            message = await category_result_channel.send(f"# DevDen - GFX\n> **Miniature** Made by us for {interaction.user.mention}!\n> Feel free to invite your friends to the server; we would be very grateful 🤗", file=file)
            await message.add_reaction("💖")
            await message.add_reaction("👍")
            await message.add_reaction("👎")
                     
        await interaction.channel.send(f"# DevDen - GFX\n\n> :shopping_cart: 『Here's your miniature {interaction.user.mention} that you requested with all the selections you've made. If you notice anything unusual or to improve, please report it in #✨・suggest.\n:sparkles:『The channel will delete soon. If you want to design the render yourself, you can download it. The render is automatically sent to #👀・shop-render, as you're not premium.』\n\n:handshake:『If you want to become premium to avoid having the copyright at the bottom of the image, as well as a render in 4K, full HD, advanced and private features, and not having your render sent to #👀・shop-render, please contact rito.off.』", file=file1)

        await asyncio.sleep(25)
        if interaction.channel:
            await interaction.channel.delete()
            created_miniature_channels.remove(interaction.user.id)

    except requests.exceptions.HTTPError as e:
        await interaction.user.send(f"An error occurred while fetching the image: {e}")
        if interaction.channel:
            await interaction.channel.delete()
            created_miniature_channels.remove(interaction.user.id)
    except (IOError, OSError) as e:
        await interaction.user.send(f"An error occurred while processing the image: {e}")
        if interaction.channel:
            await interaction.channel.delete()
            created_miniature_channels.remove(interaction.user.id)
    except Exception as e:
        await interaction.user.send(f"An unexpected error occurred: {e}")
        if interaction.channel:
            await interaction.channel.delete()
            created_miniature_channels.remove(interaction.user.id)



bot.run(config['token'])