from flask import Flask
from flask import render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        'index.html',
        js=url_for('static', filename='js.css'),
        style_path=url_for('static', filename='main.css')
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0')
