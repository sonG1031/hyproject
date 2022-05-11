from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix="/")

@bp.route("/hello")
def hello_hy():
    return "Hello Hanyang!"

@bp.route("/")
def index():
    return "Hanyang index"