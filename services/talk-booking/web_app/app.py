from flask import Flask

app = Flask(__name__)


@app.route("/health-check/")
def health_check():
    return "OK"


if __name__ == "__main__":
    app.run(debug=True)
