def can_reach_target(s):
    patterns = ["dream", "dreamer", "erase", "eraser"]

    while s:
        found = False
        for pat in patterns:
            if s.endswith(pat):
                s = s[: -len(pat)]
                found = True
                break
        if not found:
            return False

    return True


test_cases = [
    "dreameraser",
    "dreamerase",
    "dreamererase",
    "erasedreamerer",
    "dreamdream",
    "erasereraseer",
    "dreamerer",
    "eraseer",
    "dream",
    "eraser",
]

for t in test_cases:
    if can_reach_target(t):
        print(t + " " + "YES")
    else:
        print(t + " " + "NO")
