n = [0, 1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7, 8, 9]

def unique(n):
    list = []
    unique_n = set(n)

    for i in unique_n:
        list.append(i)
    
    return list
print (unique(n))

A = [0, 2, 7, 4, 4, 7, 9, 1, 4, 6]
B = [1, 5, 3, 2, 7, 6, 6, 0, 8, 5]
C = list(set(A) & set(B))
print(C)