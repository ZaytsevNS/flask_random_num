from flask import Flask, redirect, url_for, request, render_template, Markup
import random
import sys
import os


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/get_result', methods=['GET', 'POST'])
def get_result():
    global number_start
    global number_finish
    global number_quantity
    user_name = request.form['user_name']
    number_start = int(request.form['number_start'])
    number_finish = int(request.form['number_finish'])
    number_quantity = int(request.form['number_quantity'])
    error = Markup('<br>вы не выбрали данную опцию!')
    global product
    product = 1
    min_num = 0
    sorted_list = []
    if number_start > number_finish:
        number_start, number_finish = number_finish, number_start
    if number_quantity >= abs(number_start - number_finish):
        number_quantity = max(number_start, number_finish)-1
    
    list_numbers = []
    #def get_random():
        #global number_start
        #global number_finish
        #global number_quantity
    numbers = random.sample(range(number_start, number_finish + 1), k=number_quantity)
    list_numbers.extend(numbers)
    numbers_in_line = ', '.join(map(str, numbers))
    #return numbers_in_line

    def get_product():
        global product
        if request.form.get('value_one'):
            for i in list_numbers:
                product *= abs(i)
            return product
        else:
            product = error
        return product
    
    if request.form.get('value_two'):
        min_num = min([abs(i) for i in numbers])
    else:
        min_num = error
    if request.form.get('value_three'):
        sorted_list.extend(sorted([abs(i) for i in numbers]))
        sorted_list = ', '.join(map(str, sorted_list))
    else:
        sorted_list = error
    return render_template('result.html', name=user_name, start=number_start, finish=number_finish, quantity=number_quantity, random_num=numbers_in_line, product_number=get_product(), min_number=min_num, sorted_number=sorted_list)


if __name__ == '__main__':
    app.run(debug=True)
