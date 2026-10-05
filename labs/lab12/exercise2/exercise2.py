number = 0
found_number = 0

while number < 100:
    number += 1
    if number % 7 == 0 and number % 13 == 0:
        found_number = number
        break

print(found_number)
