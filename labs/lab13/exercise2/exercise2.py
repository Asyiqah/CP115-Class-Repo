# TODO: Your code here
number = 1

while number != 100:
    if number % 7 == 0 and number % 13 == 0:
        found_number = number
        break
    number += 1

print(found_number)
