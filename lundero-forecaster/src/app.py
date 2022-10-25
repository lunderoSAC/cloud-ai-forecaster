import pandas as pd
from chalice import Chalice
from statsforecast import StatsForecast
from statsforecast.models import AutoARIMA
from statsforecast.utils import generate_series

app = Chalice(app_name='lundero-ai-forecaster')

PERIODOS = dict(M=12, D=30)


@app.route('/forecast-value', methods=['POST'])
def create_user():
    """
    {
        fechas: [yyyy-mm-dd, yyyy-mm-dd]
        valores: [x1, x2]
        periodo: D (diario), M (mensual)

    """
    err = None

    fechas = app.current_request.json_body['fechas']
    valores = app.current_request.json_body['valores']
    periodo = app.current_request.json_body['periodo'].upper()
    # This is the JSON body the user sent in their POST request.
    if len(fechas) != len(valores):
        err = 'Las fechas y los valores deben tener igual cantidad de elementos'

    if len(fechas) < 5 or len(fechas) > 100:
        err = 'Cantidad fuera de rango. La cantidad de datos debe estar entre 5 y 100.'

    if periodo not in ['M', 'D']:
        err = 'El periodo debe ser mensual (M) o diario (D)'

    if not err:
        season_length = PERIODOS[periodo]
        horizon = 3

        Y_train_df = generate_series(n_series=1, freq=periodo, min_length=len(fechas), max_length=len(fechas))
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

        result = model.forecast(horizon).reset_index()

        mensaje = dict(
            fechas=result.ds.apply(lambda x: str(x)).to_list(),
            valores=result.AutoARIMA.to_list()
        )

    else:
        mensaje = 'Error al obtener el pronostico'

    return dict(
            Estado=200,
            Error=err,
            Mensaje=mensaje
        )
