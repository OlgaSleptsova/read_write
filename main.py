import os
import collections
from pprint import pprint


def read (filename):
    cook_book = {}

    with open(filename,encoding='utf8') as file:

        for ind, line in enumerate(file):
            line = line.strip()
            if ind == 0:
                list1 = []
                cook_book[line] =list1
                y = int(file.readline())

                for m in range(1,y+1):
                    len1 =file.readline().strip().split('|')
                    ingridients = {'ingredient_name': len1[0], 'quantity': int (len1[1]), 'measure': len1[2]}
                    list1.append(ingridients)

            if not line:
                x = file.readline()
                y = int(file.readline())
                list2 = []
                cook_book[x[0:-1]] = list2
                for m in range(1,y+1):
                    len1 =file.readline().strip().split('|')
                    ingridients = {'ingredient_name': len1[0], 'quantity': int(len1[1]), 'measure': len1[2]}

                    list2.append(ingridients)

    return cook_book

def write (filename, cook_book):

    with open('recipes_cleare.txt', 'w',encoding='utf8') as file:
        for x, line in cook_book.items():
            file.writelines(x+ os.linesep)
            for y in line:
                file.writelines(str(y) + os.linesep)

def read_and_write(filename,new_filename):
    cook_book = read(filename)
    write(new_filename,cook_book)

read_and_write('recipes.txt','recipes_cleare.txt')


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read('recipes.txt')
    k ={}
    for b1 in dishes:
        if b1 in cook_book:
            for f in cook_book[b1]:
                if f['ingredient_name'] in k:
                    y =(k[f['ingredient_name']].values())
                    list = list(y)
                    # print(list[1])
                    k[f['ingredient_name']] = {'measure': f['measure'], 'quantity': (f['quantity'] +list[1])* person_count}

                else:k[f['ingredient_name']]={'measure':f['measure'],'quantity':f['quantity']*person_count}






        else:print(f'{b1} -"Нет такого рецепта"')
    pprint(k)

#
get_shop_list_by_dishes(['Запеченный картофель','Омлет'],2)


