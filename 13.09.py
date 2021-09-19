def sortirovka_1(spisok):
    a = spisok
    a.sort( )
    return a

def sortirovka_2(spisok):
    a = spisok
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

print(sortirovka_1([768, 104, 34, 10005, 15000000, 1, 81, 1630, 90, 123]))
print(sortirovka_2([1, 22, 333, 4444, 55555, 6666, 777, 88, 9, 10]))