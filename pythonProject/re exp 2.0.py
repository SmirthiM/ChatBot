import re

a = "Give me a Python Example"
x = '[a-m]'
ans=re.findall(x,a)
print(ans)
