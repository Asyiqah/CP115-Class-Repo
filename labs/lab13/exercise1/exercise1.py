correct_password = "python123"

# TODO: Your code here

attempts_used = 0
login_successful = False


while attempts_used < 3:
    password = input()
    attempts_used += 1
    if password == correct_password:
        login_successful = True
        break

    
    
    

print(login_successful)
print(attempts_used)
