from flask import Flask
app = Flask(__name__)


@app.route('/')
def landingPage():
    return render_template("landingPage.html")

if __name__ == '__main__':
    app.run()
