

# 1-й урок

'''a = 5
b = 3
x = 'mk'
s = 'NARUTOOOOOO'
m = 'SAAASUUUKEEE'
print(a*b,x,s,m,'\n', 'что за ', sep='-', end='*** ')'''
import csv
import os

'''a = input("Умножение на 5, братанчик.\n")
print(int(a) * 5)'''

'''cpy = 'SASUKE'
print(cpy)
print(cpy)'''

'''print('Как тебя зовут?')
name = input()
print('Привет,', name)'''

'''b = 'dva'
c = 'dvajdi'
s = 'chetire'
print(c, b, '=', s, end='!')
'''
# 2-й урок

# переменная.replace("test", "") меняет текст на указанный
# переменная[0] показывает индекс (символ на позиции)
# 'текст {}'.format('NARUTO') происходит замена сразу в переменной --> 'текст NARUTO' с помощью индекса можно менять расположение format

'''Функции для работы со строками: str(n), len(s), chr(s) - в переменной должно быть число определенного
    символа в таблице, и он выведет этот символ, ord(s) - получаем индекс определенного символа в таблице'''

# списки
# list('spisok') --> ['s','p','i','s','o','k']
# a = ['a', 2, 2.3, true]


'''num = [1,2,3,4,5]
people = ['tom', 'reddle', 'garri', 'potter']

print(num)
print(people)'''

'''str = "h12341 42 dog 53.1 NARUTO423 11 2 pop"
str = [int(s) for s in str.split() if s.isdigit()]

print(str)'''

'''print('cow'[::-1])
print(''.join(reversed('test')))'''

# print(set(список)) выводит только элементы которые в единственном экземпляре
# print(len(set(список))) выводит кол-во элементов которые в единственном экземпляре

'''a = []
if not a:
    print('pust')
else:
    print('est')
    print(a)'''
# проверка пустой ли список

# кортеж - создаётся при помощи (), неизменный список (Как const в JS)
# если кортеж с одним элементом, то запятая обязательна!
# можно дать название кортежу
# кортеж можно хранить в списке
# кортеж - tuple
# с помощью ''.join() можно переобразовать кортеж в строку

# 3-й урок

# чтобы создать множества надо использовать {}

'''a = {1,2,3,4,5,1,2,3}

print(a)'''

# Создание множества из списка

'''list = ['a', 'b', 'asdfaf', True, False, 123]

oList = set(list)
print(oList)'''

# Пустое множество

'''set = set()'''

# {} - пустой словарь!

# метод add() добавляет значение в множество

'''set = {1,2}
set.add(4)
print(set)'''

# update()

# практика

'''a = {}
print(type(a))
af = set()
print(type(af))'''


'''set = {1, 2, 3}
print(set)
set.add(3)
print(set)
set.add(4)
print(set)'''


'''set = {1,2,3}
set.update({3,4,5,6})
print(set)'''
# ЕСЛИ ДОБАВЛЯЕМ 1 ЭЛЕМЕНТ, ТО .add, ЕСЛИ БОЛЬШЕ 1-ОГО, ТО .update


# .discard() удаление из множества (только одно) ошибку при удаление не сущ. элемента ничего не будет

'''set = {1, 2, 3, 4}
set.discard(2)''' # output 1,3,4,5
'''set.discard(5)''' # ничего не будет

# с помощью .remove можно тоже удалить (только один раз), но будет ошибка если введем элемент которого нет

# .clear удаляет сразу всё множество, а .pop одно значение (с начала)

# .union возвращает всё множество в рандоме
# .intersection  возвращает пересекающиеся элементы
# .diffrence возвращает те которые есть в одном, но нет в другом

'''stat = {1,2,3}
stat2 = {3,4,5}

print(stat.intersection(stat2))''' # выведет 3, т.к оно пересекается и там и там
'''print(stat.difference(stat2))''' # выведет уникальные значения для переменной перед точкой


# объеденение множеств происходит с помощью |


# сравнение множеств >, <, ==, !=, <=, >=

# преобразование: set() в множество, dict() в словарь

'''a = [1,1,2,2,4,5,3,3]
print(a)
a = set(a)
print(a)'''


# словари

'''dict = {
    'person': {
        'name': 'Alex',
        'age': 28,
        'skill': ['asdasd', 'asdasd'],
        'param': {'key': 'value'}
    }
}

print(dict)'''

# метод .fromkeys может пополнять ключи данными
# метод .get выдает value по его ключу пользователю

# ПРАКТИКА

