students = [
    ("Aruzhan", 19, "F", "Kazakhstan", "Cyber"),
    ("Omar",    20, "M", "Jordan",     "Cyber"),
    ("Priya",   22, "F", "India",      "CS"),
    ("Daniel",  24, "M", "Germany",    "Business"),
    ("Fatima",  18, "F", "UAE",        "Business"),
    ("Timur",   21, "M", "Kazakhstan", "CS"),
    ("Layla",   19, "F", "Lebanon",    "Cyber"),
    ("Rahul",   23, "M", "India",      "CS"),
    ("Sofia",   25, "F", "Italy",      "Business"),
    ("Yusuf",   20, "M", "Egypt",      "Cyber"),
    ("Mariam",  18, "F", "Egypt",      "Business"),
    ("Nurlan",  22, "M", "Uzbekistan", "CS"),
    ("Hana",    21, "F", "Pakistan",   "CS"),
    ("Lukas",   26, "M", "France",     "Business"),
    ("Aigerim", 20, "F", "Uzbekistan", "Cyber"),
]

region = {"Kazakhstan": "Central Asia", "Uzbekistan": "Central Asia",
          "UAE": "Middle East", "Jordan": "Middle East", "Lebanon": "Middle East", "Egypt": "Middle East",
          "India": "South Asia", "Pakistan": "South Asia",
          "Germany": "Europe", "Italy": "Europe", "France": "Europe"}

def age_range(age):
    if age <= 20:
        return "18-20"
    elif age <= 23:
        return "21-23"
    else:
        return "24+"

def count_unique(rows):
    return sum(1 for r in rows if rows.count(r) == 1)

before = [(age, g, nat, prog) for name, age, g, nat, prog in students]

after = [(age_range(age), g, region[nat], prog) for name, age, g, nat, prog in students]

print("BEFORE:")
for s in students:
    print("  ", s)
print("\nAFTER:")
for a in after:
    print("  ", a)

print("\nUnique records before:", count_unique(before), "of", len(before))
print("Unique records after: ", count_unique(after), "of", len(after))
