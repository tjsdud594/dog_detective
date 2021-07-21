from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['get'])
def get():
    return render_template('blank1.html')  

@app.route('/shop', methods=['get'])
def shop():
    return render_template('shop.html')  

@app.route('/sign', methods=['get'])
def sign():
    return render_template('join.html')  



if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")