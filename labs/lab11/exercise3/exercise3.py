number = int(input())

count = 0
biggest_jump = 0
previous = 0

while number != 0:
    count += 1
    new_number = int(input())

    if count > 1:
        jump = number - previous

    if jump > biggest_jump:
        biggest_jump = jump

    previous = numbernumber = int(input())

print(count)
print(biggest_jump)
