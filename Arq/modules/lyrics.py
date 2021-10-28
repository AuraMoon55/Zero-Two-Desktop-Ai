from asyncio import run
from aiohttp import ClientSession
from Python_ARQ import ARQ

from .Arq.arqclient import arq


async def ly_find(query):
    q_query = query.replace("lyrics", "")
    results = await arq.lyrics(q_query)
    lyr = results.result[0]
    lyric = lyr.lyrics
    rep = f'**Song Name**: `{query}`\n `{lyric}`\n **Uploaded By Zero Two**'
    print(rep)
    await session.close()
