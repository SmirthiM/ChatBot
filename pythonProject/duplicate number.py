sum=[]
even=[]
odd=[]
for a in range(1,10):
    print(a*11)
    i = a+a
    sum.append(i)
    if i%2 ==0:
        even.append(i)
    else:
        odd.append(i)
for b in range(1,10):
    print(b*111)
    j = b+b+b
    sum.append(j)
    if j%2==0:
        even.append(j)
    else:
        odd.append(j)
print("sum=",sum)
print("even=",even)
print("odd=",odd)
for x in odd:
    for y in range(3,x+1,6):
        print("",end="")
        if y%2!=0:
            print(y,end="")
    print("")
