principal_amount = float(input("Enter principal Amount:"))
rate_of_interest = float(input("Enter Rate of Interest:"))
time = float(input("Enter Time Period:"))
simple_interest = (principal_amount*rate_of_interest*time)/100
total_amount = principal_amount + simple_interest
print("The simple interest is {} and the total amount is {}".format(simple_interest,total_amount))