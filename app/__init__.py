from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
