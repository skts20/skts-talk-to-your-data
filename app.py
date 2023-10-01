from flask import Flask, jsonify

app = Flask(__name__)

from app.main import bp as main_bp
app.register_blueprint(main_bp)

# init model and tokenizer
from app.llama.llama_init import *

@app.route('/health')
def health():
    return jsonify("Hi, I am running!"), 200


if __name__ == '__main__':
    app.run(debug=True)
