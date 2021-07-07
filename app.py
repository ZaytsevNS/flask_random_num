from flask import Flask, request, render_template, Markup
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
    
    if number_start > number_finish:
        number_start, number_finish = number_finish, number_start
    if number_quantity >= abs(number_start - number_finish):
        number_quantity = abs(number_start - number_finish)
    
    list_numbers = []
    def get_random() -> str:
        """ This function returns random numbers """
        if request.form.get('remove_repeats'):
            numbers = random.sample(range(number_start, number_finish + 1), k=number_quantity)
            list_numbers.extend(numbers)
            numbers_in_line = ', '.join(map(str, numbers))
            return numbers_in_line
        else:
            numbers = [random.randint(number_start, number_finish + 1) for i in range(number_quantity)]
            list_numbers.extend(numbers)
            numbers_in_line = ', '.join(map(str, numbers))
            return numbers_in_line
            
    def get_product() -> int or str:
        """ This function returns product of random numbers or error """
        product = 1
        if request.form.get('get_product'):
            for i in list_numbers:
                product *= abs(i)
            return product
        else:
            return error
        
    def get_abs_max_and_min() -> str:
        """ This function returns max and min number from random numbers or error """
        if request.form.get('get_abs_max_and_min'):
            min_num, max_num = min([abs(i) for i in list_numbers]), max([abs(i) for i in list_numbers])
            return f'min = {min_num}, max = {max_num}'
        else:
            return error
    
    def get_sorted_numbers() -> str:
        """ This function returns sorted random numbers in absolut value or error """
        sorted_list = []
        if request.form.get('get_sorted_numbers'):
            sorted_list.extend(sorted([abs(i) for i in list_numbers]))
            sorted_list = ', '.join(map(str, sorted_list))
            return sorted_list
        else:
            return error
    
    return render_template('result.html', name=user_name, start=number_start, finish=number_finish, quantity=number_quantity, random_num=get_random(), product_number=get_product(), min_and_max_number=get_abs_max_and_min(), sorted_number=get_sorted_numbers(), info_platform = sys.platform, info_sys_description = sys.version_info, info_python_version = sys.version, info_username_unix = os.environ.get('USERNAME'))


if __name__ == '__main__':
    app.run(port=8000, debug=True)