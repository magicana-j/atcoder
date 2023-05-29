def can_reach_target(s):
    five_ = ["dream", "erase"]
    six_ = ["eraser"]
    seven_ = ["dreamer"]

    l = len(s)

    if l == 0:
        return True
    elif l < 5:
        return False
    else:
        for _ in seven_:
            if _ == s[-7:]:
                return can_reach_target(s[:-7])
        for _ in six_:
            if _ == s[-6:]:
                return can_reach_target(s[:-6])
        for _ in five_:
            if _ == s[-5:]:
                return can_reach_target(s[:-5])


t = input()
if can_reach_target(t):
    print("YES")
else:
    print("NO")
