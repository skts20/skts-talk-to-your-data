from flask import Blueprint
bp = Blueprint('llama', __name__)
from app.llama import routes