import discord
from discord.ext import commands
import sqlite3
import random
from random import choice
import peewee
from peewee import *
from Aurix_base import Language

community_rights = 'Mester Satellite, © 2023 All rights reserved'
creator_url = 'https://cdn.discordapp.com/avatars/830486806478848040/cb206fa6511033c04a91016af44a6c65.png?size=1024'

class MyViewENG(discord.ui.View):
    @discord.ui.select(
        placeholder = "Choose a category",
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label="📃information",
                description="All commands from category 📃information"
            ),
            discord.SelectOption(
                label="💻server-management",
                description="All commands from category 💻server-management"
            ),
            discord.SelectOption(
                label="⚒additional-utility",
                description="All commands from category ⚒additional-utility"
            ),
            discord.SelectOption(
                label="🎮fun",
                description="All commands from category 🎮fun"
            ),
            discord.SelectOption(
                label="💵economy",
                description="All commands from category 💵economy"
            ),
            discord.SelectOption(
                label="💾other",
                description="All commands from category 💾other"
            )
        ]
    )
    async def select_callback(self, select, interaction):
        if select.values[0] == "📃information":
            help_emb = discord.Embed(title='Command list', colour=0x39d0d6)
            help_emb.add_field(name='📃information',
                               value='/help - information about commands,\n/userinfo [user] - shows user information,\n/avatar [user] - shows user avatar,\n/serverinfo - shows current server information,\n/settings - shows all server settings,\n/statistics - shows current bot statistics',
                               inline=False)
            help_emb.set_footer(text=community_rights,
                                icon_url=creator_url)

        elif select.values[0] == "💻server-management":
            help_emb = discord.Embed(title='Command list', colour=0x39d0d6)
            help_emb.add_field(name='💻server-management',
                               value='/ban [user] {reason} - bans mentioned user, \n/unban [user] - unbans mentioned user, \n/kick [user] {reason} - kicks mentioned user,\n/mute [user] {reason} - mutes specified user,\n/role_add [role] [user] - adds mentioned role to a mentioned user,\n/clear [amount] - deletes previous messages, \n/set_lang [ru] - изменить язык бота на русский, \n/warn [user] [warn] [index] - warns mentioned user,\n/warn_list [user] - shows all warns for specified user,\n/pardon [user] [index] - clears all warns for specified user,\n/joinrole [on/off] {role} - sets join role for your server,\n/muterole [on/off] {role} - sets mute role for your server,\n/ticketrole [role] - sets maintenance role for your server,\n/open [reason] - opens the a new support ticket,\n/logschan [on/off] {channel} - sets logs channel for your server',
                               inline=False)
            help_emb.set_footer(text=community_rights,
                                icon_url=creator_url)

        elif select.values[0] == "⚒additional-utility":
            help_emb = discord.Embed(title='Command list', colour=0x39d0d6)
            help_emb.add_field(name='⚒additional-utility',
                               value="/print [message] - prints your message,\n/create_channel [name] - creates new server channel,\n/github - link to our github page,\n/wikifur - link to Wikifur community",
                               inline=False)
            help_emb.set_footer(text=community_rights,
                                icon_url=creator_url)

        elif select.values[0] == "🎮fun":
            help_emb = discord.Embed(title='Command list', colour=0x39d0d6)
            help_emb.add_field(name='🎮fun',
                               value="/fox - random picture of a cute fox🦊\n/cat - random picture of a cute cat🐱\n/roll [rolls amount] [sides amount] - rolls a dice,\n/hug [user] - hugs mentioned user,\n/sum [number] [number] - sums two mentioned numbers,\n/choice - Orix will answer 'yes' or 'no',\n/play_with [user] {game} - ask user to play some game with you",
                               inline=False)
            help_emb.set_footer(text=community_rights,
                                icon_url=creator_url)

        elif select.values[0] == "💵economy":
            help_emb = discord.Embed(title='Command list', colour=0x39d0d6)
            help_emb.add_field(name='💵economy',
                               value="/give_money [user] [amount] - give some amount of your 💷 to mentioned user,\n/balance {user} - shows your current balance,\n/set_money [user] [amount] - sets mentioned amount of 💷 to mentioned user,\n/work [crime/business/casual] - you can earn some 💷, but your salary is not stable,\n/deposit [amount] - deposit some 💷 to your bank account,\n/deduct [amount] - deduct some 💷 from your bank account,\n/shop - get list of all items available for this server,\n/add_item [name] [cost] {role} - add new item to the shop,\n/remove_item [name] - remove item from the shop,\n/buy - buy some items",
                               inline=False)
            help_emb.set_footer(text=community_rights,
                                icon_url=creator_url)

        elif select.values[0] == "💾other":
            help_emb = discord.Embed(title='Command list', colour=0x39d0d6)
            help_emb.add_field(name='💾other', value='/ping - replies with pong,\n/report - report an error', inline=False)
            help_emb.set_footer(text=community_rights,
                                icon_url=creator_url)

        await interaction.response.send_message(embed=help_emb)

