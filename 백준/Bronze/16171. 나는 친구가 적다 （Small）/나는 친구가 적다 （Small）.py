import re

S = input()
K = input()

# 1q2w3e4r5t6y
# qwerty

string = re.sub(r'[0-9]','', S)

if K in string:
    print("1")
else:
    print("0")