from aiohttp import ClientSession
from Python_ARQ import ARQ
import configparser

ARQ_API_KEY = config['DEFAULT']['AI_KEY']


ARQ_API_URL = "https://thearq.tech"

aiohttpsession = ClientSession()

arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)
