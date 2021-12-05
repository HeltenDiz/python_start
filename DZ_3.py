# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def func_delete(*args):
    a = int(input("Введите значения числа a "))
    b = int(input("Введите значения числа b "))
    if b != 0:
        division = a / b
    else:
        print('Деление на ноль запрещено')
    print(f'Результат деления = {division}')


# func_delete()

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# name = input('enter name')
# surname = input('enter surname')
# year = input('enter year')
# city = input('enter city')
# email = input('enter email')
# telephone = input('input telephone')


def my_func(name, surname, year, city, email, telephone):
    return f'Имя: {name}, Фамилия: {surname}, Год Рождения: {year}, Город проживания: {city}, Email: {email}, телефон: {telephone}'


#print(my_func(name, surname, year, city, email, telephone))


# Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.
def my_func_3(a, b, c):
    if a >= c and b >= c:
        return a + b
    elif a > b and a < c:
        return a + c
    else:
        return b + c


#print(f'Result - {my_func_3(a=int(input("enter first argument ")), b=int(input("enter second argument ")), c=int(input("enter third argument ")))}')


# Программа принимает действительное положительное число x
# и целое отрицательное число y. Необходимо выполнить возведение
# числа x в степень y. Задание необходимо реализовать в виде функции
# my_func(x, y). При решении задания необходимо обойтись без встроенной
# функции возведения числа в степень.
def func_degree(x, y):
    result = x**y
    print(f'Результат возведения в степень = {result}')


def func_degree_2(x, y):
    s = 1
    for i in range(y):
        s = s * x
    print(f'Результат возведения в степень = {s}')


#func_degree_2(x=int(input("enter first argument ")), y=int(input("enter second argument ")))


# Программа запрашивает у пользователя строку чисел, разделенных
#  пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и
# снова нажать Enter. Сумма вновь введенных чисел будет добавляться
# к уже подсчитанной сумме. Но если вместо числа вводится специальный
# символ, выполнение программы завершается. Если специальный символ
# введен после нескольких чисел, то вначале нужно добавить сумму этих
# чисел к полученной ранее сумме и после этого завершить программу.
def my_sum():
    sum_res = 0
    while True:
        number = input('Input numbers or Q for quit - ').split()

        for el in number:
            if el == 'q' or el == 'Q':
                return f'Final sum is {sum_res}'
            else:
                sum_res = sum_res + int(el)
        print(f'Current sum is {sum_res}')


#print(my_sum())


# Реализовать функцию int_func(), принимающую слово из маленьких
# латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать
# строка из слов, разделенных пробелом. Каждое слово состоит
# из латинских букв в нижнем регистре. Сделать вывод исходной
# строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def func_title (*args):
    word = input("Input words ")
    return word.title()


print(func_title())
