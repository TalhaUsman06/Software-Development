#Recursions

#Factorial Function
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
 
num = int(input("Enter Number: "))
print("\nFactorial:",factorial(num))
 
 
print("\nFACTORIAL: ")
for i in range(1,num):
    print("Fatorial of",i,": ", factorial(i))
 
 
 #Fibonacci Function
def fibonacci(n):
    if n <=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
   
print("\n\nFibonacci series :")
for i in range(3,num):
    print("Fibonacci of",i,": ", fibonacci(i))
