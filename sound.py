import discord, locale, os
from discord.ext import commands
from asyncio import *
from datetime import datetime
from boot import *
locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')
Play=True
vc=None
id_t=0
Traks=["Royalty1","Прощание1","Faster_n_harder1","Rave1","Dare1","Children_of_the_sky1"]
jsounds=["Suzume2","Shinunoga_E-wa2"]
covers=["Kiss_of_death1","Katyusha1","Suzume1","Hope_Is_the_Thing_with_Feathers1","Idol1","Starfall1","White_Night1","Wildfire1","Shinunoga_E-wa1","La_vaguelette1"]
gsounds=["Earth1","La_vaguelette2","Honor_for_all1","Take_the_Journey1","Rogue_Main_Theme1"]
ssounds=["Main_Title1","Janissary_Song_11","Janissary_Song_21","Deepest_Love1"]
path=player()
async def sound(a,bot):
    global Play, id_t
    c_time=datetime.now()
    id=id_t
    if Play==True:
        if c_time.strftime('%A').capitalize()=="Понедельник":
            if id==len(gsounds):
                id_t,id=0,0
                audio_source = discord.FFmpegPCMAudio(
                    executable=path,
                    source=f"jsound/{jsounds[id]}.mp3",
                    options="-vn"
                    )
                await bot.change_presence(activity=discord.CustomActivity(name=f"День японских песен. Играет {jsounds[id]}"))
                a.play(audio_source)
            else:
                audio_source = discord.FFmpegPCMAudio(
                    executable=path,
                    source=f"jsound/{jsounds[id]}.mp3",
                    options="-vn"
                )
                await bot.change_presence(activity=discord.CustomActivity(name=f"День японских. Играет {jsounds[id]}"))
                a.play(audio_source)
        if c_time.strftime('%A').capitalize()=="Вторник":
            if id==len(gsounds):
                id_t,id=0,0
                audio_source = discord.FFmpegPCMAudio(
                    executable=path,
                    source=f"gsound/{gsounds[id]}.mp3",
                    options="-vn"
                    )
                await bot.change_presence(activity=discord.CustomActivity(name=f"День игровых саундтреков. Играет {gsounds[id]}"))
                a.play(audio_source)
            else:
                audio_source = discord.FFmpegPCMAudio(
                    executable=path,
                    source=f"gsound/{gsounds[id]}.mp3",
                    options="-vn"
                )
                await bot.change_presence(activity=discord.CustomActivity(name=f"День игровых саундтреков. Играет {gsounds[id]}"))
                a.play(audio_source)
        if c_time.strftime('%A').capitalize()=="Среда":
            if id==len(covers):
                id_t,id=0,0
                audio_source = discord.FFmpegPCMAudio(
                    executable=path,
                    source=f"covers/{covers[id]}.mp3",
                    options="-vn"
                )
                await bot.change_presence(activity=discord.CustomActivity(name=f"День каверов. Играет {covers[id]}"))
                a.play(audio_source)
            else:
                audio_source = discord.FFmpegPCMAudio(
                    executable=path,
                    source=f"covers/{covers[id]}.mp3",
                    options="-vn"
                )
                await bot.change_presence(activity=discord.CustomActivity(name=f"День каверов. Играет {covers[id]}"))
                a.play(audio_source)
        if c_time.strftime('%A').capitalize()=="Четверг":
            if id==len(Traks):
                id_t,id=0,0
                audio_source = discord.FFmpegPCMAudio( 
                    executable=path,
                    source=f"traks/{Traks[id]}.mp3",
                    options="-vn"
                )
                await bot.change_presence(activity=discord.CustomActivity(name=f"День треков. Играет {Traks[id]}"))
                a.play(audio_source)
            else:
                audio_source = discord.FFmpegPCMAudio(
                    executable=path,
                    source=f"traks/{Traks[id]}.mp3",
                    options="-vn"
                )
        if c_time.strftime('%A').capitalize()=="Пятница":
            if id==len(gsounds):
                id_t,id=0,0
                audio_source = discord.FFmpegPCMAudio(
                    executable=path,
                    source=f"gsound/{gsounds[id]}.mp3",
                    options="-vn"
                    )
                await bot.change_presence(activity=discord.CustomActivity(name=f"День игровых саундтреков. Играет {gsounds[id]}"))
                a.play(audio_source)
            else:
                audio_source = discord.FFmpegPCMAudio(
                    executable=path,
                    source=f"gsound/{gsounds[id]}.mp3",
                    options="-vn"
                    )
                await bot.change_presence(activity=discord.CustomActivity(name=f"День игровых саундтреков. Играет {gsounds[id]}"))
                a.play(audio_source)
        if c_time.strftime('%A').capitalize()=="Суббота":
            if id==len(Traks):
                id_t,id=0,0
                audio_source = discord.FFmpegPCMAudio( 
                    executable=path,
                    source=f"traks/{Traks[id]}.mp3",
                    options="-vn"
                )
                await bot.change_presence(activity=discord.CustomActivity(name=f"День треков. Играет {Traks[id]}"))
                a.play(audio_source)
            else:
                audio_source = discord.FFmpegPCMAudio(
                    executable=path,
                    source=f"traks/{Traks[id]}.mp3",
                    options="-vn"
                )
                await bot.change_presence(activity=discord.CustomActivity(name=f"День треков. Играет {Traks[id]}"))
                a.play(audio_source)
        if c_time.strftime('%A').capitalize()=="Воскресенье":
            if id==len(ssounds):
                id_t,id=0,0
                audio_source = discord.FFmpegPCMAudio(
                    executable=path,
                    source=f"ssound/{ssounds[id]}.mp3",
                    options="-vn"
                )
                await bot.change_presence(activity=discord.CustomActivity(name=f"День сериальных песен. Играет {ssounds[id]}"))
                a.play(audio_source)
            else:
                audio_source = discord.FFmpegPCMAudio(
                    executable=path,
                    source=f"ssound/{ssounds[id]}.mp3",
                    options="-vn"
                )
                await bot.change_presence(activity=discord.CustomActivity(name=f"День сериальных песен. Играет {ssounds[id]}"))
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
        try:
            if os.name=="nt":
                global id_t,vc,Play
                voice_channel=None
                if ctx.guild.name=="Столица Агелия":
                    voice_channel = discord.utils.get(ctx.guild.voice_channels,name="Улица")
                elif ctx.guild.name=="Сервер для тестов":
                    voice_channel = discord.utils.get(ctx.guild.voice_channels,name="Основной")
                vc=await voice_channel.connect()
                await ctx.respond("Запущен тестовый режим")
                while Play==True:
                    all=Traks+covers+gsounds+ssounds+jsounds
                    audio_source = discord.FFmpegPCMAudio(
                        executable=path,
                        source=f"{tpath}/{all[id_t]}.mp3",
                        options="-vn"
                        )
                    vc.play(audio_source)
                    await bot.change_presence(activity=discord.CustomActivity(name="Запущен тестовый режим"))
                    while vc.is_playing() or vc.is_paused():
                        await sleep(1)
                    id_t+=1
                    if id_t==len(all):
                        break
                await discord.VoiceClient.disconnect(vc)
                vc=None
                id_t=0
                await bot.change_presence(activity=discord.CustomActivity(name="Готов играть музыку"))
            else:
                await ctx.respond("Запуск тестового режима не возможен вне системы владельца")
        except Exception as e:
            await ctx.respond(e)