import discord,random,asyncio
from discord.ext import commands
from cmath import log
from distutils.sysconfig import PREFIX
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

bot = discord.Bot()
a = ["λκ΅¬μΈμ ?π","μλνμΈμπ","μλ !π","λ°κ°μ !π","μλ ? λλ ν¬λλ΄μ΄μΌ !π","λλ.. λκ΅¬μΌ..?π€","λΏ‘λΏ‘λΏ‘~π¨","μΌ1λ―Έ~π","μΌ λ­λ΄ !π‘","π€"]

@bot.event
async def on_ready():
    print("ready to ν¬λλ΄ !")

@bot.slash_command(guild_ids = [1065253502068207667], description="ν¬λλ΄μκ² μΈμ¬λ₯Ό ν΄λ³΄μΈμ !")
async def μΈμ¬(ctx):
    rd = random.choice(a)
    embed=discord.Embed(title=" ", color=0xb750fb)
    embed.add_field(name="ν¬λλ΄ : {}".format(rd), value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.send(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="νμ€ν° λλ¨Έλ¦¬ ?")
async def νμ€ν°(ctx):
    embed=discord.Embed(title=" ", description="νμ€ν°λ λλ¨Έλ¦¬λ€ ?", color=0xb750fb)
    embed.set_author(name="νμ€ν° / Hister")
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : μ±μ₯λΆκ°", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  νμ€ν°λ νλͺ¨ ? λλ¨Έλ¦¬ ? / λλλΌνν μΌμ΄μ§ λΉν¨", value="", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="νΌνΌ PiPi")
async def νΌνΌ(ctx):
    embed=discord.Embed(title=" ", description="νΌνΌ = PiPi = μμ", color=0xb750fb)
    embed.set_author(name="νΌνΌ / PiPi")
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/399048531366772736/824e229fcffb0c9a536e45d90bd69665.webp?size=24')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : μ±μ₯λΆκ°", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  νΌνΌ is μμ", value="", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="μμ = YOYO")
async def μμ(ctx):
    embed=discord.Embed(title=" ", description="μμ : λ£¨μΉ΄μΏ λ₯Ό κ΅μ₯ν μ¬λν¨ / μμ", color=0xb750fb)
    embed.set_author(name="μμ / YOYO")
    embed.set_thumbnail(url='https://emojigraph.org/media/google/yo-yo_1fa80.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : μ±μ₯λΆκ°", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μμ = YOYO = λ£¨μΉ΄μΏ ", value="", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="λμμΌ = ν¬λ¦¬μ€νμμΌ")
async def μμΌ(ctx):
    embed=discord.Embed(title=" ", description="λμμΌ / ν¬μμΌ", color=0xb750fb)
    embed.set_author(name="ν¬λ¦¬μ€ν μμΌ / Crystal Isles")
    embed.set_thumbnail(url='https://ark.wiki.gg/images/e/e2/The_Island_Map.jpg')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : μ±μ₯λΆκ°", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  λμμΌ = ν¬μμΌ", value="", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="κΈ°κ°λΈν μ¬μ°λ£¨μ€ μ±μ₯μκ°")
async def κΈ°κ°(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="κΈ°κ°λΈν μ¬μ°λ£¨μ€ / Giganotosaurus")
    embed.set_thumbnail(url='https://w.namu.la/s/503de9b9720163ed2c4ac240f8e1198c7b756436af83c1680f17d6b770f9dcf65e20df49ad223b5e60bee0e1df972d15c10c2255115518ca2875a2c0c009c2c56b058516e62769c337fcdf907e99decaedc50683fed022dfe576c0756170698f791bc0b1cfe90273feb278bd5cc6aff4')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 10μΌ 3μκ° 59λΆ", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° : 2μΌ 1μκ° 59λΆ 45μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 1μΌ 23λΆ 54μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 4μΌ 1μκ° 35λΆ 39μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 5μΌ 1μκ° 59λΆ 34μ΄ ", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="λ²¨λ‘λμ¬μ°λ£¨μ€ μ±μ₯μκ°")
