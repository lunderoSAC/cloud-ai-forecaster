from tornado.web import Application, url, StaticFileHandler
from tornado_swagger.setup import setup_swagger

from handlers.HealtService import HealtService
from handlers.Forecaster import ForecasterHandler


class App(Application):
    rutas = [
        url(r'/ai-forecaster/health$', HealtService),
        url(r'/ai-forecaster/forecast', ForecasterHandler),
        url(r'/(favicon.ico)', StaticFileHandler, {"path": "static/"})
    ]

    def __init__(self):
        configuracion = dict(
            debug=False
        )
        setup_swagger(
            self.rutas,
            swagger_url='/ai-forecaster/swagger',
            api_base_url='/',
            description='Lundero - Equipo de Inteligencia Artificial.',
            title='AI-Forecaster',
            api_version='0.1.0',
            contact='soporte@lundero.com'
        )
        super(App, self).__init__(self.rutas, **configuracion)
