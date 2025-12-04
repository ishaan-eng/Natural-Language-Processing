from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST', 'GET'])
def get_result():
    name = request.form.get('name')
    phy = int(request.form.get('PHY'))
    chem = int(request.form.get('CHEM'))
    bio = int(request.form.get('BIO'))
    per = (phy + chem + bio) / 3
    return render_template('result.html', value=per)


if __name__ == '__main__':
    app.run(debug=True)
