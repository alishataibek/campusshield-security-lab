import re

users = [
    ("tamerlan", "123456"),
    ("alisha", "password"),
    ("roman", "qwerty123"),
    ("sara", "Tr0ub4dor&9"),
    ("yerlan", "Horse-Battery-Staple-77"),
]

def check(password):
    problems = []
    if len(password) < 12:
        problems.append("shorter than 12")
    if not re.search(r"[0-9]", password):
        problems.append("no number")
    if not re.search(r"[^A-Za-z0-9]", password):
        problems.append("no special character")
    return problems

for user, password in users:
    problems = check(password)
    if problems:
        print(f"{user:10} REJECTED  ({', '.join(problems)})")
    else:
        print(f"{user:10} ACCEPTED")
