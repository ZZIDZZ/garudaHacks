from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    render_template('./template/index.html')

if __name__=="__main__":
    app.run(debug=True)