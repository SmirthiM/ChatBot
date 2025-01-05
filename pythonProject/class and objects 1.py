class factorial:
    def fact(self,num):
        n = 1
        for i in range(1,num+1):
            n = n*i
        print("The factorial number is:",n)
obj = factorial()
obj.fact(int(input("Enter the number:")))
