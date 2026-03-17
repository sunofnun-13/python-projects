# ============================================================
# IF_ELSE.PY — Making decisions
# Run it: python3 if_else.py
# ============================================================

# if/elif/else lets your program choose what to do
# based on whether a condition is True or False.

age = int(input("How old are you? "))

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

# --- HOW IT WORKS ---
# Python checks each condition top to bottom.
# It runs the FIRST block that is True, then skips the rest.

# --- COMMON COMPARISON OPERATORS ---
# ==   equal to
# !=   not equal to
# >    greater than
# <    less than
# >=   greater than or equal to
# <=   less than or equal to
