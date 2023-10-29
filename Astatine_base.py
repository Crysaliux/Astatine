import discord
from discord.ext import commands
import json
import requests
import sqlite3
import random
import peewee
from peewee import *
from random import choice

intents = discord.Intents.default()
#intents.presences = True
intents.members = True

bot = commands.Bot(command_prefix='A.', intents=intents)
bot.remove_command('help')

e_db = MySQLDatabase('railway', user='root', password='hgqkthb07raKcFVRECl3',
                         host='containers-us-west-111.railway.app', port=6020)

class Money(Model):
    guild_id = BigIntegerField()
    user_id = BigIntegerField()
    amount = BigIntegerField()

    class Meta:
        database = e_db

class Bank(Model):
    guild_id = BigIntegerField()
    user_id = BigIntegerField()
    amount = BigIntegerField()

    class Meta:
        database = e_db

class Shop(Model):
    guild_id = BigIntegerField()
    item = CharField(max_length=20)
    cost = BigIntegerField()
    extra_roles = BigIntegerField()

    class Meta:
        database = e_db

e_db.connect()
e_db.create_tables([Money, Bank, Shop])

u_db = MySQLDatabase('railway', user='root', password='fFWAwPLFLR7SN2O71vlp',
                         host='containers-us-west-86.railway.app', port=7405)

class Warns(Model):
    guild_id = BigIntegerField()
    user_id = BigIntegerField()
    warn = CharField(max_length=200)
    index = BigIntegerField()

    class Meta:
        database = u_db

class Language(Model):
    guild_id = BigIntegerField()
    lang = CharField(max_length=20)

    class Meta:
        database = u_db

class Join(Model):
    guild_id = BigIntegerField()
    role_id = BigIntegerField()
    settings = CharField(max_length=20)

    class Meta:
        database = u_db

class Mute(Model):
    guild_id = BigIntegerField()
    role_id = BigIntegerField()
    settings = CharField(max_length=20)

    class Meta:
        database = u_db

class Ticket(Model):
    guild_id = BigIntegerField()
    index = BigIntegerField()

    class Meta:
        database = u_db

class TicketRole(Model):
    guild_id = BigIntegerField()
    role_id = BigIntegerField()

    class Meta:
        database = u_db

class Logs(Model):
    guild_id = BigIntegerField()
    channel_id = BigIntegerField()
    settings = CharField(max_length=20)

    class Meta:
        database = u_db

u_db.connect()
u_db.create_tables([Warns, Language, Join, Mute, Ticket, TicketRole, Logs])

cogs_list = [
    'Au_econ',
    'Au_mod',
    'Au_util',
    'Au_info',
    'Au_fun'
]
for cog in cogs_list:
    bot.load_extension(f'{cog}')

community_rights = 'Mester Satellite, © 2023 All rights reserved'
creator_url = 'https://cdn.discordapp.com/avatars/830486806478848040/cb206fa6511033c04a91016af44a6c65.png?size=1024'
game = discord.Game("Aurix community🌟")

