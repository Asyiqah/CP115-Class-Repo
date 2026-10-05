minutes = int(input())

customer = 0
total_minutes = 0

while total_minutes < 60:
    customer += 1
    total_minutes += minutes

    if total_minutes < 60:
        minutes = int(input())

print(customers)
print(total_minutes)
