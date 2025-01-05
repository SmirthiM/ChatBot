a = "Banana"
dict={}
for i in a:
    v = dict.keys()
    if i in v:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)


