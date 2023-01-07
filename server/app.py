from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from server.services.query_manager import QueryManager

app = Flask(__name__,
            static_folder="static",
            template_folder="templates")

CORS(app)


@app.route("/", methods=["GET"])
def client():
    return render_template("index.html")


@app.route("/api/airports", methods=["GET"])
def get_airports():
    us_state = request.args["us_state"]
    runway = int(request.args["runway"])

    qm = QueryManager.from_default_db()
    airports = qm.get_airports_by_us_state_and_runway(us_state, runway)

    return jsonify({"airports": airports.to_dict(orient='records')})


app.run(port=8000, debug=True)
