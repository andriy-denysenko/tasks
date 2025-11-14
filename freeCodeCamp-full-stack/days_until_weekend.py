# Is It the Weekend?
#
# Given a date in the format "YYYY-MM-DD", return the number of days left until the weekend.
#
#     The weekend starts on Saturday.
#     If the given date is Saturday or Sunday, return "It's the weekend!".
#     Otherwise, return "X days until the weekend.", where X is the number of days until Saturday.
#     If X is 1, use "day" (singular) instead of "days" (plural).
#     Make sure the calculation ignores your local timezone.

from datetime import datetime as dt

# Detects whether the date specified is a weekend.
# If not, calculates the number of days left until the weekend.
def days_until_weekend(date_string: str):
    # Get 1-based week day number for simplier calculation
    week_day: int = dt.strptime(date_string, "%Y-%m-%d").weekday() + 1
    response: str = "It's the weekend!"
    if week_day not in [6, 7]:
        days_left: int = 6 - week_day
        pl: str = 's' if days_left > 1 else ''
        response = f"{days_left} day{pl} until the weekend."
    return response

assert (days_until_weekend("2025-11-14") == "1 day until the weekend.")
assert (days_until_weekend("2025-01-01") == "3 days until the weekend.")
assert (days_until_weekend("2025-12-06") == "It's the weekend!")
assert (days_until_weekend("2026-01-27") == "4 days until the weekend.")
assert (days_until_weekend("2026-09-07") == "5 days until the weekend.")
assert (days_until_weekend("2026-11-29") == "It's the weekend!")
