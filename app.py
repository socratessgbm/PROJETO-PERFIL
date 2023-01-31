from flask import Flask, render_template, redirect

app = Flask(__name__)

# criar uma rota
@app.route('/')
def index():
    # procura na pasta templates o arquivo index
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
