n = int(input("Enter the number:"))
sub = ["Tamil","English","Mathematics","Biology","Commerce"]
sub1 = ["Economics"]
if n==1:
    sub.append(input("Enter the subject to add:"))
    print(sub)
elif n==2:
    sub.insert(int(input("Index number to add:")),input("Enter the subject to add:"))
    print(sub)
elif n==3:
    del sub[int(input("Enter the index number to delete item:"))]
    print(sub)
elif n==4:
    sub.remove(input("Enter the value to remove:"))
    print(sub)
elif n==5:
    sub.pop(int(input("Enter the index number to remove item:")))
    print(sub)
elif n==6:
    sub.clear()
    print(sub)
elif n==7:
    print("length:",len(sub))
elif n==8:
    sub2=sub+sub1
    print("join the two list",sub2)
elif n==9:
    print(input("item exist in list :")in sub)
elif n==10:
    sub1=sub.copy()
    print("copy sub list to sub1 list:",sub1)
elif n==11:
    sub.reverse()
    print("reverse the list:",sub)
elif n==12:
    sub.sort()
    print("ascending ordered list:",sub)
elif n==13:
    sub.sort(reverse=True)
    print("descending ordered list:",sub)
else:
    print("invalid input")

