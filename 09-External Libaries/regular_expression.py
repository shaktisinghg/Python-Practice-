import re

text = 'A quick brown fox is jump over the lazy dog'

mach = re.search('quick', text)

print(mach.start())
print(mach.end())

matches_fild = re.findall('a', text, re.IGNORECASE)
print(matches_fild)


new_text = re.sub('dog', 'cat', text)
print(new_text)