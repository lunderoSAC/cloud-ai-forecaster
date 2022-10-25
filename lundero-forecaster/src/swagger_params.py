from tornado_swagger.model import register_swagger_model
from tornado_swagger.parameter import register_swagger_parameter

@register_swagger_parameter
class ForecasterPostParameter:
    """
    ---
    name: request
    in: body
    description: Body of the Forecaster Post Request.
    required: true
    schema:
      $ref: '#/definitions/ForecasterBodyModel'
    """

@register_swagger_model
class ForecasterBodyModel:
    """
    ---
      type: object
      required:
        - Fechas
        - Valores
        - Periodo
      properties:
        Fechas:
          description: Lista de fechas como string. "2022-01-31", "2022-02-28", "2022-03-31", "2022-04-30", "2022-05-31", "2022-06-30", "2022-07-31", "2022-08-31", "2022-09-30", "2022-10-31", "2022-11-30", "2022-12-31", "2023-01-31"
          type: array
          items:
            $ref: '#/definitions/DateTimesModel'
        Valores:
          description: Lista de valores numeric. 0.8232, 0.8923, 0.91231, 1.0232, 1.232, 1.390, 1.4244, 1.53434, 1.67632, 1.77122, 1.8823, 1.92312, 2.02324
          type: array
          items:
            $ref: '#/definitions/ValuesModel'
        Periodo:
          description: Periodo mensual (M) yyyy-mm-01   , diario (D) con fechas yyyy-mm-dd o semanal (W) con fechas yyyy-mm-dd
          type: string
          example: D
    """

@register_swagger_model
class DateTimesModel:
    """
    ---
      type: string
      description: datetime as string for numeric record
      example: '2022-01-31'
    """
@register_swagger_model
class ValuesModel:
    """
    ---
      type: number
      format: float
      description: numeric value taken on specific time
      example: 0.8232
    """
