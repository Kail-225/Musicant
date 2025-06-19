import discord, locale, os
from discord.ext import commands
from asyncio import *
from datetime import datetime, timedelta
from boot import *
locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')
Play=True
vc=None
id_t=0
Traks=["Royalty2","Прощание2","Faster_n_harder2"]
covers=["Kiss_of_death2","Katyusha2","Suzume2","Hope_Is_the_Thing_with_Feathers2","Idol2","Starfall2","White_Night2","Wildfire2"]
gsounds=["Earth2","La_vaguelette2","Honor_for_all2","Take_the_Journey2","Rogue_Main_Theme2"]
ssounds=["Main_Title2","Janissary_Song_12","Janissary_Song_22","Deepest_Love2"]
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
        #print(c_time.strftime('%A'))
        await discord.VoiceClient.disconnect(a)
def setup(bot):
    @bot.slash_command(name='play',description='воспроизведение музыки')
    async def play(ctx):
        global id_t,vc
        await ctx.respond("Очередь запущена")
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
    @bot.slash_command(name='test',description='тестовый режим')
    async def test(ctx):
        if os.name=="nt":
            global id_t,vc
            try:
                voice_channel=None
                if ctx.guild.name=="Столица Агелия":
                    voice_channel = discord.utils.get(ctx.guild.voice_channels,name="Улица")
                elif ctx.guild.name=="Сервер для тестов":
                    voice_channel = discord.utils.get(ctx.guild.voice_channels,name="Основной")
                vc = await voice_channel.connect()
                while Play==True:
                    all=Traks+covers+gsounds+ssounds
                    audio_source = discord.FFmpegPCMAudio(
                        executable=path,
                        source=f"{tpath}{all[id_t]}.mp3",
                        options="-vn"
                        )
                    await bot.change_presence(status="Запущен тестовый режим")
                    vc.play(audio_source)
                    while vc.is_playing() or vc.is_paused():
                        await sleep(1)
                    id_t+=1
                    if id_t==len(all):
                        break
                await discord.VoiceClient.disconnect(vc)
            except Exception as e:
                await ctx.respond(f"Произошла ошибка: {e}")
        else:
            await ctx.respond("Запуск тестового режима не возможен вне системы владельца")