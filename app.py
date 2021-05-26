from flask import Flask, redirect, url_for, request, render_template
from markupsafe import Markup
import random
import sys
import os

app = Flask(__name__)
   
@app.route('/success/<name>&<start_number>&<finish_number>&<quantity_number>&<random_number>&<product_number>&<min_number>&<sorted_number>&<info_platform>&<info_sys_description>&<info_python_version>&<info_username_unix>')
def success(name, start_number, finish_number, quantity_number, random_number, product_number, min_number, sorted_number, info_platform, info_sys_description, info_python_version, info_username_unix):
    return render_template('success_form.html', name = name, start_number = start_number, finish_number = finish_number, quantity_number = quantity_number, random_number = random_number, product_number = product_number, min_number = min_number, \
    sorted_number = sorted_number, info_platform = info_platform, info_sys_description = info_sys_description, info_python_version = info_python_version, info_username_unix = info_username_unix)


@app.route('/main_form', methods = ['GET', 'POST'])
def main_form():
    if request.method == 'POST':
        #user = request.form.get('user_name')
        user = request.form['user_name']
        global start
        global finish
        global quantity
        #start = request.form.get('number_start')
        #finish = request.form.get('number_finish')
        #quantity = request.form.get('number_quantity')
        start = request.form['number_start']
        finish = request.form['number_finish']
        quantity = request.form['number_quantity']
        error = Markup('<br>вы не выбрали данную опцию!')
        sys_platform = sys.platform
        sys_description = sys.version_info
        python_version = sys.version
        username_unix = os.getlogin()
        
        list_of_numbers = []
        def get_random():
            global start
            global finish
            global quantity
            if int(start) == int(finish):
                numbers = start
            else:
                if int(start) > int(finish) and int(quantity) > abs(int(start) - int(finish)):
                    start, finish = finish, start
                    quantity = abs(int(start) - int(finish)) + 1
                    list_of_random_numbers = random.sample(range(int(start), int(finish) + 1), k=int(quantity))
                    list_of_numbers.extend(list_of_random_numbers)
                    numbers = ', '.join(map(str, list_of_random_numbers))
                elif int(quantity) > abs(int(start) - int(finish)):
                    quantity = abs(int(start) - int(finish)) + 1
                    list_of_random_numbers = random.sample(range(int(start), int(finish) + 1), k=int(quantity))
                    list_of_numbers.extend(list_of_random_numbers)
                    numbers = ', '.join(map(str, list_of_random_numbers))
                else:
                    list_of_random_numbers = random.sample(range(int(start), int(finish) + 1), k=int(quantity))
                    list_of_numbers.extend(list_of_random_numbers)
                    numbers = ', '.join(map(str, list_of_random_numbers))
            return numbers
        
        def get_abs_product():
            if request.form.get('value_one'):
                num_product = []
                result = 1
                for i in list_of_numbers:
                    result *= abs(i)
                num_product.append(result)
                num_product = ''.join(map(str, num_product))
            else:
                return error
            return num_product
        
        def get_abs_min_number(): 
            if request.form.get('value_two'):
                num_abs = []
                for i in list_of_numbers:
                    num_abs.append(abs(i))
                num_min = min(num_abs)
            else:
                return error
            return num_min

        def get_abs_sort():   
            if request.form.get('value_three'):
                num_abs = []
                for i in list_of_numbers:
                    num_abs.append(abs(i))
                    num_sorted = sorted(num_abs)
                num_sorted = ', '.join(map(str, num_sorted))
            else:
                return error
            return num_sorted
            
        #def get_sys_info():
            #list_sys_info = []
            #list_sys_info.append(sys.platform)
            #list_sys_info.append(sys.version_info)
            #list_sys_info.append(sys.version)
            #list_sys_info.append(os.getlogin())
            #return list_sys_info
            
            
    return redirect(url_for('success', name = user, start_number = start, finish_number = finish, quantity_number = quantity, random_number = get_random(), product_number = get_abs_product(),\
    min_number = get_abs_min_number(), sorted_number = get_abs_sort(), info_platform = sys_platform, info_sys_description = sys_description, info_python_version = python_version, info_username_unix = username_unix))
    #else:
        #user = request.args.get('user_name')
        #return redirect(url_for('success', name = user))

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run()
