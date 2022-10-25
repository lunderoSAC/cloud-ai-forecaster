from datetime import datetime

from tornado.web import RequestHandler


class HealtService(RequestHandler):

    def get(self):
        """
        ---
        tags:
        - Health Service
        summary: Consulta la salud de la aplicacion
        description: Aplicacion de salud para AI-Forecaster
        produces:
        - application/json
        responses:
            200:
              description: Comunicación establecida correctamente.
              schema:
            500:
              description: No se pudo comunicar con el servidor.
              schema:
            400:
              description: Bad Requests
              schema:
        """
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        response = dict(Estado=200,
                        Error=None,
                        Mensaje=current_time)
        self.write(response)
