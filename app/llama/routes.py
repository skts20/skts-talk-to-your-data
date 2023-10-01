from app.llama import bp
from app.llama.llama_init import init


@bp.route('/llama/init', methods=['POST'])
def init_llama():
    init()
