from flask import jsonify, request

from src.cfgpuhser import app, fakenfs


@app.route("/_pact/provider_states", methods=["POST"])
def provider_states():
    mapping = {
        "Cfgpusher returns file content": setup_file_content,
        "Cfgpusher delete file": setup_file_content,
        "Cfgpusher returns file not found": setup_file_not_exist,
    }
    mapping[request.json["state"]]()
    return jsonify({"result": request.json["state"]})


def setup_file_content():
    fakenfs["opt/ns/tenant/1113/watchlist2.json"] = "test2225"

def setup_file_not_exist():
    file_path = "opt/ns/tenant/1113/watchlist2.json"
    if file_path in fakenfs:
        del fakenfs[file_path]


if __name__ == "__main__":
    app.run(debug=True, port=5001)
