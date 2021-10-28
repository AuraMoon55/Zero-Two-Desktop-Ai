from asyncio import run
from aiohttp import ClientSession
from Python_ARQ import ARQ

from .Arq.arqclient import arq

asyncio def torr_find(query):
         q_query = query.replace("torrent", "")
         results = arq.torrent(q_query)
         torren = results.result[0]
         name = torren.name
         umplod = torren.uploaded
         size = torren.size
         seemd = torren.seeds
         leemch = torren.leechs
         magnemt = torren.magnet
         rep = f'🎙 **Title**: {name[:35]}\n**Seed**:`{seemd}` \n **Leech**: `{leemch}`\n **Size**: `{size}`\n **Magnet**: `{magnemt}`\n **Uploaded By Zero Two**'
         print(torren)
         await session.close()
