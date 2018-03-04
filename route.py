from view import index, handler


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/hello', handler)
    app.router.add_get('/hello/{name}', handler)