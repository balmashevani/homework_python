import string
import random

s = string.ascii_letters
def let(s):
    print(random.choice(s))
    

def create(num):
    result = ''
    for i in range (num):
        result+=random.choice(string.ascii_letters)
    return result


def count_str(s):
    big = 0
    small = 0
    for sym in s:
        if sym.isupper():
            big += 1
        else:
            small += 1
    if big > small:
        return s, 1
    elif small > big:
        return s, 0
    else: 
        return s, -1

def percentage(slova):
    a = slova
    big = []
    small = []
    middle = []
    for i in a:
        b = list(i)
        big_ = 0
        small_ = 0
        for sym in b:
            if sym.isupper():
                big_ += 1
            else:
                small_ += 1
        if big_ > small_:
            big.append(i)
        elif small_ > big_:
            small.append(i)
        else: 
            middle.append(i)
    print('Big (%):', (len(big) / len(a)) * 100)
    print('Small (%):', (len(small) / len(a)) * 100)
    print('Middle (%):', (len(middle) / len(a)) * 100)
               
print(count_str(create(8)))  

s = string.ascii_letters
def let(s):
    print(random.choice(s))
    

def f(length, num):
    return [create(length) for i in range(num)]
    
print(f(8, 10))
percentage(f(6, 10))