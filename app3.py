# {%      %} - Conditions, For loops
# {{      }} - Expressions to print output
# {#      #} - Comments 
# Integrating HTML & CSS files
# Using conditional statements in html & integrating with .py file

from tkinter import scrolledtext
from flask import Flask, redirect, url_for, render_template, request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=''
    if score > 50:
        res='Pass'
    else:
        res='Fail'
    exp={'Score':score, 'Result': res }
    return render_template('result.html', result = exp)

@app.route('/submit', methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4    
    return redirect(url_for('success', score=total_score))


if __name__=='__main__':
    app.run(debug=True)
