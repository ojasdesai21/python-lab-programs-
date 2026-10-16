import re

text = "Aaryan has 2 cats and 3 dogs"

# 1. match(): checks the beginning
print("1. match:", re.match(r"Aaryan", text))

# 2. fullmatch(): checks the entire string
print("2. fullmatch:", re.fullmatch(r"\d+", "123"))

# 3. search(): finds the first occurrence
print("3. search:", re.search(r"\d+", text).group())

# 4. findall(): finds all occurrences
print("4. findall:", re.findall(r"\d+", text))

# 5. split(): splits the string
print("5. split:", re.split(r"\s+", text))

# 6. sub(): replaces matching text
print("6. sub:", re.sub(r"\d+", "#", text))
