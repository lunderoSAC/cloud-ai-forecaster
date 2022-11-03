from datetime import datetime, timedelta


def parse_week_to_date(week_datetime: datetime) -> datetime:
    """
    parses string yyyy-W%w to datetime yyyy-mm-dd
    example: 2022-W1 -> 2022-01-01
    """
    return datetime.strptime(week_datetime + '-1', "%Y-W%W-%w")


def parse_date_to_week(week_datetime: datetime) -> datetime:
    """
    parses datetime yyyy-mm-dd to string yyyy-W%w
    example: 2022-01-01 -> 2022-W1
    """
    base_monday = week_datetime - timedelta(days=week_datetime.weekday())
    year, week, day = base_monday.isocalendar()
    return f'{year}-W{week}'


def parse_month_to_date(month_datetime: str) -> datetime:
    """
    parses string 'yyyy-mm' or 'yyyy-mm-dd' to datetime 'yyyy-mm-01'
    example: 2022-02-18 -> 2022-02-01
    """
    if month_datetime.count('-') == 1:
        year, month = month_datetime.split('-')
    elif month_datetime.count('-') == 2:
        year, month, day = month_datetime.split('-')

    return datetime(
        year=int(year),
        month=int(month),
        day=1
    )
