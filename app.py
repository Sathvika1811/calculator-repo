from flask import Flask, render_template, request, jsonify
from calculator import Calculator  # Assuming Calculator is defined in calculator.py

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    calc = Calculator()
    if data['operation'] == 'add':
        result = calc.add(data['input1'], data['input2'])
    elif data['operation'] == 'subtract':
        result = calc.subtract(data['input1'], data['input2'])
    elif data['operation'] == 'multiply':
        result = calc.multiply(data['input1'], data['input2'])
    elif data['operation'] == 'divide':
        result = calc.divide(data['input1'], data['input2'])
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
