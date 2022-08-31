import asyncio
from email import message
from fileinput import filename
from operator import sub
import os
from tkinter import N
from tkinter.ttk import Notebook
from unicodedata import name
import discord
from discord.ext import commands
import time
from datetime import datetime
from datetime import date
from discord.ext.commands import CommandNotFound
from discord.ext.commands import MissingRequiredArgument
from os.path import exists
import discord
from aiohttp import ClientSession
from discord.ext import commands, tasks
import random


#vars
space_a = 2
commandlog = False
global cmdlog
now = datetime.now()
date = datetime.now().strftime("%Y_%m_%d-%I")
current_time = now.strftime("%H:%M")

roses = [
    "Roses are red, violets are blue, and I'll never ever, ever stop loving you.",
    "Roses are red, violets are blue, let's get together and make dreams come true.",
    "Roses are red, violets are blue, and I'll never be blue while I have you.",
    "Roses are red, violets are blue, lets cut the sweet talk, and go straight to bed.",
    "Roses are red, violets are blue, pucker up sweet lips I'm gonna kiss you!",
    "Roses are red, violets are blue, what colour flowers should I give you?",
    "Roses are red, violets are blue, wherever you are I wanna run to you!",
    "Roses are red, violets are blue, is it hot in here, or is it just you?",
    "Roses are red, violets are blue, vodka costs less than dinner for two.",
    "Roses are red, violets are blue, just like my eyes so let me love you!",
    "Roses are red, violets are blue, in a world of love, just we two.",
    "Roses are red, violets are blue, thank you, and spank you, for being so true!",
    "Roses are red, violets are blue, I wanted to write you a love poem but I only got that far..."
]


Logo = ("""
██████╗░██╗░█████╗░███╗░░██╗███╗░░██╗░█████╗░░██████╗░  ░██████╗███████╗██╗░░░░░███████╗██████╗░░█████╗░████████╗
██╔══██╗██║██╔══██╗████╗░██║████╗░██║██╔══██╗██╔════╝░  ██╔════╝██╔════╝██║░░░░░██╔════╝██╔══██╗██╔══██╗╚══██╔══╝
██████╔╝██║██║░░██║██╔██╗██║██╔██╗██║███████║██║░░██╗░  ╚█████╗░█████╗░░██║░░░░░█████╗░░██████╦╝██║░░██║░░░██║░░░
██╔══██╗██║██║░░██║██║╚████║██║╚████║██╔══██║██║░░╚██╗  ░╚═══██╗██╔══╝░░██║░░░░░██╔══╝░░██╔══██╗██║░░██║░░░██║░░░
██║░░██║██║╚█████╔╝██║░╚███║██║░╚███║██║░░██║╚██████╔╝  ██████╔╝███████╗███████╗██║░░░░░██████╦╝╚█████╔╝░░░██║░░░
╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░  ╚═════╝░╚══════╝╚══════╝╚═╝░░░░░╚═════╝░░╚════╝░░░░╚═╝░░░""")

Goodbye = """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░▄▄▀▀▀▀▀▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░▄▀░░░░░░░▀▄░░░░░░░░░░░░░░░░░░░░░░░░░░
░▄▀░░░▄▄░░░░▀▀▀▀▀▀▀▄▄▀▀▀▀▀▀▀▀▀▀▀▀▄▄░░░░
░█░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▄░░
░█░░░░██▄████▄░██▄░░░░▄██░▄████▄░░░░▀▄░
░█░░░░██▀░░▀██▄░██▄░░██▀░██▀░▄██░░░░░█░
░█░░░░██░░░░███░░█████▀░░██▄█▀▀░░░░░░█░
░█░░░░███▄▄███▀░░░▀██▀░░░▀██▄▄▄██░░░░█░
░▀▄░░░░▀▀▀▀▀▀░░░░░██▀░░░░░░▀▀▀▀▀░░░░░█░
░░▀▄░░░░░░░░░░░░░██▀░░░▄▄░░░░░░░░░▄▄▀░░
░░░░▀▀▀▀▀▀▀▀▀▄░░░▀▀░░░▄▀░▀▀▀▀▀▀▀▀▀░░░░░
░░░░░░░░░░░░░▀▄░░░░░░▄▀░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▀▀▀▀▀▀░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"""

#basic def
def space():
    for i in range(space_a):
        print()
        

#onstart
os.system('CLS')
print(Logo)
space()
# token = input("Please enter your token: ")


