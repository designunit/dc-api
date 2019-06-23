import aiohttp

from sanic import Sanic
from sanic.response import json
from sanic_cors import cross_origin

app = Sanic()


async def get_data():
    url = 'https://raw.githubusercontent.com/designunit/dc-data/master/data.json'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json(content_type='text/plain')
            return data
