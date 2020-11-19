import re
pattern=r'[aeiou]'
if re.search(pattern,"apple"):
    print("match found")
else:
    print("not found")
