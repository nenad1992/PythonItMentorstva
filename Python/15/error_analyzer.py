# Izvuci sva vremena iz logs/errors.log
import re

with open('logs/errors.log') as error_log:

    # sablon: 2broja:2broja:2broja
    pattern = r"\d{2}:\d{2}:\d{2}"

    for error in error_log.readlines():
        match = re.search(pattern, error)
        print(match)