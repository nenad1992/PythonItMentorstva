import re

with open('logs/http.log', 'r') as file:
    lines = file.readlines()

# Nadji rec Error praceno sa 3 broja
error_pattern = r"Error \d{3}"
success_pattern = r"Status \d{3}"

# Izvlacite podatke iz http.log
# Ako je u pitanju Error linija upisite u logs/errors.log
# Ako je u pitanju Status linija upisite u logs/success.log

with open('logs/errors.log', 'a') as error_file, open('logs/success.log', 'a') as success_file:
    for line in lines:
        if re.search(error_pattern, line):
                error_file.write(line)
        elif re.search(success_pattern, line):
                success_file.write(line)