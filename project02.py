'''Create a miltiplication table application where user will enter a senital
value n and the application will display the mathematical multiplcation table
given senital value n Constraints: Make use of oop concept class methid and attribute'''



class Multiplication__table:
    def __init__(self,n):
        self.n=n
    def display__multiplication__tables(self):
        for i in range(2,self.n+1):
            print("Multiplication table of",i)
            for j in range(1,11):
                print(i,"*",j,"=",i*j)
n=int(input("Enter a number: "))
Multiplication__table(n).display__multiplication__tables()


