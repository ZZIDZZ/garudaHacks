from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hello World, by Flask Web Server"

if __name__=="__main__":
    app.run()