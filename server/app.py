# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_cors import CORS

from utils.query_manager import QueryManager
from utils.logger import get_logger


def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")

    CORS(app)

    # get logger
    logger = get_logger(__name__)

    @app.errorhandler(Exception)
    def handle_error(e):
        logger.exception(f"Unhandled exception: {e}")
        return jsonify(error=str(e)), 500

    @app.route("/api/airports", methods=["GET"])
    def get_airports():
        us_state = request.args["us_state"]
        runway = int(request.args["runway"])

        qm = QueryManager.from_default_db()
        airports = qm.get_airports_by_us_state_and_runway(us_state, runway)

        return jsonify({"airports": airports.to_dict(orient="records")})

    return app
