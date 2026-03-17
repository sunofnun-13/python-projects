# ============================================================
# LISTS.PY — Storing multiple values in one variable
# Run it: python3 lists.py
# ============================================================

# A list holds multiple items inside square brackets [].
# Items are separated by commas.

friends = ["Josh", "Mike", "Sarah"]

# --- ACCESSING ITEMS ---
# Lists start counting at 0, not 1.
print(friends[0])   # Josh
print(friends[1])   # Mike
print(friends[2])   # Sarah

# --- ADDING ITEMS ---
friends.append("Carlos")
print(friends)      # ['Josh', 'Mike', 'Sarah', 'Carlos']

# --- REMOVING ITEMS ---
friends.remove("Mike")
print(friends)      # ['Josh', 'Sarah', 'Carlos']

# --- LIST LENGTH ---
print(len(friends)) # 3

# --- LOOPING THROUGH A LIST ---
# A for loop visits each item in the list one at a time.
for friend in friends:
    print("Hello " + friend + "!")
