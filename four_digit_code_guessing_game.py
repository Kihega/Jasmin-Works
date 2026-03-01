import random

digits = random.sample(range(0,10),4)
secret_code = "".join(map(str,digits))

while True:
    guess = input("Enter 4 digit code: ")

    if guess == secret_code:
        print("Correct! Code guessed.")
        break

    result = ""
    for i in range(4):
        if guess[i] == secret_code[i]:
            result += "*"
        elif guess[i] in secret_code:
            result += "+"
    print("Hint:", result)
