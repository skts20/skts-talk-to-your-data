from flask import Flask

app = Flask(__name__)

from app.main import bp as main_bp
app.register_blueprint(main_bp)


@app.route('/health')
def health():
    return 'Hi, I am running'


if __name__ == '__main__':
    app.run(debug=True)