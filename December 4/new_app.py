from flask import Flask, render_template, request, redirect, url_for, session, flash
app=Flask(__name__)

@app.route('/hello/<name>')
def hello_world(name):
    return 'HAPPY BIRTHDAY %s !!!!' %name


if __name__=='__main__':
    app.run(debug=True)