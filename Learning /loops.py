# ============================================================
# LOOPS.PY — Repeating things
# Run it: python3 loops.py
# ============================================================

# --- FOR LOOP ---
# Use when you know how many times to repeat.
# range(5) produces the numbers 0, 1, 2, 3, 4

print("--- For Loop ---")
for i in range(5):
    print("Count: " + str(i))

# --- WHILE LOOP ---
# Use when you want to keep repeating UNTIL a condition is False.

print("--- While Loop ---")
count = 1
while count <= 5:
    print("Count: " + str(count))
    count = count + 1   # Move count forward each time or this runs forever!

# --- KEY DIFFERENCE ---
# for loop   → repeat a set number of times
# while loop → repeat until something changes
