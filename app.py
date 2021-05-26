from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)
   

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    
    
@app.route('/get_result', methods=['GET', 'POST'])
def get_result():
   user_name = request.form['user_name']
   number_start = request.form['number_start']
   number_finish = request.form['number_finish']
   number_quantity = request.form['number_quantity'])
   return render_template('result.html', user_name = user_name, number_start = number_start, number_finish = number_finish, number_quantity = number_quantity)

if __name__ == '__main__':
    app.run()
