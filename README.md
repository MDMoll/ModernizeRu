# ModernizeRu
This python script updates Petrine Russian text (1708-1917) to use contemporary orthography (1918-present).

At its most basic, this replaces Ѳѳ, Іі, Ѣѣ, Ѵѵ with Фф, Ее and Ии for both Ѵ and І, while removing final hard signs (ъ) in words ending with consonants.

Additionally, prefixes ending in з preceeding voiceless consonants have been changed to с.
Suffixes related to adjectives in singular genitive as well as nominative plural have also been updated.

Certain words whose spelling was altered, but beyond simply replacing the four letters above, have also been included.
Others, however have not, such as сей, an archaic form of этот, and its declensions have not.

Edge cases, such as an overlap in feminine nominative plural adjectives and that of feminine nominative singular nouns has not yet been addressed.
