from flask import Flask, jsonify

app = Flask(__name__)

from app.main import bp as main_bp
app.register_blueprint(main_bp)

from app.llama import bp as llama_bp
app.register_blueprint(llama_bp)


@app.route('/health')
def health():
    return jsonify("Hi, I am running!"), 200


if __name__ == '__main__':
    app.run(debug=True)
