numbers = range(0,50)
print numbers

even_numbers = [ i for i in range(0,50) if i % 2 == 0 and i>=2 ]

squares = [ i*i for i in numbers if i % 2 == 0 and i >=2 ]

import random
random_numbers = [ random.randint(1,1000) for x in range(50) ]
print random_numbers

unique_random_numbers = list(set(random_numbers))
print unique_random_numbers

names = ['adam', 'Justin', 'joe', 'tony', 'zoe']
names_formatted = [ x.title() for x in names ]
print names_formatted

names_formatted = map(lambda x: x.title(), names)
print names_formatted

names_starting_with_j = [ name for name in names_formatted if name[0].lower() == 'j' ]
print names_starting_with_j

import string
from random import shuffle

raw_text = "hello and welcome to linux Academy!!"

letters = list(string.ascii_letters)
print letters

encoded_letters = letters[:]
shuffle(encoded_letters)
print encoded_letters

encoding_key = {}
decoding_key = {}

for k, v in zip(letters, encoded_letters):
    encoding_key[k]=v
    decoding_key[v]=k

print encoding_key

encoded_text = ''
for letter in raw_text:
    encoded_text += encoding_key.get(letter, letter)

print encoded_text

# Same thing with less lines of code

encoding_key = dict(zip(letters,encoded_letters))
decoding_key = dict(zip(encoding_key.values(),encoding_key.keys()))
encoded_text = ''.join([ encoding_key.get(w, w) for w in raw_text ])
print encoded_text
print decoded_text

