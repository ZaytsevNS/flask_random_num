#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import sys
import os
import codecs
import random
import html

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
user_name = form.getfirst("user_name", "Вы не указали имя!")
user_name = html.escape(user_name)
number_start = int(form.getfirst("number_start"))
number_finish = int(form.getfirst("number_finish"))
quantity = int(form.getfirst("quantity"))
if quantity >= abs(number_start - number_finish):
    quantity = max(number_start, number_finish)
###
list_of_numbers = []
def get_random_num():
    global number_start
    global number_finish
    global quantity
    if number_start > number_finish:
        number_start, number_finish = number_finish, number_start
        numbers = random.sample(range(number_start, number_finish + 1), k=quantity)
        list_of_numbers.extend(numbers)
        numbers_in_line = ', '.join(map(str, numbers))
    else:
        numbers = random.sample(range(number_start, number_finish + 1), k=quantity)
        list_of_numbers.extend(numbers)
        numbers_in_line = ', '.join(map(str, numbers))
    return numbers_in_line

def get_abs_product():
    if form.getvalue('value_one'):
       num_prod = []
       result = 1
       for i in list_of_numbers:
           result *= abs(i)
       num_prod.append(result)
       num_prod = ''.join(map(str, num_prod))
    else:
       num_prod = "<br><span class='warn'><i>вы не выбрали данную опцию!</i></span>"
    return num_prod
 
def get_abs_min_number(): 
    if form.getvalue('value_two'):
       num_abs = []
       for i in list_of_numbers:
           num_abs.append(abs(i))
       num_min = min(num_abs)
    else:
       num_min = "<br><span class='warn'><i>вы не выбрали данную опцию!</i></span>"
    return num_min
   
def get_abs_sort():   
    if form.getvalue('value_three'):
       num_abs = []
       for i in list_of_numbers:
           num_abs.append(abs(i))
       num_sorted = sorted(num_abs)
       num_sorted = ', '.join(map(str, num_sorted))
    else:
       num_sorted = "<br><span class='warn'><i>вы не выбрали данную опцию!</i></span>"
    return num_sorted

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработанные данные</title>
            <link rel="stylesheet" href="/style/style_form.css">
            <link rel="shortcut icon" href="/img/favicon.ico" type="image/x-icon">
        </head>
        <body>
        <div id='answer'>""")
print("<p class='greet'>Привет, <span class='name'><strong><i>{}!</i></strong></span></p><br>".format(user_name.title()))
print("<p>Случайные {0} чисел из диапазона [{1},{2}]: <strong>{3}</strong></p>".format(quantity, number_start, number_finish, get_random_num()))
print("<p>Произведение чисел, взятых по абсолютной величине: <strong>{}</strong></p>".format(get_abs_product()))
print("<p>Минимальное число среди чисел, взятых по абсолютной величине: <strong>{}</strong></p>".format(get_abs_min_number()))
print("<p>Сортировка чисел, взятых по абсолютной величине: <strong>{}</strong></p><br>".format(get_abs_sort()))
print("""<table border='1'>
            <caption><strong>Некоторые параметры системы</strong></caption>
            <tr>
                <th>№ п/п</th>
                <th>Параметр</th>
                <th>Значение</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Операционная система</td>
                <td>{0}</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Описание версии ОС</td>
                <td>{1}</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Версия Python</td>
                <td>{2}</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Имя пользователя UNIX-системы</td>
                <td>{3}</td>
            </tr>
        </table>""".format(sys.platform, sys.version_info, sys.version, os.getlogin()))
print("<p><input type='submit' onclick='history.back();' value='Вернуться назад'/></p>")
print("""</div>
        </body>
        </html>""")
        