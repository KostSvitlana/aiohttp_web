from aiohttp import web
import asyncio

from route import setup_routes

app = web.Application()
setup_routes (app)
web.run_app(app, host = '127.0.0.1' ,  port = 8000 )