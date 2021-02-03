def csGroupAnagrams(strs):
    d ={}
    for word in strs:
        cur = list(word)
        cur.sort()
        cur = "".join(cur)
        if cur not in d:
            d[cur] = []
        d[cur].append(word)
    return list(d.values())