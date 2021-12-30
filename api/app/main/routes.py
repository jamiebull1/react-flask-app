from flask import jsonify

from api.app.main import bp


@bp.route("/ping")
def ping():
    return jsonify({"ping": "PONG"})
