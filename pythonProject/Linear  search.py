    # A=[0,0,0,0,0,0,0,0,0,]
    # found =0
    # n=int(input("Enter the number to search:"))
    # print("Enter n numbers")
    # for i in range(0,n):
    #     A[i]=int(input())
    # key = int(input("Enter a key to be searched"))
    # for i in range(0,n):
    #     if key==A[i]:
    #         print("Not found")
    #         found+=1
    #     else:
    #         continue
    # if found==0:
    #     print("Key not found")





    #
    # a = [3,2,4,1,5]
    # key = int(input("Enter the number to search:"))
    # for i in range(1,6):
    #     if(i==key):
    #         print("Found")
    #         break
    # if(key!=i):
    #     print("Not found")















def linear_search(arr,target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i

        return -1
array = [12,3,4,6,8]
target = int(input("Enter the number to search:"))
index = linear_search(array,target)

if index != -1:
     print("Found at:",index)
else:
     print("Not found")




