'''z = {
    'name': 'Alex',
    'age': 28,
    'skill': ['asdasd', 'asdasd'],
    'param': {'key': 'value'}
}

users = [
    ['name', 'Sasuke'],
    ['age', 28],
    ['kekeiGenkai', 'shringan'],
    ['enemies', ['Uchiha Madara', 'Kaguya Ootsusuki']],
    ['bidju', {'bName': 'shukaku'}]
]
b = dict(users)

print(b)
print(z)'''

# урок 4 Условия, циклы, функции

# bool() True / False
# False - пустая строка, 0, пустой список/кортеж
# нельзя сложить str + bool
# True - 1, False - 0

# Операторы - это функционал, представленный в виде символов

# Тест True False и знаков сравнения
'''
a = 123
b = 6532
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print(a > b)
print(a < b)'''

# Логические операторы or, and, and not (приоритет на True (кроме and not))

# and ищет False
'''
True and True = True
True and False = False
False and False = False
'''

# or ищет True
'''
True or True = True
True or False = True
False or False = False
'''

# and not выдаёт True только если True первым значением стоит
'''
False and not True = False
True and not False = True
False and not False = False
'''

# Условные операторы: if, else, elif (отступы важны)

# if
'''a = True
b = False
if a == True:
    print('SASUKE')
    if b == True:
        print('Yes')
        print('Yes')
    print('NARUTO')
print('Hi')
'''

# else
'''
a = 7
b = 9
if a>b:
    print(a) --> False
else:
    print(b) --> True
'''

# elif
'''
a = 3
b = 6
if a > 5:
    print('a>5')
elif a < 5:
    print('a<5')
else:
    print('ADASDASDASD')
'''

'''
a = 100
b = 150
if a > b:
    print('A faster')
else:
    print('b faster')
'''

# Условный тернарный оп
'''x = 10 if x < 0 else -10
if x < 0: x = 10 else: x = -10
print(x)'''


# Модуль Math
'''math.pow(возведение, степень) возводит в степень'''
'''math.ceil() округляет до большего'''
'''math.floor() округляет до меньшего'''

# Практика


# 1
'''a = int(input('first: '))
b = int(input('sec: '))

if a>b:
    print('True')
else:
    print('False')'''

# 2

'''a = int(input('first: '))
b = int(input('sec: '))
c = int(input('third: '))

if a+b > c:
    print('true')
else:
    print(('false'))'''

# 3
'''a = int(input('first: '))

if a%2 == 0:
    print('True')
else:
    print('False')'''

# % - ostatok, // - tseloe

# 4
'''a = int(input('first: '))
if a%2 == 0:
    print('True')
else:
    print('False')'''

# 5
'''a = int(input('asd: '))

if a == 6 or a == 7:
    print('vihod')
else:
    print('budn')'''


# 6
'''a = int(input('asd: '))
if a>20:
    print(a/6)
else:
    print(a*6)'''

# 5 урок - не пришел, ппц
# while / for in

# 6 урок
# Функции. Модули, библиотеки и пакеты
# def name_func (arguments):
'''def add(x,y):
    return x+y'''

# нахождение факториала
'''def fact(x):
    result = 1
    while x > 0:
        result = result * x
        x = x - 1
    return result
print(fact(int(input())))'''

'''def max(a,b):
    if a>b:
        return a
    else:
        return b
print(max(3,5))
print(max(5,3))
print(max(int(input()), int(input())))'''

# Особые аргументы

# *args, **kwargs

'''def max(x,y, *args, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)
max(21,42,1,1,12,3,124, hi='hello', count=123)
'''

'''def max(*a):
    max1 = a[0]
    for i in a[1:]:
        if i>max1:
            max1=i
    return max1


print(max(4,9,6,5,22))'''

# глобальные и локальные переменные
'''x = 1

def func():
    print(x)


func()'''

'''x = 1

def func():
    x = 2
    print(x)

print(x)
func()'''

'''x = 1

def func():
    global x
    x = 2

func()
print(x)'''

# f' строка, как ${} в JS

'''name = 'Алекс'
age = 23

print(f"Меня зовут {name}, мне {age} лет")'''


# Практика
'''def my_range(x):
    result = []
    num = 0
    while num < x:
        result.append(num)
        num += 1
    return result

print(my_range(11))'''

# Рекурсия - это функция которая вызывает сама себя но не больше тысячи

'''def func(x):
    if x < 796:
        print(x)
        func(x + 1)

func(-200)'''

'''def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
for i in range(1,6):
    print('factorial {} = {}'.format(i,fact(i)))'''

