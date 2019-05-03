from flask import Flask
app=Flask(__name__)
from flask import make_response 
from flask import redirect 
 
@app.route('/redire')
def redi():     
    return redirect('https://sprinter1999.github.io/')

@app.route('/cookie')
def cookie():     
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42') 
    return response

@app.route('/')
def index():
    return '<h1>Hello boy!</h1>',200

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s!</h1>' % name,200

@app.route('/badApple')
def bad():
    return '<h1>Bad Gate Request!</h1>',400
if __name__=='__main__':
    app.run(debug=True)