@bot.event
async def on_application_command_error(ctx: discord.ApplicationContext, error: discord.DiscordException):
    if isinstance(error, commands.CommandNotFound):
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is not None:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    em = discord.Embed(title="⚠Несуществующая команда⚠",
                                       description='Данной команды не существует.',
                                       color=0xFFFF00)
                    await ctx.send(embed=em)
                else:
                    em = discord.Embed(title="⚠Non-existing command⚠",
                                       description='Command does not exist.',
                                       color=0xFFFF00)
                    await ctx.send(embed=em)
        else:
            em = discord.Embed(title="⚠Non-existing command⚠",
                               description='Command does not exist.',
                               color=0xFFFF00)
            await ctx.send(embed=em)

    elif isinstance(error, commands.MissingPermissions):
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is not None:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    em = discord.Embed(title="⚠Недостаточно прав⚠",
                                       description='У вас недостаточно прав на выполнение этой команды.',
                                       color=0x39d0d6)
                    await ctx.send(embed=em)
                else:
                    em = discord.Embed(title="⚠Not enough permissions⚠",
                                       description='You dont have enough permissions to execute this command.',
                                       color=0x39d0d6)
                    await ctx.send(embed=em)
        else:
            em = discord.Embed(title="⚠Not enough permissions⚠",
                               description='You dont have enough permissions to execute this command.',
                               color=0x39d0d6)
            await ctx.send(embed=em)

    elif isinstance(error, commands.CommandOnCooldown):
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is not None:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    em = discord.Embed(title="⚠Данная команда на задержке⚠",
                                       description=f"Попробуйте снова через {error.retry_after:.2f}s.",
                                       color=0x39d0d6)
                    await ctx.send(embed=em)
                else:
                    em = discord.Embed(title="⚠Command is on cooldown⚠",
                                       description=f"Try again in {error.retry_after:.2f}s.",
                                       color=0x39d0d6)
                    await ctx.send(embed=em)
        else:
            em = discord.Embed(title="⚠Command is on cooldown⚠",
                               description=f"Try again in {error.retry_after:.2f}s.",
                               color=0x39d0d6)
            await ctx.send(embed=em)

    else:
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is not None:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    em = discord.Embed(title="⚠Недостаточно прав⚠",
                                       description='У бота недостаточно прав на выполнение этой команды.',
                                       color=0x39d0d6)
                    await ctx.send(embed=em)
                else:
                    em = discord.Embed(title="⚠Not enough permissions⚠",
                                       description='Bot doesnt have enough permissions to execute this command.',
                                       color=0x39d0d6)
                    await ctx.send(embed=em)
        else:
            em = discord.Embed(title="⚠Not enough permissions⚠",
                               description='Bot doesnt have enough permissions to execute this command.',
                               color=0x39d0d6)
            await ctx.send(embed=em)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=game)
    for guild in bot.guilds:
        get_guild = Money.get_or_none(guild_id=guild.id)
        if get_guild is not None:
            pass
        else:
            for member in guild.members:
                account = Money.create(user_id=member.id, amount='0', guild_id=guild.id)

