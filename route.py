from view import index, handler, page


def setup_routes(app):
    # app.router.add_route('GET', '/', index, name='index')
    app.router.add_get('/', index, name='index')

    app.router.add_get('/hello', handler, name='hello')
    app.router.add_get('/hello/{name}', handler)
    app.router.add_get('/page', page, name='page')