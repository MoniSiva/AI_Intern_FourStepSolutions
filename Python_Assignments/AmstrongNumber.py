number = input("Enter a number:")
sum_of_digits = 0
for iterator in number:
    iterator = int(iterator)
    sum_of_digits = sum_of_digits + iterator * iterator * iterator

if number == str(sum_of_digits):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
