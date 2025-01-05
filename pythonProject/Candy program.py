n = 10
k = int(input("Enter the candies need:"))
if k==0:
    print("Invalid input")
    print("number of candies available:",n-k)
elif n-k>=0:
    print("No of candies sold",k)
    print("number of candies available:",n-k)