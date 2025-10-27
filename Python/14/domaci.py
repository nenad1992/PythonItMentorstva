# Da li je data rec email
import re

email = "toma@gmail.com"

# \w - proveravamo da li postoje slova
# \.- -> proveravamo da li imamo . ili crticu
# \. proveravamo da li postoji .

email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(email_pattern, email):
    print("It is email")