Bot_Prefix = ";"
bot = commands.Bot(command_prefix=Bot_Prefix, case_insensitive=True, self_bot=True, description = "Hello, This bot is made by GS_S.G#3838, Down here are the commands")

#on-ready
@bot.event
async def on_ready():
    os.system('CLS')
    print(Logo)
    space()
    print(f"Welcome {bot.user.name} Thank you for using Rionnag self-bot, do .help for list of commands")

#Errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        commandused = ctx.command
        await ctx.message.edit(content="Command not found")
        time.sleep(2)
        await ctx.messsage.delete()
    raise error

# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, MissingRequiredArgument):
#         commandused = ctx.command
#         await ctx.message.edit(content=f"Missing Required Argument from command ;{commandused} please check the commands info for more details")
#         time.sleep(2)
#         await ctx.messsage.delete()
#     raise error


#Main commands



@bot.command()
async def tcmdlog(ctx):
    global commandlog
    global cmdlog
    if commandlog == True:
        cmdlog.close()
        commandlog = False
        await ctx.message.edit(content="Disabled Command log")
        time.sleep(3)
        await ctx.message.delete()
    elif commandlog == False:
        cmdlog = open("Command log.txt", "w")
        commandlog = True
        await ctx.message.edit(content="Enabled Command log")
        time.sleep(3)
        await ctx.message.delete()

@bot.command()
async def killbot(ctx):
    user = ctx.author
    def check(m):
        return m.author.id == ctx.author.id
    await ctx.message.edit(content="Are you sure?")
    msg = await bot.wait_for('message', check=check)
    msg_content = msg.content.lower()
    if msg_content == ("yes"):
        await ctx.message.edit(content="Killing self bot in 5 sec")
        time.sleep(0.5)
        await ctx.message.edit(content="5")
        time.sleep(1)
        await ctx.message.edit(content="4")
        time.sleep(1)
        await ctx.message.edit(content="3")
        time.sleep(1)
        await ctx.message.edit(content="2")
        time.sleep(1)
        await ctx.message.edit(content="1")
        time.sleep(1)
        await ctx.message.edit(content=Goodbye)
        os.system('CLS')
        print(Goodbye)
        await ctx.message.delete()
        exit()
    else:
        await ctx.message.edit(content="No respose or invaild respose please try again")
        await ctx.message.delete()

@bot.command()
async def create(ctx, subcommand=None, arg1=None, arg2=None):
    ##channel
    guild = ctx.message.guild
    if subcommand == "channel":
        if arg1 == None:
            await ctx.message.edit(content="Please enter a channel name")
            return
        await guild.create_text_channel(arg1)
        await ctx.message.edit(content=f'Created channel called "{arg1}"')
        time.sleep(5)
        await ctx.message.delete()
    ##notes

    if subcommand == "note":
        if arg1 == None:
            await ctx.message.edit(content="Please enter a Note name and text")
            return
        filename = f"{arg1}.txt"
        if exists(filename):
            await ctx.message.edit(content=f"{arg1}, arl exist")
            return
        with open(filename, "w") as notefile:
            await ctx.message.edit(content=f"Created a note called '{arg1}'")
            time.sleep(5)
            await ctx.message.delete()
    if subcommand == "notenl":
        if arg1 == None or arg2 == None:
            await ctx.message.edit(content="Please enter a Note name and text")
            return
        filename = f"{arg1}.txt"
        if not exists(filename):
            await ctx.message.edit(content=f"the file '{arg1}' does not exist")
            return
        with open(filename, "w") as notefile:
            await ctx.message.edit(content=f'Created nl with text "{arg2}" ')
            if arg2 != None:
                notefile.write(f"'{arg2}' \n")
                time.sleep(5)
            await ctx.message.delete()


