"""
target = 9
found = False

for number in range(10):
    print(f'Checking number: {number}')
    if number == target:
        found = True
        print(f'Found {target}!')
        break  # Exit loop immediately
    print(f'Still inside loop, checking next...')  # This runs before break

print(f'Search complete. Found: {found}')  # Python jumps here after break


# Password validation with break
attempts = 0

while attempts < 3:
    password = input("Enter password: ")
    attempts += 1

    if password == "secret123":
        print("Access granted!")
        break  # Exit immediately

    print(f"Wrong password. {3 - attempts} attempts remaining.")
"""
"""
# Problem: This adds ALL numbers including 3
total = 0

for number in range(5):
    print(f'Processing: {number}')
    total += number
    print(f'Added to total. Current total: {total}')

print(f'Final total: {total}')
"""
"""
# Solution: Skip number 3 with continue
total = 0

for number in range(5):
    print(f'Processing: {number}')

    if number == 3:
        print('Skipping 3!')
        continue  # Skip to next iteration

    total += number  # This line skipped when continue executes
    print(f'Added {number}. Current total: {total}')  # This too

print(f'Final total: {total}')  # Python continues here after each iteration
"""
"""
# CORRECT - Process only even numbers
number = 0

while number < 10:
    number += 1  # Counter BEFORE continue

    if number % 2 != 0:  # If odd
        continue  # Skip odd numbers

    # This only executes for even numbers
    print(f"Processing even number: {number}")
"""
"""
# WRONG - Creates infinite loop!
number = 0

while number < 10:
    if number % 2 != 0:  # If odd
        continue  # Skips the increment below!

    print(f"Processing even number: {number}")
    number += 1  # This never executes when number is odd!
"""

number = 0

while number < 10:
    print(number)
    number += 1