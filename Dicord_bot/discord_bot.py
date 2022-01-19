from typing import Text
import discord
from discord.ext import commands
from youtube_dl import YoutubeDL
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get
from discord import FFmpegPCMAudio
import asyncio
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

bot = commands.Bot(command_prefix='라이언 ')
# '라이언 ' 로 시작하는 접두어

# 재생목록 관련
user = []#          유저가 입력한 노래 이름 저장
musictitle = []#    전처리한 노래 정보의 제목
song_queue = []#    전처리한 노래 정보의 링크
musicnow = []#      현재 출력중인 노래

# 노래 제목과 링크를 저장하는 title함수
def title(msg):
    global music

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    chromedriver_dir = r"D:\Discord_Bot\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver_dir, options = options)
    driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
    source = driver.page_source
    bs = bs4.BeautifulSoup(source, 'lxml')
    entire = bs.find_all('a', {'id': 'video-title'})
    entireNum = entire[0]
    music = entireNum.text.strip()
    
    musictitle.append(music)
    musicnow.append(music)
    test1 = entireNum.get('href')
    url = 'https://www.youtube.com'+test1
    with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
    URL = info['formats'][0]['url']

    driver.quit()
    
    return music, URL

def play(ctx):
    global vc
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    URL = song_queue[0]
    del user[0]
    del musictitle[0]
    del song_queue[0]
    vc = get(bot.voice_clients, guild=ctx.guild)
    if not vc.is_playing():
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after=lambda e: play_next(ctx)) 

def play_next(ctx):
    if len(musicnow) - len(user) >= 2:
        for i in range(len(musicnow) - len(user) - 1):
            del musicnow[0]
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    if len(user) >= 1:
        if not vc.is_playing():
            del musicnow[0]
            URL = song_queue[0]
            del user[0]
            del musictitle[0]
            del song_queue[0]
            vc.play(discord.FFmpegPCMAudio(URL,**FFMPEG_OPTIONS), after=lambda e: play_next(ctx))



@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('DJ Ryan Drop the beat!!'))


@bot.command()
async def 들어와(ctx):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send('채널에 접속한 유저가 없습니당..')

@bot.command()
async def 나가(ctx):
    try:
        await vc.disconnect()
    except:
        await ctx.send('채널에 속한 상태가 아닙니당..')

@bot.command()
async def 따라하기(ctx, *, text):# 따라하기 = repeat
    #await ctx.send(text)
    await ctx.send(embed = discord.Embed(title = '따라하기', description = text, color = 0xFFB94E))# 좌측 색 = 아이보리~베이지 색상 = 연보라(0xDC75F3)
    # title = Embed의 제목, descriotion = Embed의 내용, color = Embed의 색깔( 위 기준 연두색 = 0x00ff00)

# url을 직접 입력해서 노래를 재생하는 코드
'''
@bot.command()
async def 재생(ctx, *, url):
    YDL_OPTIONS = {'format' : 'bestaudio', 'noplaylist' : 'True'}
    FFMPEG_OPTIONS = {'before_options' : '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' , 'options' : '-vn'}
    
    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download = False)
        URL = info['formats'][0]['url']
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        await ctx.send(embed = discord.Embed(title = '노래 재생', description = 'DJ_라이언 : 현재'+url+'을 재생하고 있습니다.', color = 0xDC75F3))# 연보라
    else:
        await ctx.sned('DJ_라이언 : 노래가 현재 재생중입니다.')
'''            
# 자동 검색해서 노래를 재생하는 코드
@bot.command()
async def 재생(ctx, *, msg):
    if not vc.is_playing():
        global entireText
        # ffmpeg와 youtube_dl의 기본 설정
        YDL_OPTIONS = {'format' : 'bestaudio', 'noplaylist' : 'True'}
        FFMPEG_OPTIONS = {'before_options' : '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' , 'options' : '-vn'}
        # chromedriver, selenium 활용해서 유튜브 영상 제목과 링크 가져오기
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chromedriver_dir = r'D:/Discord_bot/chromedriver.exe'
        #driver = webdriver.Chrome(chromedriver_dir)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chrome_options)
        driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id' : 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl
        # 음악 재생
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download = False)
        URL = info['formats'][0]['url']
        await ctx.send(embed = discord.Embed(title = '[DJ_라이언] 노래 재생', description = 'DJ_라이언 : 현재 '+entireText+'을(를) 재생중입니다.', color = 0xDC75F3))
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    else:
        await ctx.send('DJ_라이언 : 이미 노래가 재생중이라서 재생할 수가 없습니당')

@bot.command()
async def 일시정지(ctx):
    if vc.is_playing():
        vc.pause()
        # 재생목록을 위해 수정한 내용 ( 수정 전 코드 = description = "DJ_라이언 : 현재 " + entireText + "을(를) 재생하고 있습니다." )
        await ctx.send(embed = discord.Embed(title = '멈춰!!', description = musicnow[0] + "을(를) 일시정지 했습니다.", color = 0x00ff00))
    else:
        await ctx.send('DJ_라이언 : 지금은 노래가 재생중이 아니라 멈출수가 없어요')

