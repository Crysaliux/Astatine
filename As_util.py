import discord
from discord.ext import commands
import random
from random import choice
import sqlite3
import peewee
from peewee import *
from Aurix_base import Language

class Util(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="print", description="prints your message")
    @commands.has_permissions(manage_messages=True)
    async def print(self, ctx, *, text: str):
        print_emb = discord.Embed(
            title=text,
            color=0x39d0d6)
        await ctx.respond(embed=print_emb)

    @commands.slash_command(name="create_channel", description="creates new server channel")
    @commands.has_permissions(administrator=True)
    async def create_channel(self, ctx, *, name):
        await ctx.guild.create_text_channel(name)
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is not None:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    channel_emb = discord.Embed(
                        title=f"Канал {name} был успешно создан",
                        color=0x39d0d6)
                    await ctx.respond(embed=channel_emb)
                else:
                    channel_emb = discord.Embed(
                        title=f"Channel {name} was successfuly created",
                        color=0x39d0d6)
                    await ctx.respond(embed=channel_emb)
        else:
            channel_emb = discord.Embed(
                title=f"Channel {name} was successfuly created",
                color=0x39d0d6)
            await ctx.respond(embed=channel_emb)

    @commands.slash_command(name="github", description="link to our github page")
    async def github(self, ctx):
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is not None:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    git_emb = discord.Embed(
                        title=f"Ссылка на наш гит хаб: https://github.com/Crysaliux/Aurix-bot.git",
                        color=0x39d0d6)
                    await ctx.respond(embed=git_emb)
                else:
                    git_emb = discord.Embed(
                        title=f"link to our github page: https://github.com/Crysaliux/Aurix-bot.git",
                        color=0x39d0d6)
                    await ctx.respond(embed=git_emb)
        else:
            git_emb = discord.Embed(
                title=f"link to our github page: https://github.com/Crysaliux/Aurix-bot.git",
                color=0x39d0d6)
            await ctx.respond(embed=git_emb)

    @commands.slash_command(name="wikifur", description="The last updates on wikifur")
    async def wikifur(self, ctx):
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is not None:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == "ru":
                    wiki_emb = discord.Embed(
                        title=f"Последние публикации викифура: https://ru.wikifur.com/wiki/",
                        color=0x39d0d6)
                    await ctx.respond(embed=wiki_emb)
                else:
                    wiki_emb = discord.Embed(
                        title=f"The last updates on wikifur: https://ru.wikifur.com/wiki/",
                        color=0x39d0d6)
                    await ctx.respond(embed=wiki_emb)
        else:
            wiki_emb = discord.Embed(
                title=f"The last updates on wikifur: https://ru.wikifur.com/wiki/",
                color=0x39d0d6)
            await ctx.respond(embed=wiki_emb)

def setup(bot):
    bot.add_cog(Util(bot))