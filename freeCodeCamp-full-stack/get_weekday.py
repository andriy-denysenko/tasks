from datetime import datetime as dt


def get_weekday(date_string):
    d = dt.strptime(date_string, "%Y-%m-%d").strftime("%A")
    return d


assert (get_weekday("2025-11-06") == 'Thursday')
assert (get_weekday("1999-12-31") == 'Friday')
assert (get_weekday("1111-11-11") == 'Saturday')
assert (get_weekday("2112-12-21") == 'Wednesday')
assert (get_weekday("2345-10-01") == 'Monday')
