# ModernizeRu
This python script (crudely!) updates Petrine Russian text (1708-1917) to use contemporary orthography (1918-).

At its most basic, this replaces Ѳѳ, Іі, Ѣѣ, Ѵѵ with Фф, Ее and Ии for both Ѵ and І, while removing final hard signs (ъ).

Additionally, prefixes ending in з preceeding voiceless consonants have been changed to с.
Suffixes related to adjectives in singular genitive as well as nominative plural have also been updated.

Certain words whose spelling was altered, but beyond simply replacing the four letters above, have also been included.
Others, however, such as сей (an archaic form of этот) and its declensions, have not.

Edge cases, such as an overlap in feminine nominative plural adjectives and that of feminine nominative singular nouns has not yet been addressed.

In other words, be aware of the potential pitfalls within your text. Otherwise, you may end up replacing, e.g., the Ея river in Krasnodar Krai with the feminine genitive singular ее and not realize it.
