# Programmer's Name = Asyiqah Nur Syahirah
#required to create a Python program that asks the user to enter the monthly usage and then calculates and displays the amount of the bill to be paid after receiving the discount.

#define the data type
usage = 0
discount = 0
bill_payment = 0

#get data from user
usage = float(input("monthly usage? "))
bill_payment = float(input("bill payment? "))

if usage < 50 :
    discount = 0 * bill_payment    #No discount will be given for Usage less than RM50 per month

elif usage <= 100 :
    discount = 0.05 * bill_payment      #Get a 5% discount for Usage less than or equal to RM100 per month

else :
    discount = 0.2 * bill_payment    #Get a 20% discount for Usage more than RM100 per month

bill_to_pay = bill_payment - discount
print(f"amount of the bill to be paid = {bill_to_pay}")