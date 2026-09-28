# Problem: Teacher must count students first!
num_students = int(input("How many students? "))
total = 0

for i in range(num_students):
    grade = float(input("Enter grade: "))
    total += grade

average = total / num_students
print(f"Average: {average}")


# Complete sentinel pattern - all three parts labeled
grade = float(input("Enter grade (-1 to stop): "))  # Part 1: Prime input

while grade != -1:  # Part 2: Condition
    print(f"You entered: {grade}")
    grade = float(input("Enter grade (-1 to stop): "))  # Part 3: Update input

print("Done entering grades!")


#counter pattern
count = 1                 # Initialize
while count <= 5:         # Condition
    print(count)
    count += 1            # Update

#sentinel pattern
grade = float(input())    # Initialize (prime input)
while grade != -1:        # Condition
    print(grade)
    grade = float(input())  # Update (update input)


# Counter-controlled approach - must know count first
num_count = int(input("How many numbers? "))
total = 0

for i in range(num_count):
    number = int(input(f"Enter number {i + 1}: "))
    total += number

print(f"Total: {total}")

# Sentinel-controlled approach - stop when ready
total = 0
count = 0

number = int(input("Enter number (0 to stop): "))  # Prime input

while number != 0:  # Condition
    total += number
    count += 1
    number = int(input("Enter number (0 to stop): "))  # Update

print(f"Total of {count} numbers: {total}")