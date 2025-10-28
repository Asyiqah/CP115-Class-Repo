grade = float(input())

# TODO: Your code here
valid_count = 0
average = 0
total_grade = 0

while grade > 0:
    if grade > 100:
        pass

    valid_count += 1
    total_grade += grade
    

average = total_grade / valid_count

print(valid_count)
print(f"{average:.2f}")
