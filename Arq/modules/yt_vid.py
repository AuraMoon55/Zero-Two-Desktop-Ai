from asyncio import run
from aiohttp import ClientSession
from Python_ARQ import ARQ
import pytube
from .Arq.modules import file_converter


from .Arq.arqclient import arq

def download_video(url):
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(22)
    stream.download()
    return stream.default_filename


async def yt_vid(query):
    query = query.replace("yt", "")
    results = await arq.youtube(query)
    videos = results.result[0]
    title = videos.title
    duration = videos.duration
    views = videos.views
    uri = videos.url_suffix
    link = f'https://youtube.com{uri}'
    thumb = videos.thumbnails
    rep = f'🎙 **Title**: [{title[:35]}]({link})\n🎬 **Source**: YouTube\n⏱️ **Duration**: `{duration}`\n👁‍🗨 **Views**: `{views}`\n **Uploaded By Zero Two**'
    print(thumb,rep)
    await session.close()
    download_video(link)

def download_song(url):
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(18)
    stream.download()
    return stream.default_filename




async def song_dl(query):
     query = query.replace("song", "")
    results = await arq.youtube(query)
    videos = results.result[0]
    title = videos.title
    duration = videos.duration
    views = videos.views
    uri = videos.url_suffix
    link = f'https://youtube.com{uri}'
    thumb = videos.thumbnails
    rep = f'🎙 **Title**: [{title[:35]}]({link})\n🎬 **Source**: YouTube\n⏱️ **Duration**: `{duration}`\n👁‍🗨 **Views**: `{views}`\n **Uploaded By Zero Two**'
    print(thumb,rep)
    await session.close()
    filename = download_song(link)
    fileconverter.convert_to_mp3(filename)
    
    

