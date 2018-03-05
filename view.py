from aiohttp import web
import aiohttp_jinja2

@aiohttp_jinja2.template('index.html')
async def index(request):
    return {'text':'Hello Word!'}

@aiohttp_jinja2.template('index.html')
async def handler(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return {'text': text}

@aiohttp_jinja2.template('index.html')
async def page(request):
    return {'text': "Some text here"}