class MyViewRU(discord.ui.View):
    @discord.ui.select(
        placeholder = "Выбери категорию",
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label="📃информация",
                description="Все команды категории 📃information"
            ),
            discord.SelectOption(
                label="💻управление-сервером",
                description="Все команды категории 💻управление-сервером"
            ),
            discord.SelectOption(
                label="⚒дополнительные-утилиты",
                description="Все команды категории ⚒дополнительные-утилиты"
            ),
            discord.SelectOption(
                label="🎮развлечения",
                description="Все команды категории 🎮развлечения"
            ),
            discord.SelectOption(
                label="💵экономика",
                description="Все команды категории 💵экономика"
            ),
            discord.SelectOption(
                label="💾другое",
                description="Все команды категории 💾другое"
            )
        ]
    )
    async def select_callback(self, select, interaction):
        if select.values[0] == "📃информация":
            help_emb = discord.Embed(title='Список команд', colour=0x39d0d6)
            help_emb.add_field(name='📃информация',
                               value='/help - список всех команд,\n/userinfo [пользователь] - показывает информацию об указанном пользователе,\n/avatar [пользователь] - показывает аватар указанного пользователя,\n/settings - показывает все настройки сервера,\n/serverinfo - показывает информацию о сервере',
                               inline=False)
            help_emb.set_footer(text=community_rights,
                                icon_url=creator_url)

        elif select.values[0] == "💻управление-сервером":
            help_emb = discord.Embed(title='Список команд', colour=0x39d0d6)
            help_emb.add_field(name='💻управление-сервером',
                               value='/ban [пользователь] {причина} - банит указанного пользователя,\n/unban [пользователь] - разбанивает указанного пользователя, \n/kick [пользователь] {причина} - кикает указанного пользователя,\n/mute [пользователь] {причина} - выдает мут роль указанному пользователю,\n/role_add [роль] [пользователь] - добавляет указанную роль, указанному пользователю,\n/clear [количество] - удаляет указанное количество сообщений,\n/set_lang [eng] - set bot language to english,\n/warn [пользователь] [предупреждение] [индекс] - предупреждает указанного пользователя,\n/warn_list [пользователь] - показывает все предупреждения у указанного пользователя,\n/pardon [пользователь] [индекс] - удаляет все предупреждения у указанного пользователя,\n/joinrole [on/off] {роль} - устанавливает приветственную роль для вашего сервера,\n/muterole [on/off] {роль} - устанавливает мут роль для вашего сервера,\n/ticketrole [роль] - уставливает роль проверки тикетов для вашего сервера,\n/open [причина] - открывает новый тикет поддержки,\n/logschan [on/off] {канал} - устанавливает канал для системных сообщений',
                               inline=False)
            help_emb.set_footer(text=community_rights,
                                icon_url=creator_url)

        elif select.values[0] == "⚒дополнительные-утилиты":
            help_emb = discord.Embed(title='Список команд', colour=0x39d0d6)
            help_emb.add_field(name='⚒дополнительные-утилиты',
                               value="/print [сообщение] - выводит указанное сообщение,\n/create_channel [название] - создает новый канал с указанным названием,\n/github - репозиторий проекта в гитхабе,\n/wikifur - Викифур",
                               inline=False)
            help_emb.set_footer(text=community_rights,
                                icon_url=creator_url)

        elif select.values[0] == "🎮развлечения":
            help_emb = discord.Embed(title='Список команд', colour=0x39d0d6)
            help_emb.add_field(name='🎮развлечения',
                               value="/fox - рандомная картинка милой лисички🦊\n/cat - рандомная картинка милой кошечки🐱\n/roll [количество бросков] [количество сторон] - бросает кубик,\n/hug [user] - обнимает указанного пользователя,\n/sum [число] [число] - складывает два указанных числа,\n/choice - Orix ответит 'да' или 'нет',\n/play_with [пользователь] {игра} - попроси пользователя сыграть с тобой в игру",
                               inline=False)
            help_emb.set_footer(text=community_rights,
                                icon_url=creator_url)

        elif select.values[0] == "💵экономика":
            help_emb = discord.Embed(title='Список команд', colour=0x39d0d6)
            help_emb.add_field(name='💵экономика',
                               value="/give_money [пользователь] [количество] - вы отдаете указанную сумму 💷 другому пользователю,\n/balance {пользователь} - показывает ваш баланс,\n/set_money [пользователь] [количество] - устанавливает указанное количество 💷, указанному пользователю,\n/work [crime/business/casual] - вы можете заработать немного 💷, но ваша зарплата не постоянна,\n/deposit [количество] - пополните свой банковский счет,\n/deduct [количество] - снимите 💷 со своего банковского счета,\n/shop - получить список всех товаров, доступных для этого сервера,\n/add_item [название] [стоимость] {роль} - добавить новый товар в магазин,\n/remove_item [название] - вы можете удалить товар из магазина,\n/buy - вы можете купить некоторые товары",
                               inline=False)
            help_emb.set_footer(text=community_rights,
                                icon_url=creator_url)

        elif select.values[0] == "💾другое":
            help_emb = discord.Embed(title='Список команд', colour=0x39d0d6)
            help_emb.add_field(name='💾другое', value='/ping - понг,\n/report - сообщите об ошибке', inline=False)
            help_emb.set_footer(text=community_rights,
                                icon_url=creator_url)

        await interaction.response.send_message(embed=help_emb)

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="help", description="information about commands")
    async def help(self, ctx):
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is not None:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    help_emb = discord.Embed(title='''
                        \nВыбери категорию ниже.
                        \nОбязательные аргументы - ```[]```
                        \nНеобязательные аргументы - ```{}```''', colour=0x39d0d6)
                    await ctx.respond(embed=help_emb, view=MyViewRU())
                else:
                    help_emb = discord.Embed(title='''
                        \nChoose a category below.
                        \nRequired arguments - ```[]```
                        \nOptional arguments - ```{}```''', colour=0x39d0d6)
                    await ctx.respond(embed=help_emb, view=MyViewENG())
        else:
            help_emb = discord.Embed(title='''
                \nChoose a category below.
                \nRequired arguments - ```[]```
                \nOptional arguments - ```{}```''', colour=0x39d0d6)
            await ctx.respond(embed=help_emb, view=MyViewENG())

    @commands.slash_command(name="userinfo", description="shows user information")
    @commands.has_permissions(administrator=True)
    async def userinfo(self, ctx, member: discord.Member):
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is not None:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    emb = discord.Embed(title="📄Информация", color=member.color)
                    emb.add_field(name="📁Имя :", value=member.display_name, inline=False)
                    emb.add_field(name="📁Айди :", value=member.id, inline=False)
                    t = member.status

                    emb.add_field(name="📁Статус :", value=member.status, inline=False)
                    emb.add_field(name="📁Роль на сервере :", value=f"{member.top_role.mention}", inline=False)
                    emb.add_field(name="📁Аккаунт был создан :",
                                  value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                                  inline=False)
                    emb.set_thumbnail(url=member.avatar)
                    emb.set_footer(text=community_rights,
                                   icon_url=creator_url)
                    await ctx.respond(embed=emb)
                else:
                    emb = discord.Embed(title="📄User information", color=member.color)
                    emb.add_field(name="📁Name :", value=member.display_name, inline=False)
                    emb.add_field(name="📁User ID :", value=member.id, inline=False)
                    t = member.status

                    emb.add_field(name="📁Status :", value=member.status, inline=False)
                    emb.add_field(name="📁Server role :", value=f"{member.top_role.mention}", inline=False)
                    emb.add_field(name="📁Account was created :",
                                  value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                                  inline=False)
                    emb.set_thumbnail(url=member.avatar)
                    emb.set_footer(text=community_rights,
                                   icon_url=creator_url)
                    await ctx.respond(embed=emb)
        else:
            emb = discord.Embed(title="📄User information", color=member.color)
            emb.add_field(name="📁Name :", value=member.display_name, inline=False)
            emb.add_field(name="📁User ID :", value=member.id, inline=False)
            t = member.status

            emb.add_field(name="📁Status :", value=member.status, inline=False)
            emb.add_field(name="📁Server role :", value=f"{member.top_role.mention}", inline=False)
            emb.add_field(name="📁Account was created :",
                          value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                          inline=False)
            emb.set_thumbnail(url=member.avatar)
            emb.set_footer(text=community_rights,
                           icon_url=creator_url)
            await ctx.respond(embed=emb)

    @commands.slash_command(name="avatar", description="shows user avatar")
    @commands.has_permissions(administrator=True)
    async def avatar(self, ctx, *, user: discord.Member = None):
        if user is None:
            userAvatarUrl = ctx.author.avatar
            await ctx.respond(userAvatarUrl)
        else:
            userAvatarUrl = user.avatar
            await ctx.respond(userAvatarUrl)

    @commands.slash_command(name="serverinfo", description="shows information about current server")
    async def serverinfo(self, ctx):
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is not None:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    info_emb = discord.Embed(title=f'📄Информация о сервере', colour=0x39d0d6)
                    info_emb.set_thumbnail(url=ctx.guild.icon)
                    info_emb.add_field(name='📁Название:', value=ctx.guild, inline=False)
                    info_emb.add_field(name='📁Айди:', value=ctx.guild.id, inline=False)
                    info_emb.add_field(name='📁Количество участников:', value=len(ctx.guild.members), inline=False)
                    info_emb.add_field(name='📁Количество ролей:', value=len(ctx.guild.roles), inline=False)
                    info_emb.add_field(name='📁Владелец:', value=ctx.guild.owner, inline=False)
                    info_emb.set_footer(text=community_rights,
                                        icon_url=creator_url)
                    await ctx.respond(embed=info_emb)
                else:
                    info_emb = discord.Embed(title=f'📄Server information', colour=0x39d0d6)
                    info_emb.set_thumbnail(url=ctx.guild.icon)
                    info_emb.add_field(name='📁Server name:', value=ctx.guild, inline=False)
                    info_emb.add_field(name='📁Server id:', value=ctx.guild.id, inline=False)
                    info_emb.add_field(name='📁Number of members:', value=len(ctx.guild.members), inline=False)
                    info_emb.add_field(name='📁Number of roles:', value=len(ctx.guild.roles), inline=False)
                    info_emb.add_field(name='📁Server owner:', value=ctx.guild.owner, inline=False)
                    info_emb.set_footer(text=community_rights,
                                        icon_url=creator_url)
                    await ctx.respond(embed=info_emb)
        else:
            info_emb = discord.Embed(title=f'📄Server information', colour=0x39d0d6)
            info_emb.set_thumbnail(url=ctx.guild.icon)
            info_emb.add_field(name='📁Server name:', value=ctx.guild, inline=False)
            info_emb.add_field(name='📁Server id:', value=ctx.guild.id, inline=False)
            info_emb.add_field(name='📁Number of members:', value=len(ctx.guild.members), inline=False)
            info_emb.add_field(name='📁Number of roles:', value=len(ctx.guild.roles), inline=False)
            info_emb.add_field(name='📁Server owner:', value=ctx.guild.owner, inline=False)
            info_emb.set_footer(text=community_rights,
                                icon_url=creator_url)
            await ctx.respond(embed=info_emb)

    @commands.slash_command(name="statistics", description="Shows bot's statistics")
    async def statistics(self, ctx):
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is not None:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    guilds = len(list(self.bot.guilds))
                    users = len(list(self.bot.users))
                    stats = discord.Embed(title='Statistics', colour=0x39d0d6)
                    stats.set_thumbnail(
                        url='https://cdn.discordapp.com/avatars/1012029552635162674/c5c88afdd98386c8df956658f4f3057d.png?size=1024')
                    stats.add_field(name='📊Количество серверов:', value=f'{guilds}', inline=False)
                    stats.add_field(name='😺Количество пользователей:', value=f'{users}', inline=False)
                    await ctx.respond(embed=stats)
                else:
                    guilds = len(list(self.bot.guilds))
                    users = len(list(self.bot.users))
                    stats = discord.Embed(title='Statistics', colour=0x39d0d6)
                    stats.set_thumbnail(
                        url='https://cdn.discordapp.com/avatars/1012029552635162674/c5c88afdd98386c8df956658f4f3057d.png?size=1024')
                    stats.add_field(name='📊Total amount of servers:', value=f'{guilds}', inline=False)
                    stats.add_field(name='😺Total amount of users:', value=f'{users}', inline=False)
                    await ctx.respond(embed=stats)
        else:
            guilds = len(list(self.bot.guilds))
            users = len(list(self.bot.users))
            stats = discord.Embed(title='Statistics', colour=0x39d0d6)
            stats.set_thumbnail(
                url='https://cdn.discordapp.com/avatars/1012029552635162674/c5c88afdd98386c8df956658f4f3057d.png?size=1024')
            stats.add_field(name='📊Total amount of servers:', value=f'{guilds}', inline=False)
            stats.add_field(name='😺Total amount of users:', value=f'{users}', inline=False)
            await ctx.respond(embed=stats)

def setup(bot):
    bot.add_cog(Info(bot))