import re

val = "01012341234abc"
pattern = "^01[016789][1-9]\\d{6,7}"

if re.match(pattern, val):
    print("matched")

else:
    print("invalid")