from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/message')
def landingPage():
    return receive_large_interactive_payload();

if __name__ == '__main__':
    app.run()
