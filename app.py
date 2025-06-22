from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            result = a + b
        except ValueError:
            result = "Entrée invalide"
    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = '''
<!doctype html>
<title>Calculator Web</title>
<h1>Calculatrice (Addition)</h1>
<form method="POST">
  Nombre 1: <input type="number" name="a" step="any"><br><br>
  Nombre 2: <input type="number" name="b" step="any"><br><br>
  <input type="submit" value="Additionner">
</form>
{% if result is not none %}
  <h2>Résultat : {{ result }}</h2>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def calcuator():
    result = None
    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            result = a + b
        except ValueError:
            result = "Entrée invalide"
    return render_template_string(HTML, result=result)

if __name__ == '__main__':
    app.run(debug=True)

