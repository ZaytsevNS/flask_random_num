## FLASK web application

This web app works with random numbers and you can:
1) generate some random numbers from N to M;
2) choose the number of such numbers;
3) find the product of the numbers taken by absolute value;
4) find the minimum number among the numbers taken by absolute value;
5) perform sorting of numbers taken by absolute value.

## How to run this app?
1) Create a project directory.
2) Change into the project directory.
3) Create virtual environment: 
  ```bash
  pip install virtualenv
  ```
  ```bash
  virtualenv venv --python=<YOUR_PYTHON_VERSION>
  ``` 
  For example: 
  ```bash 
  virtualenv venv --python=3.7.6
  ```
4) Activate virtual environment: 
  ```bash 
  venv/Scripts/activate
  ```
5) Install python packages into a virtual environment:
  ```bash 
  pip install -r requirements.txt
  ```
6) Go to your web browser and type in the search field: **http://localhost:8000/**
7) Enter your name, select the required numerical values and options and click to button 'Показать результаты'.
If you want to clear the form click to button 'Очистить форму'.
8) When you’re done working on a project deactivate virtual environment: 
  ```bash 
  venv/Scripts/deactivate
  ```
  
[Run this web app on heroku](https://rndnum.herokuapp.com/)

**Home page with filled fields**:
![StartPage](https://github.com/ZaytsevNS/python_practice/blob/main/work_with_rand_num/start_page.jpg)

**Page when you click to button 'Показать результаты'**
![StartPage](https://github.com/ZaytsevNS/python_practice/blob/main/work_with_rand_num/finish_page.jpg)
