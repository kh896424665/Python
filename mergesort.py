def mergesort(A):
    if len(A) <= 1:
        return A
    r = len(A)
    m = r//2
    left = mergesort(A[0:m])
    right = mergesort(A[m:r])
    return merge(left,right)

def merge(L,R):
    B = []
    i = j = 0
    while i <len(L) and j < len(R):
        if L[i]<=R[j]:
            B.append(L[i])
            i = i+1
        else:
            B.append(R[j])
            j = j+1
    if i == len(L):
        B.extend(R[j:])
    else:
        B.extend(L[i:])
    return B


print(mergesort([2, 5, 3, 8, 6, 9, 1, 4, 7]))