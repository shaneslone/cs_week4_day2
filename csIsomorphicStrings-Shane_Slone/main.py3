def csIsomorphicStrings(a, b):
    if len(a) != len(b):
        return False
    d = {}
    for i, char in enumerate(a):
        if char not in d:
            d[char] = b[i]
        elif d[char] != b[i]:
            return False
    return True