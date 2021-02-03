def csWordPattern(pattern, a):
    d = {}
    a = a.split(" ")
    if len(pattern) != len(a):
        return False
    for i, char in enumerate(pattern):
        cur = a[i]
        if char not in d:
            if cur not in d.values():
                d[char] = cur
            else:
                return False
        elif d[char] != cur:
            return False
    return True