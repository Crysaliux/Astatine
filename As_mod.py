import discord
from discord.ext import commands
import sqlite3
import random
from random import choice
import peewee
from peewee import *
from Aurix_base import Warns, Language, Join, Mute, Ticket, TicketRole, Logs

class ticket_conf_en(discord.ui.View):
    @discord.ui.button(label="Close", style=discord.ButtonStyle.danger)
    async def first_button_callback(self, button, interaction):
        button_emb = discord.Embed(
            title=f"Closing your ticket...",
            color=0x39d0d6)
        await interaction.response.send_message(embed=button_emb)
        await interaction.channel.delete()

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.success)
    async def second_button_callback(self, button, interaction):
        for ticketrole in TicketRole.select().where(TicketRole.guild_id == interaction.guild.id):
            role = interaction.guild.get_role(ticketrole.role_id)
            if role in interaction.user.roles:
                button_emb = discord.Embed(
                    title=f"Your ticket was accepted by {interaction.user}",
                    color=0x39d0d6)
                await interaction.response.send_message(embed=button_emb)
            else:
                button_emb = discord.Embed(
                    title=f"⚠You dont have enough permissions for accepting tickets!⚠",
                    color=0x39d0d6)
                await interaction.response.send_message(embed=button_emb)

class ticket_conf_ru(discord.ui.View):
    @discord.ui.button(label="Close", style=discord.ButtonStyle.danger)
    async def first_button_callback(self, button, interaction):
        button_emb = discord.Embed(
            title=f"Закрываем ваш тикет...",
            color=0x39d0d6)
        await interaction.response.send_message(embed=button_emb)
        await interaction.channel.delete()

    @discord.ui.button(label="Принять", style=discord.ButtonStyle.success)
    async def second_button_callback(self, button, interaction):
        for ticketrole in TicketRole.select().where(TicketRole.guild_id == interaction.guild.id):
            role = interaction.guild.get_role(ticketrole.role_id)
            if role in interaction.user.roles:
                button_emb = discord.Embed(
                    title=f"Ваш билет был принят {interaction.user}",
                    color=0x39d0d6)
                await interaction.response.send_message(embed=button_emb)
            else:
                button_emb = discord.Embed(
                    title=f"⚠У вас недостаточно разрешений для приема билетов!⚠",
                    color=0x39d0d6)
                await interaction.response.send_message(embed=button_emb)

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ban", description="bans mentioned user")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is not None:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    ban_emb = discord.Embed(title=f'⚙Пользователь <@{member.id}> был забанен',
                                            description=f'Причина: {reason}',
                                            color=0x39d0d6)
                    await ctx.respond(embed=ban_emb)
                else:
                    ban_emb = discord.Embed(title=f'⚙User <@{member.id}> was banned',
                                            description=f'Reason: {reason}',
                                            color=0x39d0d6)
                    await ctx.respond(embed=ban_emb)
        else:
            ban_emb = discord.Embed(title=f'⚙User <@{member.id}> was banned',
                                    description=f'Reason: {reason}',
                                    color=0x39d0d6)
            await ctx.respond(embed=ban_emb)

    @commands.slash_command(name="unban", description="unbans mentioned user")
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, user: discord.User):
        await ctx.guild.unban(user=user)
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is not None:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    unban_emb = discord.Embed(title=f'⚙Пользователь <@{user}> был разбанен', color=0x39d0d6)
                    await ctx.respond(embed=unban_emb)
                else:
                    unban_emb = discord.Embed(title=f'⚙User <@{user}> was unbanned', color=0x39d0d6)
                    await ctx.respond(embed=unban_emb)
        else:
            unban_emb = discord.Embed(title=f'⚙User <@{user}> was unbanned', color=0x39d0d6)
            await ctx.respond(embed=unban_emb)

    @commands.slash_command(name="kick", description="kicks mentioned user")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is not None:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    kick_emb = discord.Embed(title=f'⚙Пользователь <@{member.id}> был кикнут',
                                             description=f'Причина: {reason}',
                                             color=0x39d0d6)
                    await ctx.respond(embed=kick_emb)
                else:
                    kick_emb = discord.Embed(title=f'⚙User <@{member.id}> was kicked',
                                             description=f'Reason: {reason}',
                                             color=0x39d0d6)
                    await ctx.respond(embed=kick_emb)
        else:
            kick_emb = discord.Embed(title=f'⚙User <@{member.id}> was kicked',
                                     description=f'Reason: {reason}',
                                     color=0x39d0d6)
            await ctx.respond(embed=kick_emb)

    @commands.slash_command(name="role_add", description="adds mentioned role to a mentioned user")
    @commands.has_permissions(manage_roles=True)
    async def role_add(self, ctx, user: discord.Member, role: discord.Role):
        await user.add_roles(role)
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is not None:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    role_emb = discord.Embed(title=f"Вы добавили роль {role} пользователю {user.mention}",
                                             color=0x39d0d6)
                    await ctx.respond(embed=role_emb)
                else:
                    role_emb = discord.Embed(title=f"Added role {role} to {user.mention}", color=0x39d0d6)
                    await ctx.respond(embed=role_emb)
        else:
            role_emb = discord.Embed(title=f"Added role {role} to {user.mention}", color=0x39d0d6)
            await ctx.respond(embed=role_emb)

    @commands.slash_command(name="clear", description="deletes previous messages")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, *, amount: int = None):
        if amount < 0:
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is not None:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == "ru":
                        msg_emb = discord.Embed(title=f'⚠Количество должно быть положительным⚠',
                                                color=0x39d0d6)
                        await ctx.respond(embed=msg_emb)
                    else:
                        msg_emb = discord.Embed(title=f'⚠The quantity must be positive⚠', color=0x39d0d6)
                        await ctx.respond(embed=msg_emb)
            else:
                msg_emb = discord.Embed(title=f'⚠The quantity must be positive⚠', color=0x39d0d6)
                await ctx.respond(embed=msg_emb)
        else:
            if amount > 250:
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is not None:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == "ru":
                            msg_emb = discord.Embed(title=f'⚠Вы можете удалить не более 250 сообщений за один раз⚠',
                                                    color=0x39d0d6)
                            await ctx.respond(embed=msg_emb)
                        else:
                            msg_emb = discord.Embed(title=f'⚠You cant delete more than 250 messages at once⚠',
                                                    color=0x39d0d6)
                            await ctx.respond(embed=msg_emb)
                else:
                    msg_emb = discord.Embed(title=f'⚠You cant delete more than 250 messages at once⚠', color=0x39d0d6)
                    await ctx.respond(embed=msg_emb)
            else:
                await ctx.channel.purge(limit=amount)
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is not None:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == "ru":
                            msg_emb = discord.Embed(title=f'```{amount} сообщений было успешно удалено```',
                                                    color=0x39d0d6)
                            await ctx.respond(embed=msg_emb)
                        else:
                            msg_emb = discord.Embed(title=f'```{amount} messages were deleted```', color=0x39d0d6)
                            await ctx.respond(embed=msg_emb)
                else:
                    msg_emb = discord.Embed(title=f'```{amount} messages were deleted```', color=0x39d0d6)
                    await ctx.respond(embed=msg_emb)

    @commands.slash_command(name="set_lang", description="change your bot language ru/eng")
    @commands.has_permissions(administrator=True)
    async def set_lang(self, ctx, *, lang: discord.Option(str, choices=[
        discord.OptionChoice(name="ru", value="ru", name_localizations=None),
        discord.OptionChoice(name="en", value="en", name_localizations=None)])):
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is not None:
            delete = Language.get(Language.guild_id == ctx.guild.id)
            delete.delete_instance()
            langset = Language.create(guild_id=ctx.guild.id, lang=lang)
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    lang_emb = discord.Embed(title='🇷🇺Вы изменили язык бота на русский', color=0x39d0d6)
                    await ctx.respond(embed=lang_emb)
                else:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == "en":
                            lang_emb = discord.Embed(title='🇺🇸Your bot language is english', color=0x39d0d6)
                            await ctx.respond(embed=lang_emb)
        else:
            langset = Language.create(guild_id=ctx.guild.id, lang=lang)
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    lang_emb = discord.Embed(title='🇷🇺Вы изменили язык бота на русский', color=0x39d0d6)
                    await ctx.respond(embed=lang_emb)
                else:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == "en":
                            lang_emb = discord.Embed(title='🇺🇸Your bot language is english', color=0x39d0d6)
                            await ctx.respond(embed=lang_emb)

    @commands.slash_command(name="warn", description="warns mentioned user")
    @commands.has_permissions(administrator=True)
    async def warn(self, ctx, user: discord.Member, *, warn: str, index: int = None):
        if user.id == ctx.author.id:
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is not None:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == "ru":
                        msg_emb = discord.Embed(title=f'⚠Вы не можете выдать предупреждение себе же!⚠', color=0x39d0d6)
                        await ctx.respond(embed=msg_emb)
                    else:
                        msg_emb = discord.Embed(title=f'⚠You cant give a warn to yourself!⚠', color=0x39d0d6)
                        await ctx.respond(embed=msg_emb)
            else:
                msg_emb = discord.Embed(title=f'⚠You cant give a warn to yourself!⚠', color=0x39d0d6)
                await ctx.respond(embed=msg_emb)
        else:
            if user.bot:
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is not None:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == "ru":
                            msg_emb = discord.Embed(title=f'⚠Вы не можете выдать предупреждение боту!⚠', color=0x39d0d6)
                            await ctx.respond(embed=msg_emb)
                        else:
                            msg_emb = discord.Embed(title=f'⚠You cant give a warn to a bot!⚠', color=0x39d0d6)
                            await ctx.respond(embed=msg_emb)
                else:
                    msg_emb = discord.Embed(title=f'⚠You cant give a warn to a bot!⚠', color=0x39d0d6)
                    await ctx.respond(embed=msg_emb)
            else:
                new_warn = Warns.create(guild_id=ctx.guild.id, user_id=user.id, warn=warn, index=index)
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is not None:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == "ru":
                            warns_emb = discord.Embed(title=f"Пользователь {user}, получил предупреждение: {warn}",
                                                      color=0x39d0d6)
                            await ctx.respond(embed=warns_emb)
                            channel = await user.create_dm()
                            warn_emb = discord.Embed(title=f"Вы были предупреждены: {warn}, сервер: {ctx.guild}",
                                                     color=0x39d0d6)
                            await channel.send(embed=warn_emb)
                        else:
                            warns_emb = discord.Embed(title=f"User {user}, was warned: {warn}", color=0x39d0d6)
                            await ctx.respond(embed=warns_emb)
                            channel = await user.create_dm()
                            warn_emb = discord.Embed(title=f"You were warned: {warn}, server: {ctx.guild}",
                                                     color=0x39d0d6)
                            await channel.send(embed=warn_emb)
                else:
                    warns_emb = discord.Embed(title=f"User {user}, was warned: {warn}", color=0x39d0d6)
                    await ctx.respond(embed=warns_emb)
                    channel = await user.create_dm()
                    warn_emb = discord.Embed(title=f"You were warned: {warn}, server: {ctx.guild}", color=0x39d0d6)
                    await channel.send(embed=warn_emb)

    @commands.slash_command(name="warn_list", description="shows all warns for specified user")
    @commands.has_permissions(administrator=True)
    async def warn_list(self, ctx, user: discord.Member):
        warns_get = Warns.get_or_none(guild_id=ctx.guild.id, user_id=user.id)
        if warns_get is not None:
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is not None:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == "ru":
                        warns_emb = discord.Embed(title=f'📄Предупреждения пользователя {user}',
                                                  colour=0x39d0d6)
                        for warns in Warns.select().where(Warns.guild_id == ctx.guild.id, Warns.user_id == user.id):
                            warns_emb.add_field(name=f'[Предупреждение]:',
                                                value=f'{warns.warn}, **🏷индекс**[{warns.index}]',
                                                inline=False)
                            await ctx.respond(embed=warns_emb)
                    else:
                        warns_emb = discord.Embed(title=f'📄Warns for user {user}',
                                                  colour=0x39d0d6)
                        for warns in Warns.select().where(Warns.guild_id == ctx.guild.id, Warns.user_id == user.id):
                            warns_emb.add_field(name=f'[Warn]:', value=f'{warns.warn}, **🏷index**[{warns.index}]',
                                                inline=False)
                            await ctx.respond(embed=warns_emb)
            else:
                warns_emb = discord.Embed(title=f'📄Warns for user {user}',
                                          colour=0x39d0d6)
                for warns in Warns.select().where(Warns.guild_id == ctx.guild.id, Warns.user_id == user.id):
                    warns_emb.add_field(name=f'[Warn]:', value=f'{warns.warn}, **🏷index**[{warns.index}]',
                                        inline=False)
                    await ctx.respond(embed=warns_emb)
        else:
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is not None:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == "ru":
                        warns_emb = discord.Embed(title=f"У пользователя {user} нету предупреждений", color=0x39d0d6)
                        await ctx.respond(embed=warns_emb)
                    else:
                        warns_emb = discord.Embed(title=f"User {user} has no warns", color=0x39d0d6)
                        await ctx.respond(embed=warns_emb)
            else:
                warns_emb = discord.Embed(title=f"User {user} has no warns", color=0x39d0d6)
                await ctx.respond(embed=warns_emb)

    @commands.slash_command(name="pardon", description="clears all warns for specified user")
    @commands.has_permissions(administrator=True)
    async def pardon(self, ctx, user: discord.Member, index: int = None):
        warns_get = Warns.get_or_none(guild_id=ctx.guild.id, user_id=user.id)
        if warns_get is not None:
            if index is None:
                for warns in Warns.select().where(Warns.guild_id == ctx.guild.id, Warns.user_id == user.id):
                    delete = Warns.get(Warns.guild_id == ctx.guild.id, Warns.user_id == user.id)
                    delete.delete_instance()
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is not None:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == "ru":
                            warns_emb = discord.Embed(
                                title=f"Все предупреждения пользователя {user} были успешно удалены",
                                color=0x39d0d6)
                            await ctx.respond(embed=warns_emb)
                        else:
                            warns_emb = discord.Embed(title=f"Successfully deleted all warns for user {user}",
                                                      color=0x39d0d6)
                            await ctx.respond(embed=warns_emb)
                else:
                    warns_emb = discord.Embed(title=f"Successfully deleted all warns for user {user}",
                                              color=0x39d0d6)
                    await ctx.respond(embed=warns_emb)
            else:
                for warns in Warns.select().where(Warns.guild_id == ctx.guild.id, Warns.user_id == user.id,
                                                  Warns.index == index):
                    delete = Warns.get(Warns.guild_id == ctx.guild.id, Warns.user_id == user.id, Warns.index == index)
                    delete.delete_instance()
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is not None:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == "ru":
                            warns_emb = discord.Embed(
                                title=f"Все предупреждения с индексом {index} пользователя {user} были успешно удалены",
                                color=0x39d0d6)
                            await ctx.respond(embed=warns_emb)
                        else:
                            warns_emb = discord.Embed(
                                title=f"Successfully deleted all warns with index {index} for user {user}",
                                color=0x39d0d6)
                            await ctx.respond(embed=warns_emb)
                else:
                    warns_emb = discord.Embed(
                        title=f"Successfully deleted all warns with index {index} for user {user}",
                        color=0x39d0d6)
                    await ctx.respond(embed=warns_emb)
        else:
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is not None:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == "ru":
                        warns_emb = discord.Embed(
                            title=f"У пользователя {user} нету предупреждений",
                            color=0x39d0d6)
                        await ctx.respond(embed=warns_emb)
                    else:
                        warns_emb = discord.Embed(
                            title=f"User {user} has no warns",
                            color=0x39d0d6)
                        await ctx.respond(embed=warns_emb)
            else:
                warns_emb = discord.Embed(
                    title=f"User {user} has no warns",
                    color=0x39d0d6)
                await ctx.respond(embed=warns_emb)

    @commands.slash_command(name="joinrole", description="sets joinrole for your server")
    @commands.has_permissions(administrator=True)
    async def joinrole(self, ctx, settings: discord.Option(str, choices=[
        discord.OptionChoice(name="on", value="on", name_localizations=None),
        discord.OptionChoice(name="off", value="off", name_localizations=None)]), role: discord.Role = None):
        if role is None:
            if settings == 'on':
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is not None:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == "ru":
                            role_emb = discord.Embed(
                                title="⚠Пожалуйста укажите роль!⚠",
                                color=0x39d0d6)
                            await ctx.respond(embed=role_emb)
                        else:
                            role_emb = discord.Embed(
                                title="⚠Please specify the role!⚠",
                                color=0x39d0d6)
                            await ctx.respond(embed=role_emb)
                else:
                    role_emb = discord.Embed(
                        title="⚠Please specify the role!⚠",
                        color=0x39d0d6)
                    await ctx.respond(embed=role_emb)
            else:
                getjoin = Join.get_or_none(guild_id=ctx.guild.id)
                if getjoin is None:
                    newjoin = Join.create(guild_id=ctx.guild.id, role_id='0', settings=settings)
                else:
                    delete = Join.get(Join.guild_id == ctx.guild.id)
                    delete.delete_instance()
                    newjoin = Join.create(guild_id=ctx.guild.id, role_id='0', settings=settings)
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is not None:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == "ru":
                            role_emb = discord.Embed(
                                title="Функция успешно отключена",
                                color=0x39d0d6)
                            await ctx.respond(embed=role_emb)
                        else:
                            role_emb = discord.Embed(
                                title="The function has been successfully disabled",
                                color=0x39d0d6)
                            await ctx.respond(embed=role_emb)
                else:
                    role_emb = discord.Embed(
                        title="The function has been successfully disabled",
                        color=0x39d0d6)
                    await ctx.respond(embed=role_emb)
        elif role is not None:
            if ctx.guild.me.top_role <= role:
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is not None:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == "ru":
                            em = discord.Embed(title="⚠У бота недостаточно прав⚠",
                                               description='Роль бота находится ниже или равна указанной вами роли. Бот не сможет выдавать роли пользователям стоящим по иерархии выше него.',
                                               color=0x39d0d6)
                            await ctx.respond(embed=em)
                        else:
                            em = discord.Embed(title="⚠The bot doesn't have enough permissions⚠",
                                               description='The role of the bot is below or equal to the role you specified. The bot will not be able to assign roles to users standing in the hierarchy above it.',
                                               color=0x39d0d6)
                            await ctx.respond(embed=em)
                else:
                    em = discord.Embed(title="⚠The bot doesn't have enough permissions⚠",
                                       description='The role of the bot is below or equal to the role you specified. The bot will not be able to assign roles to users standing in the hierarchy above it.',
                                       color=0x39d0d6)
                    await ctx.respond(embed=em)
            else:
                getjoin = Join.get_or_none(guild_id=ctx.guild.id)
                if getjoin is None:
                    newjoin = Join.create(guild_id=ctx.guild.id, role_id=role.id, settings=settings)
                else:
                    delete = Join.get(Join.guild_id == ctx.guild.id)
                    delete.delete_instance()
                    newjoin = Join.create(guild_id=ctx.guild.id, role_id=role.id, settings=settings)
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is not None:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == "ru":
                            role_emb = discord.Embed(
                                title="Новая роль успешно установлена",
                                color=0x39d0d6)
                            await ctx.respond(embed=role_emb)
                        else:
                            role_emb = discord.Embed(
                                title="The new role has been successfully installed",
                                color=0x39d0d6)
                            await ctx.respond(embed=role_emb)
                else:
                    role_emb = discord.Embed(
                        title="The new role has been successfully installed",
                        color=0x39d0d6)
                    await ctx.respond(embed=role_emb)

    @commands.slash_command(name="muterole", description="sets mute role for your server")
    @commands.has_permissions(administrator=True)
    async def muterole(self, ctx, settings: discord.Option(str, choices=[
        discord.OptionChoice(name="on", value="on", name_localizations=None),
        discord.OptionChoice(name="off", value="off", name_localizations=None)]), role: discord.Role = None):
        if role is None:
            if settings == 'on':
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is not None:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == "ru":
                            role_emb = discord.Embed(
                                title="⚠Пожалуйста укажите роль!⚠",
                                color=0x39d0d6)
                            await ctx.respond(embed=role_emb)
                        else:
                            role_emb = discord.Embed(
                                title="⚠Please specify the role!⚠",
                                color=0x39d0d6)
                            await ctx.respond(embed=role_emb)
                else:
                    role_emb = discord.Embed(
                        title="⚠Please specify the role!⚠",
                        color=0x39d0d6)
                    await ctx.respond(embed=role_emb)
            else:
                getmute = Mute.get_or_none(guild_id=ctx.guild.id)
                if getmute is None:
                    newmute = Mute.create(guild_id=ctx.guild.id, role_id='0', settings=settings)
                else:
                    delete = Mute.get(Mute.guild_id == ctx.guild.id)
                    delete.delete_instance()
                    newmute = Mute.create(guild_id=ctx.guild.id, role_id='0', settings=settings)
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is not None:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == "ru":
                            role_emb = discord.Embed(
                                title="Функция успешно отключена",
                                color=0x39d0d6)
                            await ctx.respond(embed=role_emb)
                        else:
                            role_emb = discord.Embed(
                                title="The function has been successfully disabled",
                                color=0x39d0d6)
                            await ctx.respond(embed=role_emb)
                else:
                    role_emb = discord.Embed(
                        title="The function has been successfully disabled",
                        color=0x39d0d6)
                    await ctx.respond(embed=role_emb)
        elif role is not None:
            if ctx.guild.me.top_role <= role:
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is not None:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == "ru":
                            em = discord.Embed(title="⚠У бота недостаточно прав⚠",
                                               description='Роль бота находится ниже или равна указанной вами роли. Бот не сможет выдавать роли пользователям стоящим по иерархии выше него.',
                                               color=0x39d0d6)
                            await ctx.respond(embed=em)
                        else:
                            em = discord.Embed(title="⚠The bot doesn't have enough permissions⚠",
                                               description='The role of the bot is below or equal to the role you specified. The bot will not be able to assign roles to users standing in the hierarchy above it.',
                                               color=0x39d0d6)
                            await ctx.respond(embed=em)
                else:
                    em = discord.Embed(title="⚠The bot doesn't have enough permissions⚠",
                                       description='The role of the bot is below or equal to the role you specified. The bot will not be able to assign roles to users standing in the hierarchy above it.',
                                       color=0x39d0d6)
                    await ctx.respond(embed=em)
            else:
                getmute = Mute.get_or_none(guild_id=ctx.guild.id)
                if getmute is None:
                    newmute = Mute.create(guild_id=ctx.guild.id, role_id=role.id, settings=settings)
                else:
                    delete = Mute.get(Mute.guild_id == ctx.guild.id)
                    delete.delete_instance()
                    newmute = Mute.create(guild_id=ctx.guild.id, role_id=role.id, settings=settings)
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is not None:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == "ru":
                            role_emb = discord.Embed(
                                title="Новая роль успешно установлена",
                                color=0x39d0d6)
                            await ctx.respond(embed=role_emb)
                        else:
                            role_emb = discord.Embed(
                                title="The new role has been successfully installed",
                                color=0x39d0d6)
                            await ctx.respond(embed=role_emb)
                else:
                    role_emb = discord.Embed(
                        title="The new role has been successfully installed",
                        color=0x39d0d6)
                    await ctx.respond(embed=role_emb)

    @commands.slash_command(name="mute", description="mutes specified user")
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, user: discord.Member, *, reason=None):
        getmute = Mute.get_or_none(guild_id=ctx.guild.id)
        if getmute is None:
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is not None:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == "ru":
                        role_emb = discord.Embed(
                            title="⚠У вас нету установленной роли для данной функции⚠",
                            color=0x39d0d6)
                        await ctx.respond(embed=role_emb)
                    else:
                        role_emb = discord.Embed(
                            title="⚠You don't have an established role for this function⚠",
                            color=0x39d0d6)
                        await ctx.respond(embed=role_emb)
            else:
                role_emb = discord.Embed(
                    title="⚠You don't have an established role for this function⚠",
                    color=0x39d0d6)
                await ctx.respond(embed=role_emb)
        else:
            for mute in Mute.select().where(Mute.guild_id == ctx.guild.id):
                if mute.settings == 'off':
                    getlang = Language.get_or_none(guild_id=ctx.guild.id)
                    if getlang is not None:
                        for language in Language.select().where(Language.guild_id == ctx.guild.id):
                            if language.lang == "ru":
                                role_emb = discord.Embed(
                                    title="⚠Эта команда не включена на данном сервере⚠",
                                    color=0x39d0d6)
                                await ctx.respond(embed=role_emb)
                            else:
                                role_emb = discord.Embed(
                                    title="⚠This command is not enabled in this server⚠",
                                    color=0x39d0d6)
                                await ctx.respond(embed=role_emb)
                    else:
                        role_emb = discord.Embed(
                            title="⚠This command is not enabled in this server⚠",
                            color=0x39d0d6)
                        await ctx.respond(embed=role_emb)
                else:
                    role = ctx.guild.get_role(mute.role_id)
                    await user.add_roles(role)
                    getlang = Language.get_or_none(guild_id=ctx.guild.id)
                    if getlang is not None:
                        for language in Language.select().where(Language.guild_id == ctx.guild.id):
                            if language.lang == "ru":
                                role_emb = discord.Embed(
                                    title=f"Пользователю был выдан мут, причина: {reason}",
                                    color=0x39d0d6)
                                await ctx.respond(embed=role_emb)
                            else:
                                role_emb = discord.Embed(
                                    title=f"The user was issued a mutation, reason: {reason}",
                                    color=0x39d0d6)
                                await ctx.respond(embed=role_emb)
                    else:
                        role_emb = discord.Embed(
                            title=f"The user was issued a mutation, reason: {reason}",
                            color=0x39d0d6)
                        await ctx.respond(embed=role_emb)

    @commands.slash_command(name="settings", description="shows your server settings")
    @commands.has_permissions(administrator=True)
    async def settings(self, ctx):
        getmute = Mute.get_or_none(guild_id=ctx.guild.id)
        if getmute is None:
            m_set = '❌off'
            m_role = 'none'
        else:
            for mute in Mute.select().where(Mute.guild_id == ctx.guild.id):
                if mute.settings == 'off':
                    m_set = '❌off'
                    m_role = 'none'
                else:
                    m_set = '✅on'
                    m_role = ctx.guild.get_role(mute.role_id)
        getjoin = Join.get_or_none(guild_id=ctx.guild.id)
        if getjoin is None:
            j_set = '❌off'
            j_role = 'none'
        else:
            for join in Join.select().where(Join.guild_id == ctx.guild.id):
                if join.settings == 'off':
                    j_set = '❌off'
                    j_role = 'none'
                else:
                    j_set = '✅on'
                    j_role = ctx.guild.get_role(join.role_id)
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is not None:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    settings = discord.Embed(title='⚙Настройки сервера', colour=0x39d0d6)
                    settings.add_field(name='⚙мут:', value=m_set, inline=False)
                    settings.add_field(name='💾мутроль:', value=m_role, inline=False)
                    settings.add_field(name='⚙роль при присоединении:', value=j_set, inline=False)
                    settings.add_field(name='💾приветственная роль:', value=j_role, inline=False)
                    settings.add_field(name='💾язык:', value='ru', inline=False)
                    await ctx.respond(embed=settings)
                else:
                    settings = discord.Embed(title='⚙Server settings', colour=0x39d0d6)
                    settings.add_field(name='⚙mute:', value=m_set, inline=False)
                    settings.add_field(name='💾muterole:', value=m_role, inline=False)
                    settings.add_field(name='⚙role-on-join:', value=j_set, inline=False)
                    settings.add_field(name='💾joinrole:', value=j_role, inline=False)
                    settings.add_field(name='💾language:', value='en', inline=False)
                    await ctx.respond(embed=settings)
        else:
            settings = discord.Embed(title='⚙Server settings', colour=0x39d0d6)
            settings.add_field(name='⚙mute:', value=m_set, inline=False)
            settings.add_field(name='💾muterole:', value=m_role, inline=False)
            settings.add_field(name='⚙role-on-join:', value=j_set, inline=False)
            settings.add_field(name='💾joinrole:', value=j_role, inline=False)
            settings.add_field(name='💾language:', value='en', inline=False)
            await ctx.respond(embed=settings)

    @commands.slash_command(name="ticketrole", description="set the role for ticket maintenance")
    @commands.has_permissions(administrator=True)
    async def ticketrole(self, ctx, role: discord.Role):
        getticketrole = TicketRole.get_or_none(guild_id=ctx.guild.id)
        if getticketrole is None:
            newticketrole = TicketRole.create(guild_id=ctx.guild.id, role_id=role.id)
        else:
            delete = TicketRole.get(TicketRole.guild_id == ctx.guild.id)
            delete.delete_instance()
            newticketrole = TicketRole.create(guild_id=ctx.guild.id, role_id=role.id)
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is not None:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    role_emb = discord.Embed(
                        title="Роль для обслуживания тикетов была успешно добавлена",
                        color=0x39d0d6)
                    await ctx.respond(embed=role_emb)
                else:
                    role_emb = discord.Embed(
                        title="The role for ticket maintenance has been successfully added",
                        color=0x39d0d6)
                    await ctx.respond(embed=role_emb)
        else:
            role_emb = discord.Embed(
                title="The role for ticket maintenance has been successfully added.",
                color=0x39d0d6)
            await ctx.respond(embed=role_emb)

    @commands.slash_command(name="open", description="open the new support ticket")
    async def open(self, ctx, *, reason):
        getticketrole = TicketRole.get_or_none(guild_id=ctx.guild.id)
        if getticketrole is None:
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is not None:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == "ru":
                        ticket_emb = discord.Embed(
                            title="⚠Роль для обслуживания тикетов не указана для этого сервера!⚠",
                            color=0x39d0d6)
                        await ctx.respond(embed=ticket_emb)
                    else:
                        ticket_emb = discord.Embed(
                            title="⚠The ticket maintenance role is not specified for this server!⚠",
                            color=0x39d0d6)
                        await ctx.respond(embed=ticket_emb)
            else:
                ticket_emb = discord.Embed(
                    title="⚠The ticket maintenance role is not specified for this server!⚠",
                    color=0x39d0d6)
                await ctx.respond(embed=ticket_emb)
        else:
            getticket = Ticket.get_or_none(guild_id=ctx.guild.id)
            if getticket is None:
                newticket = Ticket.create(guild_id=ctx.guild.id, index='0')
                for ticketrole in TicketRole.select().where(TicketRole.guild_id == ctx.guild.id):
                    overwrites = {
                        ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                        ctx.guild.me: discord.PermissionOverwrite(read_messages=True),
                        ctx.guild.get_role(ticketrole.role_id): discord.PermissionOverwrite(read_messages=True),
                        ctx.author: discord.PermissionOverwrite(read_messages=True)
                    }
                    channel = await ctx.guild.create_text_channel(f'Ticket 0', overwrites=overwrites)
                    getlang = Language.get_or_none(guild_id=ctx.guild.id)
                    if getlang is not None:
                        for language in Language.select().where(Language.guild_id == ctx.guild.id):
                            if language.lang == "ru":
                                ticket_emb = discord.Embed(
                                    title=reason,
                                    color=0x39d0d6)
                                ticket_emb.add_field(name=f"Вы открыли новый тикет, индекс: [0]",
                                                     value="Проверяющий вскоре рассмотрит вашу заявку")
                                await channel.send(embed=ticket_emb, view=ticket_conf_ru())
                            else:
                                ticket_emb = discord.Embed(
                                    title=reason,
                                    color=0x39d0d6)
                                ticket_emb.add_field(name=f"You opened new ticket, index: [0]",
                                                     value="The inspector will soon review your application")
                                await channel.send(embed=ticket_emb, view=ticket_conf_en())
                    else:
                        ticket_emb = discord.Embed(
                            title=reason,
                            color=0x39d0d6)
                        ticket_emb.add_field(name=f"You opened new ticket, index: [0]",
                                             value="The inspector will soon review your application")
                        await channel.send(embed=ticket_emb, view=ticket_conf_en())
            else:
                max_index = Ticket.select(fn.MAX(Ticket.index)).scalar()
                new_index = max_index + 1
                newticket = Ticket.create(guild_id=ctx.guild.id, index=new_index)
                for ticketrole in TicketRole.select().where(TicketRole.guild_id == ctx.guild.id):
                    overwrites = {
                        ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                        ctx.guild.me: discord.PermissionOverwrite(read_messages=True),
                        ctx.guild.get_role(ticketrole.role_id): discord.PermissionOverwrite(read_messages=True),
                        ctx.author: discord.PermissionOverwrite(read_messages=True)
                    }
                    channel = await ctx.guild.create_text_channel(f'Ticket {new_index}', overwrites=overwrites)
                    getlang = Language.get_or_none(guild_id=ctx.guild.id)
                    if getlang is not None:
                        for language in Language.select().where(Language.guild_id == ctx.guild.id):
                            if language.lang == "ru":
                                ticket_emb = discord.Embed(
                                    title=reason,
                                    color=0x39d0d6)
                                ticket_emb.add_field(name=f"Вы открыли новый тикет, индекс: [{new_index}]",
                                                     value="Проверяющий вскоре рассмотрит вашу заявку")
                                await channel.send(embed=ticket_emb, view=ticket_conf_ru())
                            else:
                                ticket_emb = discord.Embed(
                                    title=reason,
                                    color=0x39d0d6)
                                ticket_emb.add_field(name=f"You opened new ticket, index: [{new_index}]",
                                                     value="The inspector will soon review your application")
                                await channel.send(embed=ticket_emb, view=ticket_conf_en())
                    else:
                        ticket_emb = discord.Embed(
                            title=reason,
                            color=0x39d0d6)
                        ticket_emb.add_field(name=f"You opened new ticket, index: [{new_index}]",
                                             value="The inspector will soon review your application")
                        await channel.send(embed=ticket_emb, view=ticket_conf_en())
                    getlang = Language.get_or_none(guild_id=ctx.guild.id)
                    if getlang is not None:
                        for language in Language.select().where(Language.guild_id == ctx.guild.id):
                            if language.lang == "ru":
                                role_emb = discord.Embed(
                                    title="Тикет был успешно создан",
                                    color=0x39d0d6)
                                await ctx.respond(embed=role_emb)
                            else:
                                role_emb = discord.Embed(
                                    title="Ticket was successfully created",
                                    color=0x39d0d6)
                                await ctx.respond(embed=role_emb)
                    else:
                        role_emb = discord.Embed(
                            title="Ticket was successfully created",
                            color=0x39d0d6)
                        await ctx.respond(embed=role_emb)

    @commands.slash_command(name="logschan", description="set channel for server logs")
    @commands.has_permissions(administrator=True)
    async def logschan(self, ctx, settings: discord.Option(str, choices=[
        discord.OptionChoice(name="on", value="on", name_localizations=None),
        discord.OptionChoice(name="off", value="off", name_localizations=None)]), channel: discord.TextChannel = None):
        if channel is None:
            if settings == 'on':
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is not None:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == "ru":
                            log_emb = discord.Embed(
                                title="⚠Пожалуйста укажите канал!⚠",
                                color=0x39d0d6)
                            await ctx.respond(embed=log_emb)
                        else:
                            log_emb = discord.Embed(
                                title="⚠Please specify the channel!⚠",
                                color=0x39d0d6)
                            await ctx.respond(embed=log_emb)
                else:
                    log_emb = discord.Embed(
                        title="⚠Please specify the channel!⚠",
                        color=0x39d0d6)
                    await ctx.respond(embed=log_emb)
            else:
                getlogs = Logs.get_or_none(guild_id=ctx.guild.id)
                if getlogs is None:
                    newlogs = Logs.create(guild_id=ctx.guild.id, settings="off", channel_id="0")
                else:
                    delete = Logs.get(Logs.guild_id == ctx.guild.id)
                    delete.delete_instance()
                    newlogs = Logs.create(guild_id=ctx.guild.id, settings="off", channel_id="0")
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is not None:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == "ru":
                            log_emb = discord.Embed(
                                title="Функция успешно отключена",
                                color=0x39d0d6)
                            await ctx.respond(embed=log_emb)
                        else:
                            log_emb = discord.Embed(
                                title="The function has been successfully disabled",
                                color=0x39d0d6)
                            await ctx.respond(embed=log_emb)
                else:
                    log_emb = discord.Embed(
                        title="The function has been successfully disabled",
                        color=0x39d0d6)
                    await ctx.respond(embed=log_emb)
        else:
            if settings == 'on':
                getlogs = Logs.get_or_none(guild_id=ctx.guild.id)
                if getlogs is None:
                    newlogs = Logs.create(guild_id=ctx.guild.id, settings="on", channel_id=channel.id)
                else:
                    delete = Logs.get(Logs.guild_id == ctx.guild.id)
                    delete.delete_instance()
                    newlogs = Logs.create(guild_id=ctx.guild.id, settings="on", channel_id=channel.id)
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is not None:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == "ru":
                            log_emb = discord.Embed(
                                title="Функция успешно включена",
                                color=0x39d0d6)
                            await ctx.respond(embed=log_emb)
                        else:
                            log_emb = discord.Embed(
                                title="The function has been successfully enabled",
                                color=0x39d0d6)
                            await ctx.respond(embed=log_emb)
                else:
                    log_emb = discord.Embed(
                        title="The function has been successfully enabled",
                        color=0x39d0d6)
                    await ctx.respond(embed=log_emb)
            else:
                getlogs = Logs.get_or_none(guild_id=ctx.guild.id)
                if getlogs is None:
                    newlogs = Logs.create(guild_id=ctx.guild.id, settings="off", channel_id="0")
                else:
                    delete = Logs.get(Logs.guild_id == ctx.guild.id)
                    delete.delete_instance()
                    newlogs = Logs.create(guild_id=ctx.guild.id, settings="off", channel_id="0")
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is not None:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == "ru":
                            log_emb = discord.Embed(
                                title="Функция успешно отключена",
                                color=0x39d0d6)
                            await ctx.respond(embed=log_emb)
                        else:
                            log_emb = discord.Embed(
                                title="The function has been successfully disabled",
                                color=0x39d0d6)
                            await ctx.respond(embed=log_emb)
                else:
                    log_emb = discord.Embed(
                        title="The function has been successfully disabled",
                        color=0x39d0d6)
                    await ctx.respond(embed=log_emb)

def setup(bot):
    bot.add_cog(Mod(bot))