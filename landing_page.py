from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/landingPage')
def landingPage():
    return render_template("landingPage.html")


print __name__;
if __name__ == '__main__':
    app.run()
