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
    info_sys_platform = sys.platform
    if number_start > number_finish:
        number_start, number_finish = number_finish, number_start
    if number_quantity >= abs(number_start - number_finish):
        number_quantity = abs(number_start - number_finish)
    
    list_numbers = []
    def get_random():
        numbers = random.sample(range(number_start, number_finish + 1), k=number_quantity)
        list_numbers.extend(numbers)
        numbers_in_line = ', '.join(map(str, numbers))
        return numbers_in_line

    def get_product():
        product = 1
        if request.form.get('value_one'):
            for i in list_numbers:
                product *= abs(i)
            return product
        else:
            return error
        
    def get_abs_minimum():
        if request.form.get('value_two'):
            min_num = min([abs(i) for i in list_numbers])
            return min_num
        else:
            return error
    
    def get_sorted_numbers():
        sorted_list = []
        if request.form.get('value_three'):
            sorted_list.extend(sorted([abs(i) for i in list_numbers]))
            sorted_list = ', '.join(map(str, sorted_list))
            return sorted_list
        else:
            return error
    
    return render_template('result.html', name=user_name, start=number_start, finish=number_finish, quantity=number_quantity, random_num=get_random(), product_number=get_product(), min_number=get_abs_minimum(), sorted_number=get_sorted_numbers(), info_platform = info_sys_platform)


if __name__ == '__main__':
    app.run(debug=True)
