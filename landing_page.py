from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/landingPage')
def landingPage():
    return "landing page"
# app.run(host='0.0.0.0', port=8002)
if __name__ == '__main__':
    app.run()
