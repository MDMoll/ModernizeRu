import re
with open("file.txt", encoding="utf-8", mode="rt") as infile:
    text = infile.read()
words = text.split()
#original = text.split()
original = set(words)
newdict = {'Ѳ': 'Ф', 'ѳ': 'ф', 'І': 'И', 'і': 'и', 'Ѣ': 'Е', 'ѣ': 'е', 'Ъ': '', 'ъ': '', 'Мѣр': 'Мир', 'мѣр': 'мир',
           'без': 'бес', 'вз': 'вс', 'из': 'ис', 'низ': 'нис', 'раз': 'рас', 'роз': 'рос', 'чрез': 'чрес',
           'через': 'черес', 'аго': 'ого', 'яго': 'его', 'ыя': 'ые', 'ея': 'ее', 'онѣ': 'они', 'однѣ': 'одни',
           'однѣхъ': 'одних', 'однѣмъ': 'одним', 'однѣми': 'одними'
}

def modernize(original, newdict):
    # Sorts key by length in descending order
    substrs = sorted(newdict, key=len, reverse=True)
    # Matches substrings with replacements
    regexp = re.compile('|'.join(map(re.escape, substrs)))
    newtext = "".join(regexp.sub(lambda match: newdict[match.group(0)], str(original)))
    print(newtext)

modernize(original, newdict)