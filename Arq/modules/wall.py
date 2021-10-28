from asyncio import run
from aiohttp import ClientSession
from Python_ARQ import ARQ

from .Arq.arqclient import arq


async def wp(query):
    q_query = query.replace("wallpaper", "")
    results = await arq.wall(q_query)
    lyr = results.result[0]
    wdt = lyr.width
    hgt = lyr.height
    fty = lyr.file_type
    fsz = lyr.file_size
    thumb = lyr.url_thumb
    uri = lyr.url_image
    rep = f'**Results For**: `{q_query}`\n **Width**: `{wdt}`\n **Height**: {hgt}\n **File Type**: {fty}\n **File Size**: {fsz}\n **Uploaded By Zero Two**'
    print(rep)
    await session.close()