@bot.command()
async def 다시재생(ctx):
    try:
        vc.resume()
    except:
        await ctx.send('DJ_라이언 : 지금은 노래가 재생중이 아니라 다시재생할수가 없어요')
    else:
        # 재생목록을 위해 수정한 내용 ( 수정 전 코드 = description = "DJ_라이언 : 현재 " + entireText + "을(를) 재생하고 있습니다." )
        await ctx.send(embed = discord.Embed(title= "다시재생", description = musicnow[0]  + "을(를) 다시 재생했습니다.", color = 0xDC75F3))

@bot.command()
async def 끄기(ctx):
    if vc.is_playing():
        vc.stop()
        # 재생목록을 위해 수정한 내용 ( 수정 전 코드 = description = "DJ_라이언 : 현재 " + entireText + "을(를) 재생하고 있습니다." )
        await ctx.send(embed = discord.Embed(title= "노래끄기", description = musicnow[0]  + "을(를) 종료했습니다.", color = 0x00ff00))
    else:
        await ctx.send('DJ_라이언 : 지금은 노래가 재생중이 아니라 끌 노래가 없어요')

@bot.command()
async def 지금(ctx):
    if not vc.is_playing():
        await ctx.send("어_라이언 : 지금은 재생중인 노래가 없습니당")
    else:
        # 재생목록을 위해 수정한 내용 ( 수정 전 코드 = description = "DJ_라이언 : 현재 " + entireText + "을(를) 재생하고 있습니다." )
        await ctx.send(embed = discord.Embed(title = "지금노래", description = "지금은 " + musicnow[0] + "을(를) 재생하고 있습니다.", color = 0xDC75F3))

#!음악추가 '검색어'
@bot.command()
async def 음악추가(ctx, *, msg):
    user.append(msg)
    result, URLTEST = title(msg)
    song_queue.append(URLTEST)
    await ctx.send(result + "를 재생목록에 추가했어요!")

@bot.command()
async def 음악삭제(ctx, *, number):
    try:
        ex = len(musicnow) - len(user)
        del user[int(number) - 1]
        del musictitle[int(number) - 1]
        del song_queue[int(number)-1]
        del musicnow[int(number)-1+ex]
            
        await ctx.send("대기열이 정상적으로 삭제되었습니다.")
    except:
        if len(list) == 0:
            await ctx.send("대기열에 노래가 없어 삭제할 수 없어요!")
        else:
            if len(list) < int(number):
                await ctx.send("숫자의 범위가 목록개수를 벗어났습니다!")
            else:
                await ctx.send("숫자를 입력해주세요!")

@bot.command()
async def 음악리스트(ctx):
    if len(musictitle) == 0:
        await ctx.send("아직 아무노래도 등록하지 않았어요.")
    else:
        global Text
        Text = ""
        for i in range(len(musictitle)):
            Text = Text + "\n" + str(i + 1) + ". " + str(musictitle[i])
            
        await ctx.send(embed = discord.Embed(title= "노래목록", description = Text.strip(), color = 0x00ff00))

@bot.command()
async def 리스트초기화(ctx):
    try:
        ex = len(musicnow) - len(user)
        del user[:]
        del musictitle[:]
        del song_queue[:]
        while True:
            try:
                del musicnow[ex]
            except:
                break
        await ctx.send(embed = discord.Embed(title= "목록초기화", description = """목록이 정상적으로 초기화되었습니다. 이제 노래를 등록해볼까요?""", color = 0x00ff00))
    except:
        await ctx.send("아직 아무노래도 등록하지 않았어요.")

@bot.command()
async def 리스트재생(ctx):

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    
    if len(user) == 0:
        await ctx.send("아직 아무노래도 등록하지 않았어요.")
    else:
        if len(musicnow) - len(user) >= 1:
            for i in range(len(musicnow) - len(user)):
                del musicnow[0]
        if not vc.is_playing():
            play(ctx)
        else:
            await ctx.send("노래가 이미 재생되고 있어요!")

@bot.command()
async def 인기차트(ctx):
    if not vc.is_playing():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        
        global entireText
        YDL_OPTIONS = {'format' : 'bestaudio', 'noplaylist' : 'True'}
        FFMPEG_OPTIONS = {'before_options' : '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options' : '-vn'}
        
        chromedriver_dir = r'D:/Discord_bot/chromedriver.exe'
        driver = webdriver.Chrome(chromedriver_dir, options = chrome_options)
        driver.get("https://www.youtube.com/results?search_query=멜론차트")
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl 

        driver.quit()
        
        # 재생목록을 위해 추가한 내용
        musicnow.insert(0, entireText)
        
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        
        # 재생목록을 위해 수정한 내용 ( 수정 전 코드 = description = "DJ_라이언 : 현재 " + entireText + "을(를) 재생하고 있습니다." )
        await ctx.send(embed = discord.Embed(title= "멜론 인기차트 노래재생", description = "DJ_라이언 : 현재 " + entireText + "을(를) 재생하고 있습니다.", color = 0x00ff00))
        # 수정 전 코드
        #await ctx.send(embed = discord.Embed(title= "멜론 인기차트 노래재생", description = "DJ_라이언 : 현재 " + entireText + "을(를) 재생하고 있습니다.", color = 0x00ff00))
        
        # 재생목록을 위해 수정한 내용
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after = lambda e: play_next(ctx))
        # 수정 전 코드
        #vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    else:
        await ctx.send("이미 노래가 재생 중이라 노래를 재생할 수 없어요!")

bot.run('OTE2Njc2MTM3NDE2MDI4MjEw.YatnLg.9kWkxqCrr9hRER1Tu8vYIKuAzJk')