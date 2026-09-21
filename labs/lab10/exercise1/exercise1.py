num_rounds = int(input())
score = 0
bonus = 0
final_score = 0

for rounds_processed in range (1, num_rounds + 1):
    score = int(input())
    if score > 100:
        bonus = score * 0.2
    else:
        bonus = 0

    final_score = final_score + score + bonus

print(f"{final_score:.1f}")
print(rounds_processed)
