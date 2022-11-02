from datetime import datetime


def parse_week_to_date(week_datetime: datetime) -> datetime:
    """
    parses yyyy-W%w to yyyy-mm-dd
    example: 2022-W1 -> 2022-01-01
    """
    return datetime.strptime(week_datetime + '-1', "%Y-W%W-%w")


def parse_date_to_week(week_datetime: datetime) -> datetime:
    """
    parses yyyy-mm-dd to yyyy-W%w
    example: 2022-01-01 -> 2022-W1
    """
    week_of_the_year = week_datetime.isocalendar()[1]
    year = week_datetime.year
    return f'{year}-W{week_of_the_year}'