async def λ²¨λ‘(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="λ²¨λ‘λμ¬μ°λ£¨μ€ / Velonasaur")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806896756998537276/velonasaur.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 1μΌ 22μκ° 17λΆ 46μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° : 1μκ° 8λΆ 10μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 4μκ° 37λΆ 46μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 18μκ° 31λΆ 6μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 23μκ° 8λΆ 53μ΄ ", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="μ€νκ³ μ¬μ°λ£¨μ€ μ±μ₯μκ°")
async def μ€νκ³ (ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="μ€νκ³ μ¬μ°λ£¨μ€ / Stegosaurus")
    embed.set_thumbnail(url='https://obj-sg.the1.wiki/data/737465676f7361757275732e706e67.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 2μΌ 3μκ° 26λΆ 25μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° : 2μκ° 46λΆ 39μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 5μκ° 8λΆ 38μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 20μκ° 34λΆ 34μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 1μΌ 1μκ° 43λΆ 12μ΄ ", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="μμ΄λ² μ±μ₯μκ°")
async def μμ΄λ²(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="λͺ¨λ  μμ΄λ² / ALL Wyvern")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806893887162548244/806894009670434856/crystalwyvern.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 3μΌ 20μκ° 35λΆ 33μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° : 4μκ° 59λΆ 58μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 9μκ° 15λΆ 33μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 1μΌ 13μκ° 2λΆ 13μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 1μΌ 22μκ° 17λΆ 46μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="λ§λκ°λ₯΄λ§ μ±μ₯μκ°")
async def λ§λ(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="λ§λκ°λ₯΄λ§ / Managarmr")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806897005195952149/managarmr.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 3μΌ 20μκ° 35λΆ 33μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μμ μκ° : 3μκ° 58λΆ 5μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 9μκ° 15λΆ 33μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 1μΌ 13μκ° 2λΆ 13μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 1μΌ 22μκ° 17λΆ 46μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="νλ¦¬μ§λΈμ¬μ°λ£¨μ€ μ±μ₯μκ°")
async def νλ¦¬μ§λΈ(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="νλ¦¬μ§λΈμ¬μ°λ£¨μ€ / Therizinosaur")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806896780196446278/therizinosaurus.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 4μΌ 19μκ° 44λΆ 26μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° : 1μκ° 39λΆ 59μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 11μκ° 34λΆ 26μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 1μΌ 22μκ° 17λΆ 46μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 2μΌ 9μκ° 52λΆ 13μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="μλμ°λ©μΈ μ±μ₯μκ°")
async def μλ©(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="μλμ°λ©μΈ / Shadowmane")
    embed.set_thumbnail(url='https://o.remove.bg/downloads/5ff38b0a-0e07-47a3-9136-a680c5ee13fc/ACTUAL-BLACK-removebg-preview-removebg-preview.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 2μΌ 43λΆ 58μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μμ μκ° : 2μκ° 23λΆ 48μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 4μκ° 52λΆ 23μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 19μ 29λΆ 35μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 1μΌ 21λΆ 59μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="λ μ€ μ±μ₯μκ°")
async def λ μ€(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="λ μ€ / Rex")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806896810333044836/rex.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 3μΌ 20μκ° 35λΆ 33μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° : 4μκ° 59λΆ 58μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 9μκ° 15λΆ 33μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 1μΌ 13μκ° 2λΆ 13μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 1μΌ 22μκ° 17λΆ 46μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="μ¬λ§κ· μ±μ₯μκ°")
async def μ¬λ§κ·(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="μ¬λ§κ· / Mantis")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806897004445696010/mantis.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 2μΌ 6μκ° 27λΆ 58μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° : 2μκ° 46λΆ 39μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 5μκ° 26λΆ 47μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 21μκ° 47λΆ 11μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 1μΌ 3μκ° 13λΆ 59μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="λ°μ€λͺ¨λμ€ μ±μ₯μκ°")
async def λ°μ€λͺ¨(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="λ°μ€λͺ¨λμ€ / Desmodus")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806893887162548244/806893972525023312/onyc.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 2μΌ 23μκ° 13λΆ 30μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μμ μκ° : 7μκ° 56λΆ 11μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 7μκ° 7λΆ 21μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 1μΌ 4μκ° 29λΆ 24μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 1μΌ 11μκ° 36λΆ 45μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="ν¬μνμ°ν°μ€ μ±μ₯μκ°")
async def ν¬μ(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="ν¬μνμ°ν°μ€ / Tusoteuthis")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894251073208330/806894678011674634/tusoteuthis.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 7μΌ 17μκ° 11λΆ 6μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° : 4μκ° 59λΆ 58μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 18μκ° 31λΆ 6μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 3μΌ 2μκ° 4λΆ 26μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 3μΌ 20μκ° 35λΆ 33μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="μ ν°λΌλμ€ μ±μ₯μκ°")
async def μ ν°(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="μ ν°λΌλμ€ / Yutyrannus")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806896756679508008/yutyrannus.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 7μΌ 17μκ° 11λΆ 6μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° : 4μκ° 59λΆ 58μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 18μκ° 31λΆ 6μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 3μΌ 2μκ° 4λΆ 26μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 3μΌ 20μκ° 35λΆ 33μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="μΌμ°° μ±μ₯μκ°")
async def μΌμ°°(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="μΌμ°° / Quetzal")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806893887162548244/806893917949526096/quetzal-1.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 5μΌ 12μκ° 16λΆ 30μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° : 16μκ° 39λΆ 55μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 13μκ° 13λΆ 39μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 2μΌ 4μκ° 54λΆ 36μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 2μΌ 18μκ° 8λΆ 15μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="μΉ΄λ₯΄λ³΄λ€λ―Έμ€ μ±μ₯μκ°")
async def μΉ΄λ₯΄λ³΄(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="μΉ΄λ₯΄λ³΄λ€λ―Έμ€ / Carbonemys")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806897238429007892/carbonemys.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 23μκ° 8λΆ 53μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° : 1μκ° 14λΆ 59μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 2μκ° 18λΆ 53μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 9μκ° 15λΆ 33μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 11μκ° 34λΆ 26μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="μΉ΄λ₯΄λΈνμ°λ£¨μ€ μ±μ₯μκ°")
async def μΉ΄λ₯΄λΈ(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="μΉ΄λ₯΄λΈνμ°λ£¨μ€ / Carnotaurus")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806897237745074217/carnotaurus.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 1μΌ 22μκ° 17λΆ 46μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° : 1μκ° 39λΆ 59μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 4μκ° 37λΆ 46μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 18μκ° 31λΆ 6μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 23μκ° 8λΆ 53μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="λ°μ΄λΈλμΏ μ€ μ±μ₯μκ°")
async def λ°μ΄λΈ(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="λ°μ΄λΈλμΏ μ€ / Deinonychus")
    embed.set_thumbnail(url='https://o.remove.bg/downloads/1ec9baaa-e3d6-4645-b04f-a52fb73f875c/images-removebg-preview.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 1μΌ 13μκ° 2λΆ 13μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° : 4μκ° 59λΆ 58μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 3μκ° 42λΆ 13μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 14μκ° 48λΆ 53μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 18μκ° 31λΆ 6μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="λΈλ¬λμ€ν μ»€ μ±μ₯μκ°")
async def λΈμ€(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="λΈλ¬λμ€ν μ»€ / Bloodstalker")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806897238722216006/bloodstalker.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 2μΌ 6μκ° 27λΆ 58μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° : 2μκ° 56λΆ 27μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 5μκ° 26λΆ 47μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 21μκ° 47λΆ 11μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 1μΌ 3μκ° 13λΆ 59μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="μ€νΌλΈ μ±μ₯μκ°")
async def μ€νΌλΈ(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="μ€νΌλΈ / Spino")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806896780670664724/spinosaur.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 2μΌ 23μκ° 13λΆ 30μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° : 3μκ° 50λΆ 45μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 7μκ° 7λΆ 21μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 1μΌ 4μκ° 29λΆ 24μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 1μΌ 11μκ° 36λΆ 45μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="λ°λ¦¬μ€λμ€ μ±μ₯μκ°")
async def λ°λ¦¬μ€(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="λ°λ¦¬μ€λμ€ / Baryonyx")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894251073208330/806894585674465301/baryonyx.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 1μΌ 22μκ° 17λΆ 46μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° : 1μκ° 59λΆ 59μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 4μκ° 37λΆ 46μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 18μκ° 31λΆ 6μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 23μκ° 8λΆ 53μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="μ€λΉμ€ μ±μ₯μκ°")
async def μ€λΉμ€(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="μ€λΉμ€ / Ovis")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806896934794690590/ovis.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 2μΌ 43λΆ 58μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μμ μκ° : 4μκ° 10λΆ 37μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 4μκ° 52λΆ 23μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 19μ 29λΆ 35μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 1μΌ 21λΆ 59μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="μμΏ μ€(μ λμ½) μ±μ₯μκ°")
async def μμΏ μ€(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="μμΏ μ€ / Equus(Unicorn)")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806897075416858624/equus.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 1μΌ 22μκ° 17λΆ 46μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μμ μκ° : 7μκ° 56λΆ 11μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 4μκ° 37λΆ 46μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 18μκ° 31λΆ 6μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 23μκ° 8λΆ 53μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="νλΌμΌλΌνλ¦¬μ μ±μ₯μκ°")
async def λ μ΄μ(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="νλΌμΌλΌνλ¦¬μ / Paraceratherium")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806896841500131349/paracer.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 3μΌ 20μκ° 35λΆ 33μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μμ μκ° : 7μκ° 56λΆ 11μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 9μκ° 15λΆ 33μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 1μΌ 13μκ° 2λΆ 13μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 1μΌ 22μκ° 17λΆ 46μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="λ€μμ€λ μ±μ₯μκ°")
async def λ€μμ€λ(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="λ€μμ€λ / Daeodon")
    embed.set_thumbnail(url='https://i.pinimg.com/originals/a8/1f/f5/a81ff5b85050e8e06e606acf80bd164a.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 2μΌ 43λΆ 58μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μμ μκ° : 7μκ° 56λΆ 11μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 4μκ° 52λΆ 23μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 19μ 29λΆ 35μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 1μΌ 21λΆ 59μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="λ§λͺ¨μ€ μ±μ₯μκ°")
async def λ§λͺ¨μ€(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="λ§λͺ¨μ€ / Mammoth")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806897004927254558/mammoth.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 3μΌ 10μκ° 18λΆ 16μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μμ μκ° : 7μκ° 56λΆ 11μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 8μκ° 13λΆ 49μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 1μΌ 8μκ° 55λΆ 18μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 1μΌ 17μκ° 9λΆ 8μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="νΈλΌμ½λ μ€ μ±μ₯μκ°")
async def νΈλΌ(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="νΈλΌμ½λ μ€ / Thylacoleo")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806896779622088704/thylacoleo.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 2μΌ 43λΆ 58μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μμ μκ° : 4μκ° 10λΆ 37μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 4μκ° 52λΆ 23μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 19μ 29λΆ 35μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 1μΌ 21λΆ 59μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="μλΈλ§ν¬λ‘­μ€ μ±μ₯μκ°")
async def μλΈλ§(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="μλΈλ§ν¬λ‘­μ€ / Sinomacrops")
    embed.set_thumbnail(url='https://o.remove.bg/downloads/56be9a20-929a-4b2a-be3b-6de57a998041/%EC%BA%A1%EC%B2%98-removebg-preview.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 1μΌ 13μκ° 2λΆ 13μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° : 2μκ° 37λΆ 52μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 3μκ° 42λΆ 13μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 14μκ° 48λΆ 53μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 18μκ° 31λΆ 6μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="ννμλΌ μ±μ₯μκ°")
async def νν(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="ννμλΌ / Tapejara")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806893887162548244/806893917369794600/tapejara-1.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 1μΌ 3μκ° 13λΆ 59μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° : 1μκ° 39λΆ 59μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 5μκ° 26λΆ 47μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 21μκ° 47λΆ 11μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 1μΌ 3μκ° 13λΆ 59μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="μνΈλ‘ μ±μ₯μκ°")
async def μνΈλ‘(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="μνΈλ‘ / Arthropluera")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806897239854546995/arthropluera.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 2μΌ 3μκ° 26λΆ 25μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° : 2μκ° 29λΆ 59μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 5μκ° 8λΆ 38μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 20μκ° 34λΆ 34μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 1μΌ 1μκ° 43λΆ 12μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="λ²λΈλ μ±μ₯μκ°")
async def λ²λΈλ(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="λ²λΈλ / Bulbdog")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806897237929099284/bulbdog.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 2μΌ 43λΆ 58μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μμ μκ° : 4μκ° 10λΆ 37μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 4μκ° 52λΆ 23μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 19μ 29λΆ 35μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 1μΌ 21λΆ 59μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="λ©κ°λ‘μ¬μ°λ£¨μ€ μ±μ₯μκ°")
async def λ©κ°λ‘(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="λ©κ°λ‘μ¬μ°λ£¨μ€ / Megalosaurus")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806896936728526918/megalosaurus.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 3μΌ 20μκ° 35λΆ 33μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° : 1μκ° 39λΆ 59μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 9μκ° 15λΆ 33μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 1μΌ 13μκ° 2λΆ 13μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 1μΌ 22μκ° 17λΆ 46μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="μλ¬ μ±μ₯μκ°")
async def μλ¬(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="μλ¬ / Otter")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806896935223033866/otter.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 21μκ° 2λΆ 37μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μμ μκ° : 7μκ° 56λΆ 11μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 2μκ° 6λΆ 15μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 8μκ° 25λΆ 3μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 10μκ° 31λΆ 18μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="νν€ μ±μ₯μκ°")
async def νν€(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="νν€ / Pachy")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806896842029138000/pachy.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 1μΌ 2μκ° 27λΆ 18μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° : 1μκ° 25λΆ 42μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 2μκ° 38λΆ 43μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 10μκ° 34λΆ 55μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 13μκ° 13λΆ 39μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="νλ‘μ½₯ν λ μ±μ₯μκ°")
async def μΊ₯κ±°λ£¨(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="νλ‘μ½₯ν λ / Procoptodon")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806896840200683550/procoptodon.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 1μΌ 22μκ° 17λΆ 46μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μμ μκ° : 3μκ° 58λΆ 5μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 4μκ° 37λΆ 46μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 18μκ° 31λΆ 6μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 23μκ° 8λΆ 53μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="λ‘€λ  μ±μ₯μκ°")
async def λ‘€λ (ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="λ‘€λ  / Roll Rat")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806896809355903006/rollrat.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 2μΌ 9μκ° 52λΆ 13μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μμ μκ° : 4μκ° 57λΆ 37μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 5μκ° 47λΆ 13μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 23μκ° 8λΆ 53μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 1μΌ 4μκ° 56λΆ 6μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="νΈλ¦¬μΌλΌν±μ€ μ±μ₯μκ°")
async def νΈλ¦¬μΌ(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="νΈλ¦¬μΌλΌν±μ€ / Triceratops")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806896758289989652/triceratops.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 1μΌ 22μκ° 17λΆ 46μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° : 2μκ° 29λΆ 59μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 4μκ° 37λΆ 46μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 18μκ° 31λΆ 6μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 23μκ° 8λΆ 53μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="μΈλ¦¬λΌμ΄λΈ μ±μ₯μκ°")
async def μΈλ¦¬(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="μΈλ¦¬λΌμ΄λΈ / Woolly Rhino")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894932836220928/806896756049707018/woollyrhino.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 2μΌ 9μκ° 52λΆ 13μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μμ μκ° : 3μκ° 58λΆ 5μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 5μκ° 47λΆ 13μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 23μκ° 8λΆ 53μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 1μΌ 4μκ° 56λΆ 6μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="λ°μ€λ‘μ¬μ°λ£¨μ€ μ±μ₯μκ°")
async def λ°μ€λ‘(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="λ°μ€λ‘μ¬μ°λ£¨μ€ / Basilosaurus")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894251073208330/806894585950765086/basilosaurus.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 4μΌ 19μκ° 44λΆ 26μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μμ μκ° : 7μκ° 56λΆ 11μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 11μκ° 34λΆ 26μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 1μΌ 22μκ° 17λΆ 46μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 2μΌ 9μκ° 52λΆ 13μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="λ©κ°λ‘λ μ±μ₯μκ°")
async def λ©κ°λ‘λ(ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="λ©κ°λ‘λ / Megalodon")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894251073208330/806894665034891294/megalodon.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 2μΌ 23μκ° 13λΆ 30μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μμ μκ° : 6μκ° 6λΆ 18μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 7μκ° 7λΆ 21μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 1μΌ 4μκ° 29λΆ 24μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 1μΌ 11μκ° 36λΆ 45μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="λ©κ°μλ‘  μ±μ₯μκ°")
async def λ©κ°μλ‘ (ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="λ©κ°μλ‘  / Megachelon")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806894251073208330/806894664548483103/megachelon.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 3μΌ 20μκ° 35λΆ 33μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° : 4μκ° 59λΆ 58μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 9μκ° 15λΆ 33μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 1μΌ 13μκ° 2λΆ 13μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 1μΌ 22μκ° 17λΆ 46μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids = [1065253502068207667], description="μλ₯΄μ  νλΉμ€ μ±μ₯μκ°")
async def μλ₯΄μ  (ctx):
    embed=discord.Embed(title=" ", description="κ³΅μ μ€νΌμ μ±μ₯μκ° ( x 1 )", color=0xb750fb)
    embed.set_author(name="μλ₯΄μ  νλΉμ€ / Argentavis")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/806893887162548244/806894008407949342/argentavis-1.png')
    embed.add_field(name="", value="", inline=True)
    embed.add_field(name="  μ±μ₯μκ°", value="", inline=False)
    embed.add_field(name="", value="μ΄ μ±μ₯μκ° : 2μΌ 6μκ° 27λΆ 58μ΄", inline=False)
    embed.add_field(name=" ", value="", inline=False)
    embed.add_field(name=" ", value="μ λΆνμκ° :2μκ° 56λΆ 27μ΄", inline=False)
    embed.add_field(name=" ", value="λ² μ΄λΉ : 5μκ° 26λΆ 47μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μ₯κΈ° : 21μκ° 47λΆ 11μ΄", inline=False)
    embed.add_field(name=" ", value="μ±μκΈ° : 1μΌ 3μκ° 13λΆ 59μ΄", inline=False)
    embed.add_field(name="", value="", inline=True)
    embed.set_footer(text="Made by WELCIKS")
    await ctx.respond(embed=embed)

bot.run(token)
