def reversedstring(s):
    if len(s)==1:
        return s[0]
    firstcharecter=s[0]
    return reversedstring(s[1:])+firstcharecter
b="adit jaldi"
print(reversedstring(b))