from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():  # put application's code here
    return 'Welcome to FAPI!'


if __name__ == '__main__':
    app.run()
