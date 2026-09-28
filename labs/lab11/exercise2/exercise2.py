score = int(input())

total_a = 0
total_b = 0
score_number = 1

while score != -1:

    if score_number % 2 == 1:  #if remainder is = 1 which means it is for score A
        total_a += score
    else:                       #if remainder is = 0 which means it is for score B
        total_b += score

    score_number += 1
    score = int(input())

if total_a > total_b:
    winner = "A"
elif total_b > total_a:
    winner = "B"
else:
    winner = "Tie"

print(total_a)
print(total_b)
print(winner)
