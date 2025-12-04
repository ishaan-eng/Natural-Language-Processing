from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)


@app.route('/admin')
def hello_admin():
    return 'Hello Administrator'

@app.route('/home/<user>')
def hello_home(user):
    return render_template('Welcome.html', name=user)

@app.route('/guest/<guest_name>')
def hello_guest(guest_name):
    return f'Hello {guest_name} as guest'


@app.route('/user/<username>')
def hello_user(username):
    if username == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest_name=username))


if __name__ == '__main__':
    app.run(debug=True)
