from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    @app.route('/health')
    def test_page():
        return 'Hi, I am running'
    return app
