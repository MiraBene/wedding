from flask import Flask
from flask import redirect, render_template, request, url_for

csv_path = '/data/guests.csv'

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        'index.html',
        js_path=url_for('static', filename='js/main.js'),
        style_path=url_for('static', filename='css/main.css')
    )


@app.route("/register", methods=['POST'])
def register():
    data = request.form

    with open(csv_path, 'a') as f:
        f.write(f"{data['email']},{data['descr']}\n")

    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
