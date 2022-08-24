from flask import Flask

app=Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome To My Website. Hope You Are Doing Well. See You Soon'

@app.route('/members')
def members():
    return 'All Right Then.. Stay Tuned..'


if __name__=='__main__':
    app.run(debug=True)