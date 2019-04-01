from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/landingPage", methods=['GET'])
def landingPage():
    return render_template("landingPage.html")
# app.run(host='0.0.0.0', port=8002)
app.run(host='0.0.0.0', port=8002)
