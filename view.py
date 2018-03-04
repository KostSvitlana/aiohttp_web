from aiohttp import web


async def index(request):
    return web.Response(text='Hello Aiohttp!')

async def handler(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

# async def page(request):
#     return templ('index', request, {'key':'val'})