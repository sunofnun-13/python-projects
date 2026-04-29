# ==================================================
# Dictionaries.py  - Storing data in key/value pairs 
# Run it: python3 dictionaries.py 
# ==================================================

# A dictionary sotres data as key: value paires 
# THink of it like a real dictionary - you look up a word (key) and gets it definition (value). 

player = {
    "name": "Josh",
    "level": 10, 
    "health": 100 
} 

print(player)

# --- ACCESSING VALYES --- #
# Use the key in square brackets to get its value. 

print(player["name"])  # Josh
print(player["level"]) # 10 
print(player["health"]) # 