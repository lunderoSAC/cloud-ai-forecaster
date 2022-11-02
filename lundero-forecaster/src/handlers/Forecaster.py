import json

import pandas as pd
from statsforecast import StatsForecast
from statsforecast.models import AutoARIMA
from statsforecast.utils import generate_series

from tornado.web import RequestHandler
from swagger_params import ForecasterPostParameter
from utils.datemaker import parse_week_to_date, parse_date_to_week

PERIODOS = dict(M=12, D=30, W=7)


class ForecasterHandler(RequestHandler):

    def post(self):
        """
        ---
        tags:
        - Core Forecast Service
        summary: Consulta la salud de la aplicacion
        description: Aplicacion de salud para AI-Reporter
        produces:
        - application/json
        parameters:
        -   $ref: '#/parameters/ForecasterPostParameter'
        responses:
            200:
              description: Comunicación establecida correctamente.
            500:
              description: No se pudo comunicar con el servidor.
            400:
              description: Bad Requests
        """
        err = None
        json_body = json.loads(self.request.body.decode(encoding='utf-8'))
        fechas = json_body['Fechas']
        valores = json_body['Valores']
        periodo = json_body['Periodo'].upper()
        # This is the JSON body the user sent in their POST request.
        if len(fechas) != len(valores):
            err = 'Las fechas y los valores deben tener igual cantidad de elementos'

        if len(fechas) < 5 or len(fechas) > 100:
            err = 'Cantidad fuera de rango. La cantidad de datos debe estar entre 5 y 100.'

        if periodo not in ['M', 'D', 'W']:
            err = 'El periodo debe ser mensual (M), diario (D) o semanal (W)'

        if not err:
            season_length = PERIODOS[periodo]
            horizon = 4
            freq = periodo
            if periodo == 'W':
                freq = 'D'
                fechas = [parse_week_to_date(d) for d in fechas]

            Y_train_df = generate_series(n_series=1, freq=freq, min_length=len(fechas), max_length=len(fechas))
            Y_train_df.ds = fechas
            Y_train_df.ds = pd.to_datetime(Y_train_df.ds, infer_datetime_format=True)
            Y_train_df.y = valores

            models = [
                AutoARIMA(season_length=season_length),
            ]
            model = StatsForecast(
                df=Y_train_df,
                models=models,
                freq=periodo,
                n_jobs=-1)

            result = model.forecast(horizon).reset_index()[1:]

            if periodo == 'W':
                result.ds = result.ds.apply(lambda x: parse_date_to_week(x))

            mensaje = dict(
                fechas=result.ds.apply(lambda x: str(x)).to_list(),
                valores=result.AutoARIMA.to_list()
            )

        else:
            mensaje = 'Error al obtener el pronostico'

        self.write(
            dict(
                Estado=200,
                Error=err,
                Mensaje=mensaje
            )
        )



