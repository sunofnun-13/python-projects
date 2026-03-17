# ============================================================
# GUESSING_GAME.PY — Mini project using everything so far
# Run it: python3 guessing_game.py
# ============================================================

# This game uses: variables, input, int(), if/elif/else, while loop

secret_number = 7
attempts      = 0
max_attempts  = 5

print("Guess the number (1–10). You have " + str(max_attempts) + " tries.")

while attempts < max_attempts:
    guess    = int(input("Your guess: "))
    attempts = attempts + 1

    if guess == secret_number:
        print("Correct! You got it in " + str(attempts) + " tries.")
        break
    elif guess < secret_number:
        print("Too low!  Tries left: " + str(max_attempts - attempts))
    else:
        print("Too high! Tries left: " + str(max_attempts - attempts))

if attempts == max_attempts and guess != secret_number:
    print("Out of tries. The number was " + str(secret_number) + ".")
