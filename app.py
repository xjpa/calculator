from flask import Flask, request, render_template_string
import ctypes

app = Flask(__name__)
lib = ctypes.CDLL('./libcalculator_operations.so')

# Setting restype for divide function to avoid integer division
lib.divide.restype = ctypes.c_float

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        operation = request.form['operation']
        a = int(request.form['a'])
        b = int(request.form['b'])

        if operation == 'add':
            result = lib.add(a, b)
        elif operation == 'subtract':
            result = lib.subtract(a, b)
        elif operation == 'multiply':
            result = lib.multiply(a, b)
        elif operation == 'divide':
            result = lib.divide(a, b)
        else:
            result = 'Invalid operation'

        return render_template_string(FORM_TEMPLATE, result=result, a=a, b=b, operation=operation)

    return render_template_string(FORM_TEMPLATE, result="", a=0, b=0, operation='add')

FORM_TEMPLATE = """
<!doctype html>
<html>
<head><title>Calculator</title></head>
<body>
  <h2>Calculator</h2>
  <form method="post">
    <label for="a">A:</label>
    <input type="number" id="a" name="a" value="{{ a }}"><br><br>
    <label for="b">B:</label>
    <input type="number" id="b" name="b" value="{{ b }}"><br><br>
    <label for="operation">Operation:</label>
    <select id="operation" name="operation">
        <option value="add" {% if operation == 'add' %}selected{% endif %}>Add</option>
        <option value="subtract" {% if operation == 'subtract' %}selected{% endif %}>Subtract</option>
        <option value="multiply" {% if operation == 'multiply' %}selected{% endif %}>Multiply</option>
        <option value="divide" {% if operation == 'divide' %}selected{% endif %}>Divide</option>
    </select><br><br>
    <input type="submit" value="Calculate">
  </form>
  {% if result != "" %}
    <h3>Result: {{ result }}</h3>
  {% endif %}
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
