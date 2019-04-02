from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/landingPage')
def landingPage():
    return render_template("landingPage.html")
# app.run(host='0.0.0.0', port=8002)
if __name__ == '__main__':
    app.run()
