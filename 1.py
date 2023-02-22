"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jaroslav Dvočák
email: dvorak-jaroslav@email.cz
discord: Jaroslav D

"""


TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# registrovaní uživatelé
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
    }

# zadání přihlašovacích údajů
username = input("enter your username:  ")
password = input("enter your password:  ")

# kontrola přihl. údajů a kontola výběru textu
if users.get(username) != password:
    print("unregistered user, terminating the program..")
    quit()
else:
    print("-" * 40)
    print(f"Welcome to the app, bob")
    print(f"We have 3 texts to be analyzed.")
    print("-" * 40)
    number = input("Enter a number btw. 1 and 3 to select:  ")
    print("-" * 40)
    
if not number.isdigit():
    print(F"{number} is not a number ")
    print("terminating the program..")
    quit()
if int(number) < 1 or int(number) > 3:
    print(F"the number {number} is not between 1 and 3")
    print("terminating the program..")
    quit()

# počet slov
selected_text = TEXTS[int(number) - 1].split()
word_count = len(selected_text)
print(f"There are {word_count} words in the selected text.")

# počet slov začínajících velkým písmenem
count = 0
for word in selected_text:
    if word[0].isupper():
        count = count + 1
titltcase = count
print(f"There are {titltcase} titlecase words.")

# počet slov psaných velkými písmeny
count = 0
for word in selected_text:
    if word.isupper() and word.isalpha():
        count = count + 1
uppercase = count
print(f"There are {uppercase} uppercase words.")

# počet slov psaných malými písmeny
count = 0
for word in selected_text:
    if word.islower():
        count = count + 1
lowercase = count
print(f"There are {lowercase} lowercase words.")

# počet čísel (ne cifer)
count = 0
for word in selected_text:
    if word.isdigit():
        count = count + 1
numeric = count
print(f"There are {numeric} numeric strings.")

# sumu všech čísel (ne cifer) v textu
count = 0
for word in selected_text:
    if word.isdigit():
        count = count + int(word)
all_suma = count
print(f"The sum of all the numbers {all_suma}.")

# čistění textu od , a .
clean_texts = TEXTS[int(number) - 1].replace(",", "").replace(".", "")
l_clean_texts = clean_texts.split()

# zjištění četnosti délek slov
counts ={}
for slovo in l_clean_texts:
    if len(slovo) not in counts:
        counts[len(slovo)] = 1
    else:
        counts[len(slovo)] = counts[len(slovo)] + 1

# výpis tabulky
print("-" * 40)
print("{:<3}|{:^18}|{}".format("LEN", "OCCURENCES", "NR."))
print("-" * 40)
for key, value in sorted(counts.items()):
    print("{:>3}|{:<18}|{}".format(key, "*" * value , value))
    
