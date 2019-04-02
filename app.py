from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def landingPage():
    return ("helloo")

if __name__ == '__main__':
    app.run()
