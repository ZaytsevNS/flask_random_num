from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)
   

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    
    
@app.route('/get_result', methods=['GET', 'POST'])
def get_result():
    return render_template('result.html', name = request.form['user_name'], start_number = request.form['number_start'], finish_number = request.form['number_finish'], quantity_number = request.form['number_quantity'])

if __name__ == '__main__':
    app.run()
