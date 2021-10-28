from asyncio import run
from aiohttp import ClientSession
from Python_ARQ import ARQ

from .Arq.arqclient import arq


async def py_inf(query):
    query = query.replace("python", "")
    results = await arq.pypi(query)
    pypack = results.result[0]
    name = pypack.name
    version = pypack.version
    descrip = pypack.description
    uri = pypack.homepage
    reqs = pypack.requiirements
    auth = pypack.author
    rep = f'🎙 **Title**: {name}\n **Author**: {auth} \n**Version**: {version}\n **Description**: `{descrip}`\n👁‍🗨 **Requirements**: `{reqs}`\n **Uploaded By Zero Two**'
    print(rep)
    await session.close()
