num = int(input("Number: "))

factorial = 1
for i in range(1,num + 1):
    factorial = factorial*i
print("The factorial of",str(num),"is",str(factorial))