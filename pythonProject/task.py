a=str(input("Enter a word:"))
dict={}
for i in a:
    tue=dict.keys()
    if i in tue:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)