from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Replace '0.0.0.0' with your IPv4 address if you prefer
    app.run(host='192.168.1.10', port=5000, debug=True)