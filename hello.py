from flask import Flask
from sklearn.model_selection import train_test_split
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!,fuck you ten times i will rule this things my way , i do not care "

if __name__ == '__main__':
    app.run()
    