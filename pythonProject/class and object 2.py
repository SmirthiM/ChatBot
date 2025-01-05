name = input("Enter the username:")
p = input("Enter the password:")
a = 1234567890
b = "abcdefghijklmnopqrstuvwxyz"
c = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
d = "!@#$%^&*_-=+"
if name==a and name==b and name==c and name==d and name==8:
    print("correct username")
    if p==a and p==b and p==c and p==d and p==8:
        print("Login successfully")
    else:
        print("Incorrect username")
else:
    print("Incorrect password")


