from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/message')
def landingPage():
    # return render_template("landingPage.html")

    return receive_message();

if __name__ == '__main__':
    app.run()
