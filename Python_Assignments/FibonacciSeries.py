a = -1
b = 1
c = 0
number = int(input("Enter n value: "))
print("Fibonacci series : ")
for i in range(number):
    c = a+b
    print(c)
    a=b
    b=c