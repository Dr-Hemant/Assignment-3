'''Printing Factorial of a Number given by user'''
def factorial(n):
   if (n == 0 or n == 1):
       return 1
   else :
       return n * factorial(n-1)


num = float(input("Enter Number: "))
print(f"Factorial of {num} is {factorial(num)}.")

