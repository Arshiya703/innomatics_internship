from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def arsr():
    return render_template('arsr.html')

if (__name__ == '__main__'):
    app.run(debug=True)