# 7 урок
# Функции. Модули, библиотеки и пакеты
# lambda - анонимная функция маленькая функция для небольших действий
'''double = lambda x:x*2
print(double(5))'''
'''def func(x,y):
    res = x + y
    return res

a = func(5,3)
print(a)'''

'''def func(x,y):
    return x + y

a = func

b = lambda  x, y: x+y

print(a(2,5))
print(b(3,4))'''


'''def plus(x,y):
    return x + y
def minus(x,y):
    return x - y'''

'''def main():
    a = int(input('1: '))
    b = int(input('2: '))
    c = input('oper: ')
    if c == '+':
        plus = lambda x, y:x +y
        print(plus(a,b))
    elif c == '-':
        minus = lambda x, y:x -y
        print(minus(a,b))
    else:
        print('Err')
main()
'''

# filter - если функция возвращает True, то выводит только те значения которые соответствуют условиям
'''lst = [4,123,63,61,3,6,354,7,2346]
nlst = list(filter(lambda n:n%2==0,lst))
print(nlst)'''

# map - операция смещения чисел (выполняет действие)
'''lst = [4,123,63,61,3,6,354,7,2346]
nlst = list(map(lambda n:n*2,lst))
print(nlst)'''

# reduce - вызывается с помощью лямбда функции и  итерируемого объекта и возвращается новый уменьшенный результат (требуется import functools)
'''lst = [4,123,63,61,3,6,354,7,2346]'''
# берется пара иттерируемых объектов и выполняет действие (допустим 2 + 2 и 3 + 3, следом выполнит 4 + 6, так будет делать пока не закончится пары)
'''ld2 = functools.reduce((lambda x,y:x+y), lst) #
ld = functools.reduce((lambda x,y:x-y), lst) #
print(ld2)
print(ld)'''

'''lst = [1,2,3,4]
ld = functools.reduce((lambda x,y:x*y), lst)
print(ld)'''
'''1*2 = 2
3*4 = 12
2*12 = 24'''

# в функции ниже он берет числа от 1 до 10 ( range(1, 11) ) и умножает их на 10
'''tbl = [lambda x=x:x*10 for x in range(1, 11)]
for t in tbl:
    print(t())''' # выполняется функция t которая ссылается на tbl

# functools - это встроенная библиотека python в которой есть доп. предметы для функций (по типу reduce)
# они вызываются с помощью functools.название_тула
# в некоторых случаях необязательно всю библиотеку/модули импортировать. Можно импортировать отдельную функцию его
# например: from functools import reduce (в данном случае мы сможем пользоватся только functools.reduce)
# если функция из модуля совпадает с названием вашей переменной/функции и т.п, можно использовать as
# as дает пользовательское название функции. Например:
'''from functools import reduce
reduce = 123''' # тут происходит конфликт, но можно обойти это записав с as
'''from functools import reduce as reduce_one # название функции теперь не reduce, а reduce_one
reduce = 123''' #обычная переменная

# можно вытащить несколько функций из модуля вписав функции через запятую:
'''from functools import reduce, wraps''' # достанем и reduce и wraps


# dir и help
# dir выводит список всех функций в библиотеке
'''print(dir(math))'''
# help выводит как работает определенная функция
'''print(help(math.pi))''' # выведет документацию о функции pi

# модуль local
'''При форматировании чисел Пайтон по умолчанию использует англосаксонскую систему, при которой
разряды целого числа отделяются друг от друга запятыми, а дробная часть от целой отделяется точкой'''
# Это уже тонкости (не обязательно)


# NumPy - библиотека которая позволяет нам работать с массивами

# Collections - модуль который предоставляет спец. типы данных, на основе словарей, кортежей и т.д

# 8 урок
# Сортировка, поиск, регулярные выражения
# Функция sorted(). По умолчанию сортирует по возрастанию (список, словарь, кортеж)
# Сортировка слов осуществляется по ANCII (возвращает list)
'''
Синтаксис:
sorted(iterable, key=None, reverse=False)
'''
'''iterable - название строки, списка и т.д'''
'''key - ортировка будет выполнена по функции ключа (необязательный)'''
'''reverse - из возрастания делает убывание при значении True'''

# Метод list.sort() - сразу сортирует, мы не получим изначальное значение и работает только со списками
# Метод сортировки пузырьком
'''Берет первые два значения и сравнивает оставляет на месте то число которое меньше (работает пока не увидит перемен'''

'''import random

N = 50
a = []
for i in range(N):
    bun = random.randint(1,50)
    if bun not in a:
        a.append(bun)

print(a)
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j] > a[j + 1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)'''

