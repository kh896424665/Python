def findMinAndMax(L):
    max = L[0]
    min = L[0]
    for item in L:
        if item > max:
            max = item
        if item < min:
            min = item
    return (max, min)
print(findMinAndMax([7,1]))