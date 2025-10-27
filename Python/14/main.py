import re

ourNumbers = "12345" # Da li se ovde nalaze samo brojevi

# r (malo slovo r) predstavlja da mi trazimo i tretiramo ceo string kao obican text

# r - sve sto proveravam tretiraj kao obican text
# ^ - trazimo od pocetka stringa
# \d - trazi samo brojeve (0-9) - matches any numbers from 0 to 9
# + - nastavlja dalje
# $ - kraj stringa

# Proveri da li su samo brojevi unutar necega
pattern = r"^\d+$"

# Proveri da li postoji taj pattern (sablon) unutar stinga (ourNumbers)
if re.match(pattern, ourNumbers):
    print("Samo brojevi")
else:
    print("Nisu samo brojevi")

# regEx koji ce proveravati da li imamo samo slova unutar stringa
sentence = "I love Python"

# Character class: [A-Za-z]
pattern_string = r"^[a-zA-Z ]+$" # posle Z je stavljen razmak da bi i njega trazio

if re.match(pattern_string, sentence):
    print("Samo slova")
else:
    print("Nisu samo slova")

# Da li recenica pocinje velikim slovom
importantSentence = "Today will rain"

capitalPattern = r"^[A-Z]"

if re.match(capitalPattern, importantSentence):
    print("Has capital letter")

phone_number = "38160555333"

phone_pattern = r"^38(1|2|5|9)" # r"^381(1|2||5|9)" - | sluzi kao ili

phone_match = re.match(phone_pattern, phone_number)

phone_map = {
    "381": "Serbia",
    "382": "Montenegro",
    "385": "Bosnia and Herzegovina",
    "389": "Croatia"
}

if phone_match:
    prefix = "38"+phone_match.group(1)
    print(f"Prefix number is {prefix} and matching country is {phone_map[prefix]}")