@bot.event
async def on_member_join(member):
    user = Money.get_or_none(user_id=member.id, guild_id=member.guild.id)
    if user is not None:
        pass

    else:
        account = Money.create(user_id=member.id, amount='0', guild_id=member.guild.id)
    getjoin = Join.get_or_none(guild_id=member.guild.id)
    if getjoin is None:
        pass
    else:
        for join in Join.select().where(Join.guild_id == member.guild.id):
            if join.settings == 'off':
                pass
            else:
                role = member.guild.get_role(join.role_id)
                await member.add_roles(role)
    getlogs = Logs.get_or_none(guild_id=member.guild.id)
    if getlogs is None:
        pass
    else:
        for logs in Logs.select().where(Logs.guild_id == member.guild.id):
            if logs.settings == 'on':
                channel = bot.get_channel(logs.channel_id)
                getlang = Language.get_or_none(guild_id=member.guild.id)
                if getlang is not None:
                    for language in Language.select().where(Language.guild_id == member.guild.id):
                        if language.lang == "ru":
                            join_emb = discord.Embed(title='📋Новый пользователь присоединился', colour=0x39d0d6)
                            join_emb.add_field(name='📁Имя:', value=member.name, inline=False)
                            join_emb.add_field(name='📁Айди:', value=member.id, inline=False)
                            join_emb.add_field(name='📁Аккаунт был создан:',
                                               value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                                               inline=False)
                            await channel.send(embed=join_emb)
                        else:
                            join_emb = discord.Embed(title='📋New user joined', colour=0x39d0d6)
                            join_emb.add_field(name='📁Username:', value=member.name, inline=False)
                            join_emb.add_field(name='📁User ID:', value=member.id, inline=False)
                            join_emb.add_field(name='📁Account created:',
                                               value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                                               inline=False)
                            await channel.send(embed=join_emb)
                else:
                    join_emb = discord.Embed(title='📋New user joined', colour=0x39d0d6)
                    join_emb.add_field(name='📁Username:', value=member.name, inline=False)
                    join_emb.add_field(name='📁User ID:', value=member.id, inline=False)
                    join_emb.add_field(name='📁Account created:',
                                       value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
                    await channel.send(embed=join_emb)
            else:
                pass

@bot.event
async def on_guild_join(guild):
    channel = bot.get_channel(1034869012074606632)
    await channel.send(f'Bot was added to a new server, called ```{guild}```({guild.id})', file=discord.File("on_guild_join.gif"))
    for member in guild.members:
        user = Money.get_or_none(user_id=member.id, guild_id=guild.id)
        if user is not None:
            pass

        else:
            account = Money.create(user_id=member.id, amount='0', guild_id=guild.id)

@bot.event
async def on_member_remove(member):
    user = Money.get_or_none(user_id=member.id, guild_id=member.guild.id)
    if user is not None:
        delete = Money.get(Money.user_id == member.id, Money.guild_id == member.guild.id)
        delete.delete_instance()
    else:
        pass
    getlogs = Logs.get_or_none(guild_id=member.guild.id)
    if getlogs is None:
        pass
    else:
        for logs in Logs.select().where(Logs.guild_id == member.guild.id):
            if logs.settings == 'on':
                channel = bot.get_channel(logs.channel_id)
                getlang = Language.get_or_none(guild_id=member.guild.id)
                if getlang is not None:
                    for language in Language.select().where(Language.guild_id == member.guild.id):
                        if language.lang == "ru":
                            join_emb = discord.Embed(title='📋Пользователь покинул сервер', colour=0x39d0d6)
                            join_emb.add_field(name='📁Имя:', value=member.name, inline=False)
                            join_emb.add_field(name='📁Айди:', value=member.id, inline=False)
                            join_emb.add_field(name='📁Аккаунт был создан:',
                                               value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                                               inline=False)
                            await channel.send(embed=join_emb)
                        else:
                            join_emb = discord.Embed(title='📋User leaved server', colour=0x39d0d6)
                            join_emb.add_field(name='📁Username:', value=member.name, inline=False)
                            join_emb.add_field(name='📁User ID:', value=member.id, inline=False)
                            join_emb.add_field(name='📁Account created:',
                                               value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                                               inline=False)
                            await channel.send(embed=join_emb)
                else:
                    join_emb = discord.Embed(title='📋User leaved server', colour=0x39d0d6)
                    join_emb.add_field(name='📁Username:', value=member.name, inline=False)
                    join_emb.add_field(name='📁User ID:', value=member.id, inline=False)
                    join_emb.add_field(name='📁Account created:',
                                       value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
                    await channel.send(embed=join_emb)
            else:
                pass

@bot.event
async def on_member_update(before, after):
    if before.roles != after.roles:
        getlogs = Logs.get_or_none(guild_id=after.guild.id)
        if getlogs is None:
            pass
        else:
            for logs in Logs.select().where(Logs.guild_id == after.guild.id):
                if logs.settings == 'on':
                    channel = bot.get_channel(logs.channel_id)
                    getlang = Language.get_or_none(guild_id=after.guild.id)
                    if getlang is not None:
                        for language in Language.select().where(Language.guild_id == after.guild.id):
                            if language.lang == "ru":
                                role_emb = discord.Embed(title='📋Пользователь изменил роли', colour=0x39d0d6)
                                role_emb.add_field(name='📁Имя:', value=after.name, inline=False)
                                role_emb.add_field(name='📁Айди:', value=after.id, inline=False)
                                role_emb.add_field(name='📁Аккаунт был создан:',
                                                   value=after.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                                                   inline=False)
                                role_emb.add_field(name='Новые роли:', value=", ".join([r.mention for r in after.roles]),
                                                   inline=False)
                                await channel.send(embed=role_emb)
                            else:
                                role_emb = discord.Embed(title='📋User changed roles', colour=0x39d0d6)
                                role_emb.add_field(name='📁Username:', value=after.name, inline=False)
                                role_emb.add_field(name='📁User ID:', value=after.id, inline=False)
                                role_emb.add_field(name='📁Account created:',
                                                   value=after.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                                                   inline=False)
                                role_emb.add_field(name='New roles:', value=", ".join([r.mention for r in after.roles]),
                                                   inline=False)
                                await channel.send(embed=role_emb)
                    else:
                        role_emb = discord.Embed(title='📋User changed roles', colour=0x39d0d6)
                        role_emb.add_field(name='📁Username:', value=after.name, inline=False)
                        role_emb.add_field(name='📁User ID:', value=after.id, inline=False)
                        role_emb.add_field(name='📁Account created:',
                                           value=after.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
                        role_emb.add_field(name='New roles:', value=", ".join([r.mention for r in after.roles]),
                                           inline=False)
                        await channel.send(embed=role_emb)
                else:
                    pass

@bot.event
async def on_guild_remove(guild):
    leave = Money.get_or_none(guild_id=guild.id)
    if leave is not None:
        delete = Money.get(Money.guild_id == guild.id)
        delete.delete_instance()
    else:
        pass

@bot.slash_command(name = "ping", description = "Replies with pong!")
async def ping(ctx):
    getlang = Language.get_or_none(guild_id=ctx.guild.id)
    if getlang is not None:
        for language in Language.select().where(Language.guild_id == ctx.guild.id):
            if language.lang == "ru":
                money_emb = discord.Embed(
                    title=f'✔Понг! {bot.latency}',
                    color=0x39d0d6)
                await ctx.respond(embed=money_emb)
            else:
                money_emb = discord.Embed(
                    title=f'✔Pong! {bot.latency}',
                    color=0x39d0d6)
                await ctx.respond(embed=money_emb)
    else:
        money_emb = discord.Embed(
            title=f'✔Pong! {bot.latency}',
            color=0x39d0d6)
        await ctx.respond(embed=money_emb)

@bot.slash_command(name = "s_link", description = "Only creator can execute this command")
async def s_link(ctx, channel: int, id):
    if ctx.author.id != 830486806478848040:
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is not None:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    s_emb = discord.Embed(
                        title='Эту команду может использовать только создатель',
                        color=0x39d0d6)
                    await ctx.respond(embed=s_emb)
                else:
                    s_emb = discord.Embed(
                        title='Only creator has access to this command',
                        color=0x39d0d6)
                    await ctx.respond(embed=s_emb)
        else:
            s_emb = discord.Embed(
                title='Only creator has access to this command',
                color=0x39d0d6)
            await ctx.respond(embed=s_emb)
    else:
        link_emb = discord.Embed(
            title="Done! The invite should be sent soon",
            color=0x39d0d6)
        await ctx.respond(embed=link_emb)
        guild_id = int(id)
        guild = bot.get_guild(guild_id)
        channel = guild.channels[channel]
        invitelink = await channel.create_invite(max_uses=1)
        await ctx.author.send(invitelink)

class Enform(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="How did you find us?", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="Have you ever user our bot?", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="Have you read our rules?", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="What are your hobbies?", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        channel = bot.get_channel(1080188253967233084)
        embed = discord.Embed(title=f"New user has joined.")
        embed.add_field(name="How did you find us?", value=self.children[0].value)
        embed.add_field(name="Have you ever user our bot?", value=self.children[1].value)
        embed.add_field(name="Have you read our rules?", value=self.children[2].value)
        embed.add_field(name="What are your hobbies?", value=self.children[3].value)
        await interaction.response.send_message('Your verification form was recieved', ephemeral=True)
        await channel.send('<@&1080191959651602493>')
        await channel.send(embeds=[embed])

class Ruform(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Как вы нашли наш сервер?", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="Вы когда либо использовали нашего бота?", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="Вы ознакомились с правилами?", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="Ваши увлечения?", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        channel = bot.get_channel(1080188253967233084)
        embed = discord.Embed(title=f"New user has joined.")
        embed.add_field(name="Как вы нашли наш сервер?", value=self.children[0].value)
        embed.add_field(name="Вы когда либо использовали нашего бота?", value=self.children[1].value)
        embed.add_field(name="Вы ознакомились с правилами?", value=self.children[2].value)
        embed.add_field(name="Ваши увлечения?", value=self.children[3].value)
        await interaction.response.send_message('Ваша верификационная форма была получена', ephemeral=True)
        await channel.send('<@&1080191959651602493>')
        await channel.send(embeds=[embed])

class EnButton(discord.ui.View):
    @discord.ui.button(label="Verify")
    async def button_callback(self, button, interaction):
        await interaction.response.send_modal(Enform(title="Verification form"))

class RuButton(discord.ui.View):
    @discord.ui.button(label="Верификация")
    async def button_callback(self, button, interaction):
        await interaction.response.send_modal(Ruform(title="Форма верификации"))

@bot.slash_command(name = "verify", description = "Only for Aurix community")
async def verify(ctx, language: discord.Option(str, choices=[discord.OptionChoice(name="ru", value="ru", name_localizations=None), discord.OptionChoice(name="en", value="en", name_localizations=None)])):
    if ctx.guild != bot.get_guild(1018143149383757946):
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is not None:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    ver_emb = discord.Embed(
                        title=f'⚠Эта команда доступна только для сервера Aurix community⚠',
                        color=0x39d0d6)
                    await ctx.respond(embed=ver_emb)
                else:
                    ver_emb = discord.Embed(
                        title=f'⚠This command is only available for the Aurix community server⚠',
                        color=0x39d0d6)
                    await ctx.respond(embed=ver_emb)
        else:
            ver_emb = discord.Embed(
                title=f'⚠This command is only available for the Aurix community server⚠',
                color=0x39d0d6)
            await ctx.respond(embed=ver_emb)
    else:
        if ctx.channel != bot.get_channel(1018144056594931712):
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is not None:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == "ru":
                        ver_emb = discord.Embed(
                            title=f'⚠Эта команда доступна только на канале верификации⚠',
                            color=0x39d0d6)
                        await ctx.respond(embed=ver_emb)
                    else:
                        ver_emb = discord.Embed(
                            title=f'⚠This command is only available on the verification channel⚠',
                            color=0x39d0d6)
                        await ctx.respond(embed=ver_emb)
            else:
                ver_emb = discord.Embed(
                    title=f'⚠This command is only available on the verification channel⚠',
                    color=0x39d0d6)
                await ctx.respond(embed=ver_emb)
        else:
            channel = bot.get_channel(1080188253967233084)
            if language == 'ru':
                await ctx.respond(view=RuButton(), ephemeral=True)
            elif language == 'en':
                await ctx.respond(view=EnButton(), ephemeral=True)
            await channel.send(f'**New user created a form!** ```User id: [{ctx.author.id}], user name: [{ctx.author}]```')

@bot.slash_command(name = "accept", description = "Only for Aurix community")
async def accept(ctx, user: discord.Member):
    if ctx.guild != bot.get_guild(1018143149383757946):
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is not None:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    ver_emb = discord.Embed(
                        title=f'⚠Эта команда доступна только для сервера Aurix community⚠',
                        color=0x39d0d6)
                    await ctx.respond(embed=ver_emb)
                else:
                    ver_emb = discord.Embed(
                        title=f'⚠This command is only available for the Aurix community server⚠',
                        color=0x39d0d6)
                    await ctx.respond(embed=ver_emb)
        else:
            ver_emb = discord.Embed(
                title=f'⚠This command is only available for the Aurix community server⚠',
                color=0x39d0d6)
            await ctx.respond(embed=ver_emb)
    else:
        if ctx.channel != bot.get_channel(1080188253967233084):
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is not None:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == "ru":
                        ver_emb = discord.Embed(
                            title=f'⚠Эта команда доступна только на канале верификации⚠',
                            color=0x39d0d6)
                        await ctx.respond(embed=ver_emb)
                    else:
                        ver_emb = discord.Embed(
                            title=f'⚠This command is only available on the verification channel⚠',
                            color=0x39d0d6)
                        await ctx.respond(embed=ver_emb)
            else:
                ver_emb = discord.Embed(
                    title=f'⚠This command is only available on the verification channel⚠',
                    color=0x39d0d6)
                await ctx.respond(embed=ver_emb)
        else:
            await user.add_roles(ctx.guild.get_role(1018202889606398034))
            await user.add_roles(ctx.guild.get_role(1088797142493167627))
            await user.add_roles(ctx.guild.get_role(1088796557907857528))
            await ctx.respond(f'**Successfully accepted user {user}!**')

@bot.slash_command(name = "decline", description = "Only for Aurix community")
async def decline(ctx, user: discord.Member, *, reason):
    if ctx.guild != bot.get_guild(1018143149383757946):
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is not None:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    ver_emb = discord.Embed(
                        title=f'⚠Эта команда доступна только для сервера Aurix community⚠',
                        color=0x39d0d6)
                    await ctx.respond(embed=ver_emb)
                else:
                    ver_emb = discord.Embed(
                        title=f'⚠This command is only available for the Aurix community server⚠',
                        color=0x39d0d6)
                    await ctx.respond(embed=ver_emb)
        else:
            ver_emb = discord.Embed(
                title=f'⚠This command is only available for the Aurix community server⚠',
                color=0x39d0d6)
            await ctx.respond(embed=ver_emb)
    else:
        if ctx.channel != bot.get_channel(1080188253967233084):
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is not None:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == "ru":
                        ver_emb = discord.Embed(
                            title=f'⚠Эта команда доступна только на канале верификации⚠',
                            color=0x39d0d6)
                        await ctx.respond(embed=ver_emb)
                    else:
                        ver_emb = discord.Embed(
                            title=f'⚠This command is only available on the verification channel⚠',
                            color=0x39d0d6)
                        await ctx.respond(embed=ver_emb)
            else:
                ver_emb = discord.Embed(
                    title=f'⚠This command is only available on the verification channel⚠',
                    color=0x39d0d6)
                await ctx.respond(embed=ver_emb)
        else:
            dec_emb = discord.Embed(title=f'❌Your form was declined!, reason: {reason}')
            await user.send(embed=dec_emb)
            await ctx.respond(f'**Successfully declined user {user}, reason: {reason}!**')

class Enrepform(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Describe your problem:", style=discord.InputTextStyle.long))
        self.add_item(discord.ui.InputText(label="Did you try solving it?", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="Does it involve any data corruption?", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="When did you encouter the problem?", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="Server id, where the problem was found:", style=discord.InputTextStyle.short))

    async def callback(self, interaction: discord.Interaction):
        channel = bot.get_channel(1100099118338150550)
        embed = discord.Embed(title=f"New report form recieved.")
        embed.add_field(name="Describe your problem:", value=self.children[0].value)
        embed.add_field(name="Did you try solving it?", value=self.children[1].value)
        embed.add_field(name="Does it involve any data corruption?", value=self.children[2].value)
        embed.add_field(name="When did you encouter the problem?", value=self.children[3].value)
        embed.add_field(name="Server id:", value=self.children[4].value)
        rep_emb = discord.Embed(
            title=f"Your form was sent",
            color=0x39d0d6)
        await interaction.response.send_message(embed=rep_emb)
        await channel.send('<@&1018203286836363484>')
        await channel.send(embeds=[embed])

class Rurepform(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Опишите проблему:", style=discord.InputTextStyle.long))
        self.add_item(discord.ui.InputText(label="Вы пытались её как либо решить?", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="Это связано с повреждением данных?", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="Когда вы заметили проблему?", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="Айди сервера, где была обнаружена проблема:", style=discord.InputTextStyle.short))

    async def callback(self, interaction: discord.Interaction):
        channel = bot.get_channel(1100099118338150550)
        embed = discord.Embed(title=f"Был получен новый репорт.")
        embed.add_field(name="Опишите проблему:", value=self.children[0].value)
        embed.add_field(name="Вы пытались её как либо решить?", value=self.children[1].value)
        embed.add_field(name="Это связано с повреждением данных?", value=self.children[2].value)
        embed.add_field(name="Когда вы заметили проблему?", value=self.children[3].value)
        embed.add_field(name="Айди сервера, где была обнаружена проблема:", value=self.children[4].value)
        rep_emb = discord.Embed(
            title=f"Ваша форма была отправлена",
            color=0x39d0d6)
        await interaction.response.send_message(embed=rep_emb)
        await channel.send('<@&1018203286836363484>')
        await channel.send(embeds=[embed])

@bot.slash_command(name = "report", description = "report an error")
async def report(ctx):
    getlang = Language.get_or_none(guild_id=ctx.guild.id)
    if getlang is not None:
        for language in Language.select().where(Language.guild_id == ctx.guild.id):
            if language.lang == "ru":
                await ctx.send_modal(Rurepform(title="Форма ошибки"))
            else:
                await ctx.send_modal(Enrepform(title="Error report form"))
    else:
        await ctx.send_modal(Enrepform(title="Error report form"))

bot.run('MTAxMjAyOTU1MjYzNTE2MjY3NA.GNdCdB.n2zTGQjsvfFsATOGT1ijSfJOv_gSIbwSpSOU3U')
