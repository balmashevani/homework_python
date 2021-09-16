names = ['Балмашева Наталья Игоревна', 'Виноградова Юлия Игоревна', 'Путин Владимир Владимирович']
def initials(name):
    l = name.split()
    return l[0] + ' '+ l[1][0:1] + '.' + l[2][0:1] + '.'

def initials_more(names):
    return [initials(name) for name in names]

def initials_multiply(name, num):
    return [name for i in range(num)]


print(initials_more(names))
print(initials_multiply('Виноградова Юлия Игоревна', 7))