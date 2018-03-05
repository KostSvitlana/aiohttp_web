from aiohttp import web
import asyncio
# import peewee_async
# from models import database
import aiohttp_jinja2
import jinja2

from route import setup_routes

app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

setup_routes (app)
web.run_app(app, host = '127.0.0.1' ,  port = 8000 )