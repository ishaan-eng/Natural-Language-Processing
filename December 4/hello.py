from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)


# print(app.template_folder)

# @app.route('/')
# def index():
#     render_template("login.html")

@app.route('/admin')
def hello_admin():
    return 'Hello Administrator'


@app.route('/guest/<user>')
def hello_user(user):
    return f'Hello {user} as guest'


@app.route('/login', methods=['get','post'])
def login():
    user = request.form['username']
    # user = request.args.get('username')

    if user == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_user', user=user))


if __name__ == '__main__':
    app.run(debug=True)
