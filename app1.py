#Building Dynamic URL
#Variable Rules & URL Building


from flask import Flask, redirect, url_for

app=Flask(__name__)


@app.route('/')
def welcome1():
    return 'Welcome Everyone'

@app.route('/success/<int:score>')
def success(score):
    return 'The person has passed exaam with Marks ' + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'The person has failed exam with Marks ' + str(score) 

@app.route('/result/<int:marks>')
def result(marks):
    result=""
    if marks > 50:
        result='success'
    else:
        result='fail'
    return redirect(url_for(result,score=marks))

if __name__=='__main__':
    app.run(debug=True)
