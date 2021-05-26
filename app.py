from flask import Flask, redirect, url_for, request, render_template
from markupsafe import Markup
import random
import sys
import os


app = Flask(__name__)
   

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    
    
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    # global start
    # global finish
    # global quantity
    # user = request.form['user_name']
    # start = request.form['number_start']
    # finish = request.form['number_finish']
    # quantity = request.form['number_quantity']
    # error = Markup('<br>вы не выбрали данную опцию!')
    # sys_platform = sys.platform
    # sys_description = sys.version_info
    # python_version = sys.version
    # username_unix = os.getlogin()
        
    # list_of_numbers = []
    # def get_random():
    #     global start
    #     global finish
    #     global quantity
    #     if int(start) == int(finish):
    #         numbers = start
    #     else:
    #         if int(start) > int(finish) and int(quantity) > abs(int(start) - int(finish)):
    #             start, finish = finish, start
    #             quantity = abs(int(start) - int(finish)) + 1
    #             list_of_random_numbers = random.sample(range(int(start), int(finish) + 1), k=int(quantity))
    #             list_of_numbers.extend(list_of_random_numbers)
    #             numbers = ', '.join(map(str, list_of_random_numbers))
    #         elif int(quantity) > abs(int(start) - int(finish)):
    #             quantity = abs(int(start) - int(finish)) + 1
    #             list_of_random_numbers = random.sample(range(int(start), int(finish) + 1), k=int(quantity))
    #             list_of_numbers.extend(list_of_random_numbers)
    #             numbers = ', '.join(map(str, list_of_random_numbers))
    #         else:
    #             list_of_random_numbers = random.sample(range(int(start), int(finish) + 1), k=int(quantity))
    #             list_of_numbers.extend(list_of_random_numbers)
    #             numbers = ', '.join(map(str, list_of_random_numbers))
    #     return numbers
        
    # def get_abs_product():
    #     if request.form.get('value_one'):
    #         num_product = []
    #         result = 1
    #         for i in list_of_numbers:
    #             result *= abs(i)
    #         num_product.append(result)
    #         num_product = ''.join(map(str, num_product))
    #     else:
    #         return error
    #     return num_product
        
    # def get_abs_min_number(): 
    #     if request.form.get('value_two'):
    #         num_abs = []
    #         for i in list_of_numbers:
    #             num_abs.append(abs(i))
    #         num_min = min(num_abs)
    #     else:
    #         return error
    #     return num_min

    # def get_abs_sort():   
    #     if request.form.get('value_three'):
    #         num_abs = []
    #         for i in list_of_numbers:
    #             num_abs.append(abs(i))
    #             num_sorted = sorted(num_abs)
    #         num_sorted = ', '.join(map(str, num_sorted))
    #     else:
    #         return error
    #     return num_sorted
            
        #def get_sys_info():
            #list_sys_info = []
            #list_sys_info.append(sys.platform)
            #list_sys_info.append(sys.version_info)
            #list_sys_info.append(sys.version)
            #list_sys_info.append(os.getlogin())
            #return list_sys_info
            
            
    return render_template('form.html', name = request.form['user_name'], start_number = request.form['number_start'], finish_number = request.form['number_finish'], quantity_number = request.form['number_quantity'])




if __name__ == '__main__':
    app.run()
