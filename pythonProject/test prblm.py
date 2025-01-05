path = ["TH","GA","IC","HA","TE","LU","NI","CA"]
price = [800,600,750,900,1400,1200,1100,1500]
source = str(input("Enter the Source place:"))
destination = str(input("Enter the Destination place:"))
i1 = path.index(source)
i2 = path.index(destination)
if i1>i2:
    print(i1,i2)
    a=price[i2:i1+1]
    b=0
    for i in a:
        b+=1
        print(b)
        s=b/1000
        pr=s*5
        print("{pr}INR")
elif i1<12:
    print(i1,i2)
    a = price[i1:i2+1]
    b = 0
    for i in a:
        b +=1
    print(b)
    s = b/1000
    pr = s*5
    print("{pr}INR")



