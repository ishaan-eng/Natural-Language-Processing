import joblib
from flask import Flask, render_template, request
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

def clean_text(sent):
    tokens1=word_tokenize(sent.lower())
    tokens2=[token for token in tokens1 if token.isalpha()]
    tokens3=[ps.stem(token) for token in tokens2 if token not in swords]
    return tokens3

classifier = joblib.load("classifier.model")
preprocessor = joblib.load("preprocessor.model")
ps = PorterStemmer()
swords = stopwords.words("english")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('frontend.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    sentence = str(request.form.get('sms_text'))
    prediction = classifier.predict(preprocessor.transform([sentence]))
    if prediction == 'ham':
        return render_template('prediction.html', value="not Spam")
    elif prediction == 'spam':
        return render_template('prediction.html', value="Spam")
    return None

if __name__ == '__main__':
    app.run(debug=True)