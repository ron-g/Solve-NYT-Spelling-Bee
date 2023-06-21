#!/usr/bin/python3

import argparse, re
from random import sample

charsLower = 'qwertyuipasdfghjkzxcvbnm'
dict_file = './dictionary'
separator = '-='

validWords = []
allSevenLetters = []

try:
    with open(dict_file, 'r') as f:
       words = f.read()
except Exception as e:
    print(f"The '{dict_file}' dictionary file doesn't exist.")
    raise
    exit(1)
else:
    words = set(words.split('\n'))
    # print(words)
finally:
    pass

parser = argparse.ArgumentParser(description="Suggest words for NYT's Spelling Bee.")

parser.add_argument(
	"--charSet",
	type=str,
	default = ''.join(sample(charsLower, 7)),
	help="The seven letters provided by the puzzle, where THE FIRST LETTER IS THE MANDATORY LETTER."
	)

args = parser.parse_args()

if len(args.charSet) != 7:
	print(f"charSet '{args.charSet}' doesn't have seven (7) characters. What were you thinking!?\n")
	exit(1)

the_regex = rf"^[{args.charSet}]""{4,}$"
the_regex = re.compile(the_regex)

print(f"\n{separator * 10} WORDS {separator[::-1] * 10}")
print(f"Character Set:\n\t{args.charSet}")

sorted_word_list = \
        sorted(\
            list(filter(the_regex.match, words)), \
            key = len
        )

for _ in sorted_word_list:
	#print(_)
	if \
		args.charSet[0] in _ and \
		args.charSet[1] in _ and \
		args.charSet[2] in _ and \
		args.charSet[3] in _ and \
		args.charSet[4] in _ and \
		args.charSet[5] in _ and \
		args.charSet[6] in _ :
		allSevenLetters.append(_)
	elif args.charSet[0] in _ :
		validWords.append(_)
	else:
		pass

print(f"\nContains '{args.charSet[0]}':")
for _ in validWords:
	print(f"\t{_}")

print(f"\nContains all seven letters!:")
for _ in allSevenLetters:
	print(f"\t{_}")

print(f"{separator * 12} {separator[::-1] * 12}")

exit(0)

