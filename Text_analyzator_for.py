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

USERS = {'bob':'123',
         'ann':'pass123',
         'mike':'password123',
         'liz':'pass123'}

ODDELOVAC = '-' * 40

print(ODDELOVAC)
print('Welcome to the app. Please log in: ')
USERNAME = input('USERNAME: ')
PASSWORD = input('PASSWORD: ')
print(ODDELOVAC)

if USERS.get(USERNAME) != PASSWORD:
    print('Incorrect USERNAME or PASSWORD. Please log in again.')
    exit()

print('We have 3 texts to be analyzed.')
NUMBER = int(input('Enter a number btw. 1 and 3 to select: '))
print(ODDELOVAC)

if NUMBER < 1 or NUMBER > 3:
    print('Incorrect NUMBER!')
    exit()

TEXT = str(TEXTS[NUMBER-1])
words = [word.strip(',.:/') for word in TEXT.split()]
print('There are', len(words), 'words in the selected text.')

titlecase = 0
uppercase = 0
lowercase = 0
numeric = 0
numbers = 0
word_lenghts = {}

for word in words:
    if word.istitle():
        titlecase += 1
    elif word.isupper():
        uppercase += 1
    elif word.islower():
        lowercase += 1
    elif word.isdigit():
        numbers = numbers + int(word)
        numeric += 1

    word_lenghts[len(word)] = word_lenghts.setdefault(len(word), 0) + 1

print('There are', titlecase, 'titlecase words')
print('There are', uppercase, 'uppercase words')
print('There are', lowercase, 'lowercase words')
print('There are', numeric, 'numeric strings')
print(ODDELOVAC)

counts_letters = sorted(word_lenghts)

for letter in counts_letters:
    if letter in word_lenghts:
        frequency = word_lenghts.get(letter)
        print(letter,'*' * frequency, frequency)

print(ODDELOVAC)
print('If we summed all the numbers in this text we would get:', float(numbers))
print(ODDELOVAC)