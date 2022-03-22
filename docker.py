import os
import argparse

name = os.getenv('BOT_NAME') or 'Generic Bot'

parser=argparse.ArgumentParser()
parser.add_argument("input", help = "Input File Path")
parser.add_argument("character", help = "Character to count")
args = parser.parse_args()

input = (open(args.input, encoding='utf8')).read()

occurences = input.count(args.character)
print('Hello I am {name}!'.format(name=name))
print('Your specified character appears {occurences} time(s)!'.format(occurences=occurences))