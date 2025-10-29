# QWE123 -> Moraju biti 3 slova i pracena sa 3 broja
import re

# [A-Za-z]{3} -> pronadji svuda gde imamo 3 slova zaredom
# \d -> trazimo brojeve
# \d{3} -> pronadji saboln gde imamo 3 broja zaredom
# \b -> word boundary (granicna rec)

bonus_codes = "ABC123, bonus455, bonus22"
pattern = r"\b[A-Za-z]{3}\d{3}\b"

product_codes = re.findall(pattern, bonus_codes)

print(product_codes)

# Rec od 5 slova, pracena sa minimum 2 broja
username = "toma1993"

# [a-zA-Z]{1,5} -> t, to, tom, toma, tomaa
# \d{2,} -> nadji 2 ili vise brojeva zaredom
username_pattern = r"[a-zA-Z]{1,5}\d{2,}"

match = re.match(username_pattern, username)

if match:
    print(match.group())