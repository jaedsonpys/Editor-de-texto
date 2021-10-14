from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World from flask!'

@app.route('/about')
def about():
    return 'This is a about page, welcome!'

if __name__ == '__main__':
    app.run(debug=True, port=5500)


# Alterção