# сортировка Shell sort
'''def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        print(alist)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        while position >= gap and alist[position-gap]>currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap
        alist[position] = currentvalue

alist = [5,4,6,3,7,2,8,1,9]
shellSort(alist)
print(alist)'''

# Быстрая сортировка (QuickSort)
'''import random
def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = []
        M = []
        R = []
'''

# Сортировка слияния (mergesirt)

# Поиск
# Линейный поиск это когда мы берем первое наше число и идем по порядку в поисках того самого элемента

# Бинарный поиск - может использоватся только в сортированных наборах данных
# Его алгоритм использует подход "Разделяй и властвуй"
# Если нечетное кол-во то начинает с середины
# Если не нашли, то продолжает поиск по левой части, тоже с середины

# Регулярные выражения
# \d любая цифра
# \D убирает все цифры
# \w заменяет цифры буквы и подчеркивания
# \W все кроме латиницы
# \s соответствует любому пробельному символу
# \S описывает любой не пробельный символ

# 9 урок
# Итераторы, контейнеры и перечисления
# Итератор - это объект который поддерживает функцию next() которая позволит перейти к следующему
# iter() and next()
# next() каждый раз возвращает следующий элемент из списка, а когда они заканчиваются, будет ошибкка

# генератор - функция которая будет работать только 1 раз (ключевое слово yield)
# Функции-генератор - функции которые возвращают значения и затем могут продолжить работу с того места, где они
# остановились в пред. раз
'''def gias(n):
    for x in range(n):
        yield x**3

for i in gias(5 + 1):
    print(i)'''


'''def genfib(n):
    a = 1
    b = 2
    for i in range(n):
        yield a
        a, b = b, a+b
def fibon(n):
    a = 1
    b = 1
    output = []
    for i in range(n):
        output.append(a)
        a,b = b, a+b
    return output
'''


'''for i in genfib(5):
    print(i)
print()
'''

# Выражение-генератор - выражение в круглых скобках которое выдаёт создает на каждой итерации новый элемент
'''a = [input() for i in range(int(input()))]
print(a)
b = [int(x) for x in a]
print(b)'''
# Сравнение
'''num = [1,2,3,4,5]
res = []
for x in num:
    if x > 3:
        y = x*x
        res.append(y)

print(res)'''

# Или

'''num = [1,2,3,4,5]

res_g = [x*x for x in num if x>3]
print(res_g)'''

# Декоратор
'''def decor(func):
    def warp():
        print('SASUKE')
        func()
        print('NARUTO')
    return warp

@decor
def popa():
    print('SAKURA')

popa()'''


# 10 урок
# Работа с датой и временем. Файлы и каталоги
# существуют два модуля: import datetime и import time
'''
date - объекты даты
datetime - объекты даты и времени
time - объекты времени
timedelta - этот атрибут покрывает интервалы и используется для определения прошлых или будущий событий
Tzinfo - этот атрибут отвечает за часовые пояса
'''
'''import datetime
a = datetime.datetime.now()     
b = a.time()
c = a - datetime.timedelta(hours=4)
print(c)'''
# import pytz - выбираете страну которой хотите использовать часовой пояс
# %Y - 2023
# %y 23

# Форматирование и перевод в строку
# получение дня от даты
'''date  = datetime.date.today()
print(date.today())'''

# Метод strftime
# %d - число
# %D - дата
# %m - месяц
# %M - минуты
# %y - последние 2 цифры года
# %c - день недели, месяц, число, время, год
# %x - дата
# %A - полное название дня недели
# %a - сокращенное название дня недели
# %S - секунды

'''import datetime
now = datetime.datetime.now().strftime('%D')
print(now)
'''

'''import datetime
now = '25.10.2023'
now_dt = datetime.datetime.strptime(now, '%d.%m.%Y')
print(now_dt)
'''

# Метки (штампы) timestamp (счёт секунд с 01.01.1970)
'''import datetime
now = datetime.datetime.now().timestamp()
print(now)
'''

# перевод из Гринвич в обычную дату
'''
import datetime
now = datetime.datetime.now().timestamp()

new = datetime.datetime.fromtimestamp(now)

print(new)
'''

# открыть файл в пайтон можно с помощью r - Read (только читаем файл), w - Write(помощью write можем только добавлять)
# e - Edit (только редактируем файл)
'''
1. Открытие файла с помощью метода open()
2. r - открытие файла для просмотра (по умолчанию)
3. w - открытие файла на запись, всё предыдущее удаляется
4. x - открытие на запись, если файла нет
5. a - открытие на дозапись, добавляется в конец
6. b - открытие в двоичном режиме (101010001010) бинарные файлы
7. t - открытие в текстовом режиме
8. + - открытие на чтение и запись
'''

