# Solve NYT Spelling Bee

Without a string value for `charSet`, the script generates a random seven char string and proceeds with that as input.

If `charSet` is not a seven character string, the script exits prematurely.

The dictionary file was generated on Ubuntu 22 with

```bash
cat /usr/share/dict/words | \
  tr [:upper:] [:lower:] | \
    tr -d [:punct:] | \
      sort -uf > dictionary
```

Usage:

```bash
usage: solve_spelling_bee.py [-h] [-c CHARSET]

Suggest words for NYT's Spelling Bee.

options:
  -h, --help            show this help message and exit
  -c CHARSET, --charSet CHARSET
                        The seven letters provided by the puzzle, where THE FIRST LETTER IS THE MANDATORY LETTER.
```

