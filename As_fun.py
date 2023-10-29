import discord
from discord.ext import commands
import json
import requests
import random
from random import choice
import sqlite3
import peewee
from peewee import *
from Aurix_base import Language

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="fox", description="random picture of a cute fox🦊")
    async def fox(self, ctx):
        response = requests.get('https://some-random-api.ml/img/fox')
        json_fox = json.loads(response.text)
        embed = discord.Embed(color=0xff9900, title='Random Fox')
        embed.set_image(url=json_fox['link'])
        await ctx.response.defer()
        await ctx.followup.send(embed=embed)

    @commands.slash_command(name="cat", description="random picture of a cute cat🐱")
    async def cat(self, ctx):
        response = requests.get('https://some-random-api.ml/img/cat')
        json_cat = json.loads(response.text)
        embed = discord.Embed(color=0xff9900, title='Random Cat')
        embed.set_image(url=json_cat['link'])
        await ctx.response.defer()
        await ctx.followup.send(embed=embed)

    @commands.slash_command(name="roll", description="rolls a dice")
    async def roll(self, ctx, number_of_dice: int, number_of_sides: int):
        if number_of_dice > 50:
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is not None:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == "ru":
                        sum_emb = discord.Embed(
                            title='⚠Максимальное числовое значение: 50⚠',
                            color=0x39d0d6)
                        await ctx.respond(embed=sum_emb)
                    else:
                        sum_emb = discord.Embed(
                            title='⚠Maximum numeric value: 50⚠',
                            color=0x39d0d6)
                        await ctx.respond(embed=sum_emb)
            else:
                sum_emb = discord.Embed(
                    title='⚠Maximum numeric value: 50⚠',
                    color=0x39d0d6)
                await ctx.respond(embed=sum_emb)
        elif number_of_sides > 50:
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is not None:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == "ru":
                        sum_emb = discord.Embed(
                            title='⚠Максимальное числовое значение: 50⚠',
                            color=0x39d0d6)
                        await ctx.respond(embed=sum_emb)
                    else:
                        sum_emb = discord.Embed(
                            title='⚠Maximum numeric value: 50⚠',
                            color=0x39d0d6)
                        await ctx.respond(embed=sum_emb)
            else:
                sum_emb = discord.Embed(
                    title='⚠Maximum numeric value: 50⚠',
                    color=0x39d0d6)
                await ctx.respond(embed=sum_emb)
        else:
            dice = [
                str(random.choice(range(1, number_of_sides + 1)))
                for _ in range(number_of_dice)
            ]
            dice_emb = discord.Embed(
                title=', '.join(dice),
                color=0x39d0d6)
            await ctx.respond(embed=dice_emb)

    @commands.slash_command(name="hug", description="hugs mentioned user")
    async def hug(self, ctx, user: discord.Member):
        if user == bot.user:
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is not None:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == "ru":
                        hug_emb = discord.Embed(
                            title=f"⚠Укажите пользователя не являющегося ботом!⚠",
                            color=0x39d0d6)
                        await ctx.respond(embed=hug_emb)
                    else:
                        hug_emb = discord.Embed(
                            title=f"⚠Specify a non-bot user!⚠",
                            color=0x39d0d6)
                        await ctx.respond(embed=hug_emb)
            else:
                hug_emb = discord.Embed(
                    title=f"⚠Specify a non-bot user!⚠",
                    color=0x39d0d6)
                await ctx.respond(embed=hug_emb)
        else:
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is not None:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == "ru":
                        hug_emb = discord.Embed(
                            title=f"😻{ctx.author.name} обнял {user.name}!",
                            color=0x39d0d6)
                        await ctx.respond(embed=hug_emb)
                    else:
                        hug_emb = discord.Embed(
                            title=f"😻{ctx.author.name} hugged {user.name}!",
                            color=0x39d0d6)
                        await ctx.respond(embed=hug_emb)
            else:
                hug_emb = discord.Embed(
                    title=f"😻{ctx.author.name} hugged {user.name}!",
                    color=0x39d0d6)
                await ctx.respond(embed=hug_emb)

    @commands.slash_command(name="sum", description="sums two mentioned numbers")
    async def sum(self, ctx, a: int, b: int):
        if a > 1000:
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is not None:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == "ru":
                        sum_emb = discord.Embed(
                            title='⚠Максимальное числовое значение: 1000⚠',
                            color=0x39d0d6)
                        await ctx.respond(embed=sum_emb)
                    else:
                        sum_emb = discord.Embed(
                            title='⚠Maximum numeric value: 1000⚠',
                            color=0x39d0d6)
                        await ctx.respond(embed=sum_emb)
            else:
                sum_emb = discord.Embed(
                    title='⚠Maximum numeric value: 1000⚠',
                    color=0x39d0d6)
                await ctx.respond(embed=sum_emb)
        elif b > 1000:
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is not None:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == "ru":
                        sum_emb = discord.Embed(
                            title='⚠Максимальное числовое значение: 1000⚠',
                            color=0x39d0d6)
                        await ctx.respond(embed=sum_emb)
                    else:
                        sum_emb = discord.Embed(
                            title='⚠Maximum numeric value: 1000⚠',
                            color=0x39d0d6)
                        await ctx.respond(embed=sum_emb)
            else:
                sum_emb = discord.Embed(
                    title='⚠Maximum numeric value: 1000⚠',
                    color=0x39d0d6)
                await ctx.respond(embed=sum_emb)
        else:
            sum = a + b
            sum_emb = discord.Embed(
                title=sum,
                color=0x39d0d6)
            await ctx.respond(embed=sum_emb)

    @commands.slash_command(name="choice", description="Aurix will answer 'yes' or 'no'")
    async def choice(self, ctx):
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is not None:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    from random import choice
                    answer = choice(['да', 'нет'])
                    choice_emb = discord.Embed(
                        title=answer,
                        color=0x39d0d6)
                    await ctx.respond(embed=choice_emb)
                else:
                    from random import choice
                    answer = choice(['yes', 'no'])
                    choice_emb = discord.Embed(
                        title=answer,
                        color=0x39d0d6)
                    await ctx.respond(embed=choice_emb)
        else:
            from random import choice
            answer = choice(['yes', 'no'])
            choice_emb = discord.Embed(
                title=answer,
                color=0x39d0d6)
            await ctx.respond(embed=choice_emb)

    @commands.slash_command(name="play_with", description="ask user to play with you")
    async def play_with(self, ctx, user: discord.Member, *, game=None):
        if game is None:
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is not None:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == "ru":
                        play_emb = discord.Embed(
                            title="⚠Вы не указали игру в которую хотите сыграть⚠",
                            color=0x39d0d6)
                        await ctx.respond(embed=play_emb)
                    else:
                        play_emb = discord.Embed(
                            title="⚠You have not specified the game you would like to play⚠",
                            color=0x39d0d6)
                        await ctx.respond(embed=play_emb)
            else:
                play_emb = discord.Embed(
                    title="⚠You have not specified the game you would like to play⚠",
                    color=0x39d0d6)
                await ctx.respond(embed=play_emb)
        else:
            if user.id == ctx.author.id:
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is not None:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == "ru":
                            play_emb = discord.Embed(
                                title="⚠Вы не можете отправить сообщение себе же!⚠",
                                color=0x39d0d6)
                            await ctx.respond(embed=play_emb)
                        else:
                            play_emb = discord.Embed(
                                title="⚠You can't send a message to yourself!⚠",
                                color=0x39d0d6)
                            await ctx.respond(embed=play_emb)
                else:
                    play_emb = discord.Embed(
                        title="⚠You can't send a message to yourself!⚠",
                        color=0x39d0d6)
                    await ctx.respond(embed=play_emb)
            else:
                if user.bot:
                    getlang = Language.get_or_none(guild_id=ctx.guild.id)
                    if getlang is not None:
                        for language in Language.select().where(Language.guild_id == ctx.guild.id):
                            if language.lang == "ru":
                                play_emb = discord.Embed(
                                    title="⚠Вы не можете отправить сообщение боту!⚠",
                                    color=0x39d0d6)
                                await ctx.respond(embed=play_emb)
                            else:
                                play_emb = discord.Embed(
                                    title="⚠You can't send a message to a bot!⚠",
                                    color=0x39d0d6)
                                await ctx.respond(embed=play_emb)
                    else:
                        play_emb = discord.Embed(
                            title="⚠You can't send a message to a bot!⚠",
                            color=0x39d0d6)
                        await ctx.respond(embed=play_emb)
                else:
                    getlang = Language.get_or_none(guild_id=ctx.guild.id)
                    if getlang is not None:
                        for language in Language.select().where(Language.guild_id == ctx.guild.id):
                            if language.lang == "ru":
                                channel = await user.create_dm()
                                play_emb = discord.Embed(
                                    title=f"🕹Пользователь {ctx.author} хочет сыграть с вами в игру {game}",
                                    color=0x39d0d6)
                                await channel.send(embed=play_emb)
                            else:
                                channel = await user.create_dm()
                                play_emb = discord.Embed(
                                    title=f"🕹User {ctx.author} wants to play a game called {game} with you",
                                    color=0x39d0d6)
                                await channel.send(embed=play_emb)
                    else:
                        channel = await user.create_dm()
                        play_emb = discord.Embed(
                            title=f"🕹User {ctx.author} wants to play a game called {game} with you",
                            color=0x39d0d6)
                        await channel.send(embed=play_emb)
                    getlang = Language.get_or_none(guild_id=ctx.guild.id)
                    if getlang is not None:
                        for language in Language.select().where(Language.guild_id == ctx.guild.id):
                            if language.lang == "ru":
                                play_emb = discord.Embed(
                                    title="Пользователь успешно получил сообщение",
                                    color=0x39d0d6)
                                await ctx.respond(embed=play_emb)
                            else:
                                play_emb = discord.Embed(
                                    title="User successfully got message",
                                    color=0x39d0d6)
                                await ctx.respond(embed=play_emb)
                    else:
                        play_emb = discord.Embed(
                            title="User successfully got message",
                            color=0x39d0d6)
                        await ctx.respond(embed=play_emb)

def setup(bot):
    bot.add_cog(Fun(bot))