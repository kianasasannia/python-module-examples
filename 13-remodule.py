import re

s="this is a test"
x=re.search("^this.*test$",s)
if x:
    print("Ok")

y=re.findall("he",s)
print(y)

print(re.split("\s",s))
re.sub()


email="as.gha-r123@gmail.com"

pattern=r"^[\w\.-]+@[\w\.-]+.(com|org|net)$"

if re.match(pattern,email):
    print("valid")
else:
    print("invalid")

s="Asghar"

upper=re.findall(r"[A-Z]",s)
print(upper)

lower=re.findall(r"[a-z]",s)
print(lower)

number=re.findall(r"[1-9]",s)
print(number)

if not upper :
    print("at least one upper character needed ")
if not lower :
    print("at least one lower character needed ")
if not number :

    print("at least one number needed ")
