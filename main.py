import discord
import PIL


from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont

TOKEN = 'NzQ5ODkxMTg1ODY2MzA5NjYy.X0yklw.ol1hQfz6_KfPE-FSndHswcvt-Mc'
client = commands.Bot(command_prefix="bhaiya ")


@client.event
async def on_ready():
    print('Bot is ready.')


@client.event
async def on_member_join(member):
    print(f'{member} has joined server.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left server.')


@client.command()
async def helpme(ctx):
    await ctx.send("**Send:** \n `ayodhya` - if you want to pilgrimage \n `poop` `argument` - for poop :poop:"
                   "\n `laugh` `argument` - for lafing :rofl: \n `hello` - for hello :grin: \n `gay` `argument` - for gæ :rainbow: \n `bjp` - for epic bjp reaction :crown:")


@client.command()
async def ayodhya(ctx):
    print(f'bruh {ctx.message.author} wants to go to Ayodhya from {ctx.guild}.')
    await ctx.send(f"**Booking two tickets to Ayodhya** for me and {ctx.message.author.mention}...")

    # get an image
    base = Image.open("burh.jpg").convert("RGBA")

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

    # get a font
    fnt = ImageFont.truetype("./times.ttf", 30)

    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, full opacity
    d.text((64, 287), f"{ctx.message.author}", font=fnt, fill="black")

    out = Image.alpha_composite(base, txt)
    out.save('burh2.png')
    await ctx.send(file=discord.File('burh2.png'))


@client.command()
async def poop(ctx, arg):
    print(f'{arg} is poop by {ctx.message.author} in {ctx.guild}')
    await ctx.send(f":poop::poop::poop:||{arg} is poop||:poop::poop::poop:")


@client.command()
async def gay(ctx, arg):
    print(f'{arg} is gay by {ctx.message.author} in {ctx.guild}')
    await ctx.send(f":rainbow::rainbow_flag::rainbow:||{arg} GAE||:rainbow::rainbow_flag::rainbow:")


@client.command()
async def laugh(ctx, arg):
    print(f'{ctx.message.author} is laufing in {ctx.guild}')
    await ctx.send(f":rofl::rofl::rofl::rofl: **Call me rinkiya ke papa cuz I do be laughing at {arg}'s silly ass** :flushed::rofl::rofl:")


@client.command()
async def bjp(ctx):
    print(f'{ctx.message.author} is bjp in {ctx.guild}')
    await ctx.send(f":flag_in: WELCOME to **BJP** king {ctx.message.author.mention} :crown:")

@client.command()
async def hello(ctx):
    print(f'{ctx.message.author} is telling hi in {ctx.guild}')
    await ctx.send(f":flag_in: SatSriAkal {ctx.message.author.mention} ji :grin::grin::grin::bouquet:")
client.run(TOKEN)
