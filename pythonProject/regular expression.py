import re
text = "Welcome to python smirthi07.m@gmail.com"
result = re.compile("[a-z]+[0-9]+.[a-z]@[a-z]+")
ans = result.findall(text)
print(ans)