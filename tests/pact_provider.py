from flask import jsonify, request

from src.cfgpuhser import app, fakenfs


@app.route("/_pact/provider_states", methods=["POST"])
def provider_states():
    if "file not found" in request.json["state"]:
        setup_file_not_exist()
    else:
        setup_file_content()
    return jsonify({"result": request.json["state"]})


def setup_file_content():
    fakenfs["opt/ns/tenant/1113/watchlist2.json"] = "test2225"

def setup_file_not_exist():
    file_path = "opt/ns/tenant/1113/watchlist2.json"
    if file_path in fakenfs:
        del fakenfs[file_path]


if __name__ == "__main__":
    app.run(debug=True, port=5001)
