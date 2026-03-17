# ============================================================
# STRINGS_AND_NUMBERS.PY — Working with text and math
# Run it: python3 strings_and_numbers.py
# ============================================================

# --- STRINGS (text) ---
# Strings are wrapped in quotes.

first_name = "Josh"
last_name  = "Nunez"

# Use + to join strings together (called concatenation).
full_name = first_name + " " + last_name
print(full_name)   # Josh Nunez

# --- NUMBERS ---
# int   = whole number  (25)
# float = decimal number (5.9)

age    = 25
height = 5.9

print(age + 10)    # 35  — regular math
print(height)      # 5.9

# --- MIXING STRINGS AND NUMBERS ---
# You can't join a string and a number directly with +.
# Wrap the number in str() to convert it to a string first.

print("I am " + str(age) + " years old.")
