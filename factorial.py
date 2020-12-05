def factorial(a):
   if a==1:
    return 1
   else:
    return a*factorial(a-1)
b=factorial(3)
print("Factorial of 3 is",b)


