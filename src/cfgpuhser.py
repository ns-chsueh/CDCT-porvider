from flask import Flask, jsonify

fakenfs = {}  

app = Flask(__name__)

@app.route("/file/<path:file_path>", methods=["GET"])
def read_file(file_path: str):
    if file_path in fakenfs:
        return fakenfs[file_path]
    return jsonify({"message": f"[Reason]: File /opt/ns/configshare/dp/{file_path} doesn't exist."}), 404

@app.route("/file/<path:file_path>", methods=["DELETE"])
def delete_file(file_path: str):
    if file_path in fakenfs:
        del fakenfs[file_path]
    return jsonify({"status": "OK"})


if __name__ == "__main__":
    app.run(debug=True, port=5001)
