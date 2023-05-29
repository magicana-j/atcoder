def can_reach_target(s):
    five_ = ["dream", "erase"]
    seven_ = ["dreamer", "eraser"]

    l = len(s)

    if l == 0:
        return True
    elif l < 5 or l == 6:
        return False
    else:
        for _ in five_:
            if _ == s[-5:]:
                return can_reach_target(s[:-5])
        for _ in seven_:
            if _ == s[-7:]:
                return can_reach_target(s[:-7])


if __name__ == "__main__":
    t = input()
    if can_reach_target(t):
        print("YES")
    else:
        print("NO")
