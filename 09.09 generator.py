import random
surnames_list=['Иванов', 'Петров', 'Сидоров', 'Дроздов', 'Кошкин']
names_list=['Иван', 'Петр', 'Александр', 'Владимир', 'Андрей']
father_name=['Иванович', 'Петрович', 'Юрьевич', 'Александрович', 'Владимирович']
def generator_x(num):
    i = 0
    while i < num:
        yield random.choice(surnames_list) + ' ' + random.choice(names_list) + ' ' + random.choice(father_name)
        i += 1

gen = generator_x(3)
for x in gen:
    print(x)