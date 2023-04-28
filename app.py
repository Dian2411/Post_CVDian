from flask import Flask, render_template
from flask_ngrok import run_with_ngrok

app = Flask(__name__, static_folder='static')


@app.route("/")
def halamanCV():
    return render_template("CV_Dian NurBudi Leksono.html")


if __name__ == "__main__":
    run_with_ngrok(app)
    app.run()