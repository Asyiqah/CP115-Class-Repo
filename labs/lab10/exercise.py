for count in range(4):
    print(count)

for number in range(10, 15):
    print(number)

for value in range(0, 25, 5):
    print(value)

for multiplier in range(1, 11):
    print(f"7 x {multiplier} = {7 * multiplier}")

team_size = int(input("How many members? "))
for member in range(1, team_size + 1):
    name = input(f"Enter name for member {member}: ")
    print(f"Member {member}: {name}")

attempt = 1                 # initialize
while attempt <= 3:         # condition
    print(attempt)
    attempt += 1            # update

week = 1
while week <= 4:
    points = int(input(f"Week {week} points: "))
    if points >= 100:
        week += 2   # skip ahead a week
    else:
        week += 1