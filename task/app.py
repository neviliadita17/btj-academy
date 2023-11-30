from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/about')
def about():
    return 'This is the About page.'

@app.route('/contact')
def contact():
    return 'This is the Contact page.'

if __name__ == '__main__':
    # Ganti port menjadi 5001
    app.run(debug=True, host='0.0.0.0', port=5001)
    