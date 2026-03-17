# ============================================================
# INPUT.PY — Getting information from the user
# Run it: python3 input.py
# ============================================================

# input() shows a prompt and waits for the user to type.
# Whatever they type is stored as a STRING.

name = input("What is your name? ")
age  = input("How old are you? ")

print("Hello " + name + "!")
print("You are " + age + " years old.")

# --- IMPORTANT ---
# input() always returns a string, even if the user types a number.
# To do math with it, convert it using int() first.

num = input("Pick a number: ")
print("Your number doubled is: " + str(int(num) * 2))