@bot.command()
async def freestyle(ctx):
    await ctx.channel.send(content='Yeah, yeah (we love you on face time)')
    time.sleep(2)
    await ctx.channel.send(content='Ahah, goofy on Uncle productions')
    time.sleep(2)
    await ctx.channel.send(content='Ey I know them five years late')
    time.sleep(2)
    await ctx.channel.send(content='You cant fuck with me')
    time.sleep(2)        
    await ctx.channel.send(content='Im on a different level')
    time.sleep(3)        
    await ctx.channel.send(content='Money so big')
    time.sleep(2)        
    await ctx.channel.send(content='Niggas think Im yeat')
    time.sleep(2)        
    await ctx.channel.send(content='Bitch you cant compete')
    time.sleep(2)        
    await ctx.channel.send(content='Lil hoe')
    time.sleep(2)        
    await ctx.channel.send(content='Get on your knees and lick the cheese')
    time.sleep(2)        
    await ctx.channel.send(content='Im fina get on your ass')
    time.sleep(2)        
    await ctx.channel.send(content='You could call me pair of jeans')
    time.sleep(2)        
    await ctx.channel.send(content='That girl she came and sucked my dick')
    time.sleep(2)        
    await ctx.channel.send(content='And she did it hella mean')
    time.sleep(2)        
    await ctx.channel.send(content='Yeah, they call me Quandale')
    time.sleep(3)        
    await ctx.channel.send(content='Got to get to the green')
    time.sleep(2)        
    await ctx.channel.send(content='Im not talking bout no Kale')
    time.sleep(2)        
    await ctx.channel.send(content='Had to kick a lil bitch out')
    time.sleep(2)        
    await ctx.channel.send(content='Man, I was just in jail')
    time.sleep(2)        
    await ctx.channel.send(content='I was opening up mail')
    time.sleep(2)        
    await ctx.channel.send(content='Quandarious tried to diss me and his stupid ass failed')
    time.sleep(2)        
    await ctx.channel.send(content='Got these hoes mad')
    time.sleep(2)        
    await ctx.channel.send(content='Cause Im getting racks put a Hunnid on the dash')
    time.sleep(2)        
    await ctx.channel.send(content='Bitch yo breath stink')
    time.sleep(3)        
    await ctx.channel.send(content='Please go put on a fucking mask')
    time.sleep(2)        
    await ctx.channel.send(content="*She said pass the weed*")
    time.sleep(2)        
    await ctx.channel.send(content='Bitch, I dont like to pass the gas')
    time.sleep(2)        
    await ctx.channel.send(content='*Blowing bubbles, blowing Zaza*')
    time.sleep(2)
    await ctx.channel.send(content='She got big all titties')
    time.sleep(2)        
    await ctx.channel.send(content='I said goo, goo, goo, gah, gah')
    time.sleep(2)        
    await ctx.channel.send(content='In the zoo, monkey ass niggas')
    time.sleep(2)        
    await ctx.channel.send(content='Ooh, ooh, ooh, ah, ah')
    time.sleep(2)        
    await ctx.channel.send(content='Stop playing with me')
    time.sleep(2)        
    await ctx.channel.send(content='When the money talking')
    time.sleep(10)
    await ctx.channel.send(content='Cover by GS selfbot')
    time.sleep(0.5)
    await ctx.channel.send('Singing done')  

# @bot.command(pass_content=True)

# async def dadjoke(self, ctx):
#     self.bot = bot
#     url = "https://dad-jokes.p.rapidapi.com/random/joke"
#     headers = {
#         'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
#         'x-rapidapi-key': self.bot.joke_api_key
#     }

#     async with ClientSession() as session:
#         async with session.get(url, headers=headers) as response:
#             r = await response.json()
#             r = r["body"][0]
#             await ctx.channel.send(f"**{r['setup']}**\n\n||{r['punchline']}||")


# @bot.command()
# async def opstatus(ctx, status=None):
#     url1='https://www.youtube.com/watch?v=2jCQvgY1GaE'
#     if status == None:
#         await ctx.message.edit(content='Please enter a bool')
#     elif status == "false":
#         await ctx.message.edit(content='Disabled')
#     elif status == "true":
#         await ctx.message.edit(content='Enabled')
#         while opstatus == True:    
#             await bot.change_presence(activity=discord.Streaming(name="Please go put on a fucking mask", url=url1))
#             time.sleep(2)
#             await bot.change_presence(activity=discord.Streaming(name="She said pass the weed", url=url1))
#             time.sleep(2)
#             await bot.change_presence(activity=discord.Streaming(name="Bitch, I don't like to pass the gas", url=url1))
#             time.sleep(2)
#             await bot.change_presence(activity=discord.Streaming(name="Blowing bubbles, blowing Zaza", url=url1))
#             time.sleep(2)
#             await bot.change_presence(activity=discord.Streaming(name="She got big all titties", url=url1))
#             time.sleep(2)
#             await bot.change_presence(activity=discord.Streaming(name="I said goo, goo, goo, gah, gah", url=url1))
#             time.sleep(2)
#             await bot.change_presence(activity=discord.Streaming(name="In the zoo, monkey ass niggas", url=url1))
#             time.sleep(2)
#             await bot.change_presence(activity=discord.Streaming(name="Ooh, ooh, ooh, ah, ah", url=url1))
#             time.sleep(2)
#             await bot.change_presence(activity=discord.Streaming(name="Stop playing with me", url=url1))
#             time.sleep(2)
#             await bot.change_presence(activity=discord.Streaming(name="When the money talking", url=url1))
#             time.sleep(5)