'''myfile = open('путь до файла', 'w')

myfile.close()'''

# 11 урок
# Работа с файлами и каталогами
# Существует абсолютный путь и относительный
# Абсолютный путь это весь путь до файла в проводнике
# C:\Users\ПарвизС\Downloads\main.py
# Есть неполный путь (дериктория) (наша папка)
# open('main.py', 'w')
# После открытия файла, его нужно закрыть close()
# Практикка
'''a = open('hello.txt', 'r')''' #ошибка т.к файла не сущ
# a = open('123.txt', 'w') # создаёт файл и открывает его
# a.write('HIIIII') # записывает в файл то что мы вписали
# a.close() # закрывает файд
'''В Python, оператор try используется для определения блока кода, в котором может произойти исключение. 
Он позволяет выполнить определенный блок кода и проверить наличие исключений. Если исключение
возникает внутри блока try, 
управление передается соответствующему блоку except, где можно обработать исключение. 
Если исключение не обработано, оно может быть передано во 
внешний блок кода для обработки или вызвать прерывание программы.Блок try может также иметь необязательные блоки except,
 else и finally, которые предоставляют дополнительные возможности
  для обработки исключений и выполнения кода после блока try.'''

'''a = open('123.txt', 'r')
print(a.read())
a.close()

with open('123.txt', 'r') as b:
    print(b.read())'''

'''a = open('123.txt', 'a')
print(a.read())
a.close()'''

'''with open('123.txt', 'x') as b:
    b.write('\nsdadsa')
'''


'''import datetime
import time

for i in range(5):
    x = str(datetime.datetime.now())
    with open('123.txt', 'a') as file:
        file.write(x + '\n')
    time.sleep(.8)
with open('123.txt', 'r') as file:
    print(file.read())'''

# Модуль OS
'''Модуль os в Python предоставляет функции для взаимодействия с операционной системой, такие как управление 
файлами, директориями, окружением и процессами.'''
# import os
# os.mkdir(r"D:\folder") # создание новой папки
# os.mldirs(r"D:\folder\f\r\we\s") # создание новой цепочки папок
# os.remove(r"D:\forder") # удаляет все файлы в папке
# os.rmdir(r"D:\folder") # удаляет папку
# os.startfile(r"D:\test.exe") # запуск файлов .exe или .txt
# print(os.path.basename("D:/test.txt")) # возвращает название файла которого мы указали
# print(os.path.dirname("D:/folder/test.txt")) # возвращает путь к файлу (без его названия)
# os.rename() # меняет название одной директории
# os.renames() # меняет название целого пути

# csv файлы
# есть библиотека import csv
# reader_obj = csv.reader(file,delimiter=",")

# Работа с комплексными файлами


# 12 урок
# Git и Jira
'''Git - система контроля версий, позволяющая отслеживать изменения в коде; 
эффективно совместно работать над проектами и управлять версиями кода.'''
# github.com/Parviz0/PyPy

# Подготовка файлов для пуша
# git add -A
# git commit -m "first commit"
# git push

# Откатка
# git reset --hard



# 13 урок
# Обработка исключений. (ошибок, кроме синтаксических)
# Исключения (exception)

# Проверка исключений
'''try:
    инструкции
except[Тип_исключения]:
    инструкции'''


# Вместо исключения выводит то что мы ему прописали
'''try:
    number = int(input('Числ: '))
    print("Числ: ", number)
except:
    print('Неудачно')
print('Конки')'''

# Блок finally
# Выводится при любых объстаятельствах и выполняет то что написали внутри
'''try:
    number = int(input('Числ: '))
    print("Числ: ", number)
except:
    print('Неудачно')
finally:
    print('Работа почти завершена')
print('Конки')'''

# Вызов ошибки
'''raise AttributeError'''

# У каждого исключения есть собственный тип

# Основные типы исключений
# BaseException
# Exception
# ArithmeticError
# OverflowError
# https://imgur.com/a/C4ZTro4
# https://imgur.com/a/aDUrzcH

'''def func(x,y):
    try:
        return x + y
    except TypeError:
        return 'Ошибка'

print(func('123',123))'''



# print(func('123', 123))

'''
try:
    print('123' + 123)
except[TypeError]:
    print('Тип не верный')
'''

