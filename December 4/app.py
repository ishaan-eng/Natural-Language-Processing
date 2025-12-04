from flask import Flask, render_template, request, redirect, url_for, session, flash
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'HAPPY BIRTHDAY ATHARVA !!!!'

@app.route('/index')
def hello_index():
    return 'Welcome to index Page'

if __name__=='__main__':
    app.run(debug=True)