@bot.command(pass_context=True)
async def clean(ctx, limit: int):
        dm = discord.DMChannel
        await ctx.authordm.purge(limit=limit)
        await ctx.send('Cleared by {}'.format(ctx.author.mention))
        await ctx.message.delete()

#commandslog
# @bot.event
# async def on_command(ctx):
#     if commandlog == True:
#         serverused = ctx.guild.name
#         commandused = ctx.command
#         cmdlog.write(f';{commandused} from {serverused} at {current_time} \n')
#     elif commandlog == False:
#         return

#presence changeing
@bot.command()
async def pr(ctx, presence=None, arg1 = None, arg2 = None, arg3 = None):
    if presence == None:
        await ctx.message.edit(content='Please enter what presence you want to choose')
        time.sleep(5)
        await ctx.message.delete()
        return
    if presence == "game":
        if arg1 == None:
            await ctx.message.edit(content='Enter what game you want')
            time.sleep
            await ctx.message.delete()
            return
        await bot.change_presence(activity=discord.Game(name=arg1))
        await ctx.message.edit(content=f'Setted to playing {arg1}')
        time.sleep(5)
        await ctx.message.delete()
    if presence == "streaming":
        if arg1 == None and arg2 == None:
            await ctx.message.edit(content='Enter whats you name of stream and url')
            time.sleep
            await ctx.message.delete()
            return
        await bot.change_presence(activity=discord.Streaming(name=arg1, url=arg2))
        await ctx.message.edit(content=f'Setted to Streaming {arg1} and URL to {arg2}')
        time.sleep(5)
        await ctx.message.delete()
    if presence == "listening":
        if arg1 == None:
            await ctx.message.edit(content='Enter what song you are hearing to')
            time.sleep
            await ctx.message.delete()
            return
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=arg1))
        await ctx.message.edit(content=f'Setted to listening {arg1}')
        time.sleep(5)
        await ctx.message.delete()
    if presence == "watching":
        if arg1 == None:
            await ctx.message.edit(content='Enter what your watching')
            time.sleep
            await ctx.message.delete()
            return
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=arg1))
        await ctx.message.edit(content=f'Setted to watching {arg1}')
        time.sleep(5)
        await ctx.message.delete()
    if presence == "help":
        await ctx.message.edit(content="""
```
To use this command please follow this command with same agr, down below:
;pr [Activity] [Action]

There are 4 presence to keep:
    1. game, any
    2. steaming, URL
    3. listening, any
    4. watching, any
every this after , on that list is a req item to use in the command
        ```""")
        time.sleep(60)
        await ctx.message.delete()




@bot.command()
async def userinfo(ctx, *, user: discord.User = None): # b'\xfc'
    if not ctx.guild:
        if user is None:
            user = ctx.author      
        date_format = "%a, %d %b %Y %I:%M %p"
        await ctx.message.edit(content=f"""
        User: {user}\npfp: {user.avatar_url}\nRegistered, {user.created_at.strftime(date_format)}\n""")
    elif ctx.guild:
        if user is None:
            user = ctx.author     
        date_format = "%a, %d %b %Y %I:%M %p"
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        await ctx.message.edit(content=f"""
        User: {user}\npfp: {user.avatar_url}\nRegistered, {user.created_at.strftime(date_format)}\nJoint server: {user.joined_at.strftime(date_format)}\nJoin position: {members.index(user)+1}""")
           




#Roasting commands
@bot.command()
async def lic(ctx):    
    await ctx.message.edit(content="https://cdn.discordapp.com/attachments/661472973815021568/986884249825189908/meme_lic.jpg")

@bot.command()
async def fr(ctx):    
    await ctx.message.edit(content="https://cdn.discordapp.com/attachments/923464196987953194/986888229359845396/fr-ong.mp4")

@bot.command()
async def whereurlic(ctx):   
    await ctx.message.edit(content="https://cdn.discordapp.com/attachments/934803218398081087/986889791272517702/whereyomemlic.mov")

@bot.command()
async def iop(ctx):   
    await ctx.message.edit(content="https://cdn.discordapp.com/attachments/934803218398081087/986889790962143242/trim.FE88ACC8-E64A-4870-A645-D5064B2851B2.mov")

@bot.command()
async def switch(ctx):   
    await ctx.message.edit(content="https://cdn.discordapp.com/attachments/934803218398081087/986889790651793428/reverse.png")

