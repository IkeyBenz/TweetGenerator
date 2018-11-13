from flask import Flask
import dictionaryWords

app = Flask(__name__)

@app.route('/')
def hello_world():
    return dictionaryWords.main()

