from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    word = request.args.get('word')
    dictionary = {
        'cat': 'кошка',
        'dog': 'собака'
    }
    translation = dictionary.get(word, 'не найдено слово')
    requests.post()
    requests.get()
    return render_template("index.html", word=word, translation=translation)


if __name__ == "__main__":
    app.run(debug=True)
