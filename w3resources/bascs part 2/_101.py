students = {"Bernita Ahner": 12, "Kristie Marsico": 11, "Sara Pardee": 14, "Fallon Fabiano": 11, "Nidia Dominique": 15}
{"Nilda Woodside": 12, "Jackelyn Pineda": 12.2, "Sofia Park": 12.4, "Joannie Archibald": 12.6, "Becki Saunder": 12.7}

max = 0
oldest_key = ""
for key, value in students.items():
    if value > max:
        max = value
        oldest_key = key #correct

print(f"the oldests student is {oldest_key} who is {max} years old")