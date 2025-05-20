import discord, json, locale
from discord.ext import commands
from asyncio import *
from datetime import datetime, timedelta
from boot import player
locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')
Play=True
vc=None
id_t=0
Traks=["тест","Royalty"]
covers=["Kiss_of_death","Katyusha","Suzume"]
gsounds=["Earth","La_vaguelette","Main_Theme","Take_the_Journey","Rogue_Main_Theme"]
ssounds=["Main_Title","Janissary_Song_1","Janissary_Song_2","Deepest_Love"]
path=player()
async def sound(a,bot):
    global Play, id_t
    c_time=datetime.now()+timedelta(hours=3)
    id=id_t
    if Play==True:
        if c_time.strftime('%A').capitalize()=="Пятница":
            if id==len(gsounds):
                id_t,id=0,0
                audio_source = discord.FFmpegPCMAudio(
                    executable=path,
                    source=f"gsound/{gsounds[id]}.mp3",
                    options="-vn"
                    )
                await bot.change_presence(activity=discord.Game(name=f"День игровых саундтреков. Играет {gsounds[id]}"))
                a.play(audio_source)
            else:
                audio_source = discord.FFmpegPCMAudio(
                    executable=path,
                    source=f"gsound/{gsounds[id]}.mp3",
                    options="-vn"
                    )
                await bot.change_presence(activity=discord.Game(name=f"День игровых саундтреков. Играет {gsounds[id]}"))
                a.play(audio_source)
        if c_time.strftime('%A').capitalize()=="Вторник":
            if id==len(gsounds):
                id_t,id=0,0
                audio_source = discord.FFmpegPCMAudio(
                    executable=path,
                    source=f"gsound/{gsounds[id]}.mp3",
                    options="-vn"
                    )
                await bot.change_presence(activity=discord.Game(name=f"День игровых саундтреков. Играет {gsounds[id]}"))
                a.play(audio_source)
            else:
                audio_source = discord.FFmpegPCMAudio(
                    executable=path,
                    source=f"gsound/{gsounds[id]}.mp3",
                    options="-vn"
                )
                await bot.change_presence(activity=discord.Game(name=f"День игровых саундтреков. Играет {gsounds[id]}"))
                a.play(audio_source)
        if c_time.strftime('%A').capitalize()=="Среда":
            if id==len(covers):
                id_t,id=0,0
                audio_source = discord.FFmpegPCMAudio(
                    executable=path,
                    source=f"covers/{covers[id]}.mp3",
                    options="-vn"
                )
                await bot.change_presence(activity=discord.Game(name=f"День каверов. Играет {covers[id]}"))
                a.play(audio_source)
            else:
                audio_source = discord.FFmpegPCMAudio(
                    executable=path,
                    source=f"covers/{covers[id]}.mp3",
                    options="-vn"
                )
                await bot.change_presence(activity=discord.Game(name=f"День каверов. Играет {covers[id]}"))
                a.play(audio_source)
        if c_time.strftime('%A').capitalize()=="Воскресенье":
            if id==len(ssounds):
                id_t,id=0,0
                audio_source = discord.FFmpegPCMAudio(
                    executable=path,
                    source=f"ssound/{ssounds[id]}.mp3",
                    options="-vn"
                )
                await bot.change_presence(activity=discord.Game(name=f"День сериальных песен. Играет {ssounds[id]}"))
                a.play(audio_source)
            else:
                audio_source = discord.FFmpegPCMAudio(
                    executable=path,
                    source=f"ssound/{ssounds[id]}.mp3",
                    options="-vn"
                )
                await bot.change_presence(activity=discord.Game(name=f"День сериальных песен. Играет {ssounds[id]}"))
                a.play(audio_source)
        if c_time.strftime('%A').capitalize()=="Суббота":
            if id==len(Traks):
                id_t,id=0,0
                audio_source = discord.FFmpegPCMAudio( 
                    executable=path,
                    source=f"traks/{Traks[id]}.mp3",
                    options="-vn"
                )
                await bot.change_presence(activity=discord.Game(name=f"День треков. Играет {Traks[id]}"))
                a.play(audio_source)
            else:
                audio_source = discord.FFmpegPCMAudio(
                    executable=path,
                    source=f"traks/{Traks[id]}.mp3",
                    options="-vn"
                )
                await bot.change_presence(activity=discord.Game(name=f"День треков. Играет {Traks[id]}"))
                a.play(audio_source)
    else:
        print(c_time.strftime('%A'))
        await discord.VoiceClient.disconnect(a)
def setup(bot):
    @bot.slash_command(name='play',description='воспроизведение музыки')
    async def play(ctx):
        global id_t,vc
        print(ctx.guild.name)
        try:
            voice_channel=None
            if ctx.guild.name=="Столица Агелия":
                voice_channel = discord.utils.get(ctx.guild.voice_channels,name="Улица")
            elif ctx.guild.name=="Сервер для тестов":
                voice_channel = discord.utils.get(ctx.guild.voice_channels,name="Основной")
            vc = await voice_channel.connect()
            while Play==True:
                await sound(vc,bot)
                while vc.is_playing() or vc.is_paused():
                    await sleep(1)
                id_t+=1
        except Exception as e:
            await ctx.respond(f"Произошла ошибка: {e}")
    @bot.slash_command(name='finish',description='Завершение очереди')
    async def finish(ctx):
        global Play
        if Play==True:
            Play=False
            await ctx.respond("Очередь завершена")
            while vc.is_playing() or vc.is_paused():
                    await sleep(1)
            await sound(vc,bot)
        else:
            await ctx.respond("Невозможно завершить завершённую очередь")
