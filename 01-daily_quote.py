#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date

quotes = [
    # Create a list of quotes here
    "The man who says his wife can’t take a joke, forgets that she took him. — Oscar Wilde",
    "All you need is love. But a little chocolate now and then doesn’t hurt. ― Charles M. Schulz",
    "Instant gratification takes too long. ― Carrie Fisher",
    "Don’t be so humble — you are not that great. ― Golda Meir",
    "Why do they call it rush hour when nothing moves? — Robin Williams"
]

def get_quote_of_the_day(quotes):
    todays_quote = None

    # Your code here
    todays_quote = random.choice(quotes)
    return todays_quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))

# Cron job (add this to your crontab):
#0 8 * * * /workspaces/03-data-structures-shwe-kandhalu/01-daily_quote.py >> /workspaces/03-data-structures-shwe-kandhalu/01-daily_quote.txt