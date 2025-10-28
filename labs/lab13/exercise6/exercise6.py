age = int(input())

# TODO: Your code here
tickets_sold = 0
total_revenue = 0

while age != -1:
    if age >= 0 and age <= 12:
        price = 8
    elif age >= 13 and age <= 17:
        price = 10
    elif age >= 18 and age <= 64:
        price = 15
    elif age >= 65:
        price = 10
    
        

    tickets_sold += 1
    total_revenue += price

    age = int(input())

print(tickets_sold)
print(total_revenue)