@bot.command()
async def nou(ctx):   
    await ctx.message.edit(content="https://cdn.discordapp.com/attachments/934803218398081087/986889790345584711/nou.png")


@bot.command()
async def idc(ctx):   
    await ctx.message.edit(content="https://cdn.discordapp.com/attachments/934803218398081087/986889789854867456/Nobody_Cares_Nigga.mp4")


@bot.command()
async def mhm(ctx):    
    await ctx.message.edit(content="https://cdn.discordapp.com/attachments/934803218398081087/986889789338947584/intresting.mov")

@bot.command()
async def giga(ctx):   
    await ctx.message.edit(content="https://cdn.discordapp.com/attachments/934803218398081087/986889788965670952/iamgiga.mp4")

@bot.command()
async def iwin(ctx):   
    await ctx.message.edit(content="https://cdn.discordapp.com/attachments/934803218398081087/986889788483330058/I_win_skull.mp4")

@bot.command()
async def hmm(ctx):   
    await ctx.message.edit(content="https://cdn.discordapp.com/attachments/934803218398081087/986889788139401276/dotdotdot.mov")

@bot.command()
async def mf(ctx): 
    await ctx.message.edit(content="https://cdn.discordapp.com/attachments/934803218398081087/986889787686395945/cat-1.mp4")

@bot.command()
async def icome(ctx): 
    await ctx.message.edit(content="https://cdn.discordapp.com/attachments/934803218398081087/986891598086426624/lv_0_20220304123200.mp4")

@bot.command()
async def lgbt(ctx):
    await ctx.message.edit(content="https://cdn.discordapp.com/attachments/934803218398081087/986891895663898644/c76d70653cf941f0981c6afd36065e83.mp4")

@bot.command()
async def music(ctx):
    await ctx.message.edit(content="https://cdn.discordapp.com/attachments/934803218398081087/986892091114258452/C418__Aria_Math.mp4")

@bot.command()
async def based(ctx):
    await ctx.message.edit(content="https://cdn.discordapp.com/attachments/934803218398081087/986892469796995082/nogf.mp4")

@bot.command()
async def lgbt1(ctx):
    await ctx.message.edit(content="https://cdn.discordapp.com/attachments/934803218398081087/986892478852509706/Snaptik_6993657046532967686_tiktok.mp4")

@bot.command()
async def cringe(ctx):
    await ctx.message.edit(content='https://cdn.discordapp.com/attachments/661472973815021568/990437848429772840/cringe.mp4')

@bot.command()
async def lie(ctx):
    await ctx.message.edit(content='https://cdn.discordapp.com/attachments/990284855931707442/992770836673089596/videoplayback.mp4')

@bot.command()
async def lgbt3(ctx):
    await ctx.message.edit(content='https://media.discordapp.net/attachments/945315442216554536/993903994147721216/trim.F94DF0DE-B45B-461F-8348-49824A8A6022.mov')

@bot.command()
async def lgbt4(ctx):
    await ctx.message.edit(content='https://cdn.discordapp.com/attachments/997110512884125807/998189542978891796/Reject_modernity_Embrace_Wehrmacht.mp4')



@bot.command()
async def shr(ctx):
    await ctx.message.edit(content="¯\_(ツ)_/¯")

@bot.command()
async def intro(ctx):
    await ctx.message.edit(content="""
Hey, my name is **GS**, im 14 years old, and this is my introduce message.
────────────────────────────────────────────────────────────────────────────
**Main:**
    He/Him
    Homophobic (dont ask why)
    Single
    Call me "GS" do not call me by my real name, atleast in the public.  
────────────────────────────────────────────────────────────────────────────
**My Hobbies:**
    I love too code Discord bots with Python, JavaScript, Java, Rust, RobloxLua.
    I also love to play Minecraft, Roblox (scripting).
    I hear to Phonk music (very op).
    I interested in hacking, but still new (I can doxx you hehe).
────────────────────────────────────────────────────────────────────────────
**Other:**
	If your interested in having your own Self bot or Bot, feel free to ask me, I dont got ideas so maybe yours can help me know about Discord API.
	Yes, this message is automated with my self bot :sunglasses:"""
)

@bot.command()
async def flirt(ctx):
    await ctx.message.edit(content=random.choice(roses))
    
#token
bot.run("NjYxMjQ5MjQ4NzQ2MTQzNzQ0.GD3IAO.lag4X2GGLyGJN1YzOkBB5LARVKOQ-ya3JLgV-w", bot=False)




