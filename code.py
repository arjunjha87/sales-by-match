def sockMerchant(n, ar):
    pairs = 0
    color = set()
    for i in range(len(ar)):
        if ar[i] not in color:
            color.add(ar[i])
        else:
            pairs += 1 
            color.remove(ar[i])
    return pairs
