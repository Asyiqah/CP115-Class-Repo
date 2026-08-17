# Lab 07 scratch file
# Use this file to try out the code from the lab as you follow along.
value = 1

if(value == 1):
     print("Value is 1")
else:
  print("Value is not 1")

# other samples
  value = 1

if(value == 1):
     print("Value is 1")
     print("This is an additional print statement.")
else:
    print("Value is not 1")

# another sample
print(0.1 + 0.2)

#round the answer of decimal
answer = 0.1 + 0.2
print(round(answer, 2))

# Test addition and subtraction
result1 = 25 + 15
result2 = 100 - 25
print(f"25 + 15 = {result1}")
print(f"100 - 25 = {result2}")

# Test multiplication and division
result3 = 8 * 7
result4 = 20 / 4
print(f"8 * 7 = {result3}")
print(f"20 / 4 = {result4}")

# Test floor division, modulus, and powers
result5 = 17 // 5
result6 = 17 % 5
result7 = 3 ** 4
print(f"17 // 5 = {result5}")
print(f"17 % 5 = {result6}")
print(f"3 ** 4 = {result7}")

# Test division - always returns float
division = 10 / 2
print(f"10 / 2 = {division} (type: {type(division)})")

# Test floor division - returns int when both operands are int
floor_div = 10 // 3
print(f"10 // 3 = {floor_div} (type: {type(floor_div)})")

# Test modulus - returns int when both operands are int
modulus = 17 % 5
print(f"17 % 5 = {modulus} (type: {type(modulus)})")

# Test exponentiation - returns int when both operands are int
power = 2 ** 3
print(f"2 ** 3 = {power} (type: {type(power)})")

# Test mixing int and float in different operations
mixed_division = 15.0 / 4        # float / int = float
mixed_floor = 15.0 // 4          # float // int = float
mixed_modulus = 17.0 % 5         # float % int = float
mixed_power = 2.0 ** 3           # float ** int = float

print(f"15.0 / 4 = {mixed_division} (type: {type(mixed_division)})")
print(f"15.0 // 4 = {mixed_floor} (type: {type(mixed_floor)})")
print(f"17.0 % 5 = {mixed_modulus} (type: {type(mixed_modulus)})")
print(f"2.0 ** 3 = {mixed_power} (type: {type(mixed_power)})")

# Compare without and with brackets
result1 = 10 + 3 * 2     
result2 = (10 + 3) * 2    
print(f"10 + 3 * 2 = {result1}")
print(f"(10 + 3) * 2 = {result2}")

# Complex BODMAS example
expression = 3 + 2 ** 2 * 4 - 6 / 2
print(f"3 + 2 ** 2 * 4 - 6 / 2 = {expression}")

# Let's break it down step by step
step1 = 2 ** 2    
step2 = step1 * 4  
step3 = 6 / 2     
final = 3 + step2 - step3 
print(f"Step 1 (Powers): 2 ** 2 = {step1}")
print(f"Step 2 (Multiply): {step1} * 4 = {step2}")
print(f"Step 3 (Division): 6 / 2 = {step3}")
print(f"Final: 3 + {step2} - {step3} = {final}")

# Same numbers, different brackets = different results
without_brackets = 5 + 3 * 2 ** 2
with_brackets = (5 + 3) * 2 ** 2
different_brackets = 5 + (3 * 2) ** 2
print(f"5 + 3 * 2 ** 2 = {without_brackets}")
print(f"(5 + 3) * 2 ** 2 = {with_brackets}")
print(f"5 + (3 * 2) ** 2 = {different_brackets}")

# Test assignment operators
score = 100
print(f"Starting score: {score}")

score += 10     # Add 10
print(f"After += 10: {score}")

score -= 5      # Subtract 5
print(f"After -= 5: {score}")

score *= 2      # Multiply by 2
print(f"After *= 2: {score}")

score //= 3     # Floor division by 3
print(f"After //= 3: {score}")

score %= 15     # Modulus by 15
print(f"After %= 15: {score}")

score **= 2     # Square it
print(f"After **= 2: {score}")