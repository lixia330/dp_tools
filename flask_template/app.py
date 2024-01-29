from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/test_api", methods=["GET"])
def test_api():
    # check test input
    if "test" not in request.args:
        return jsonify({"status_code":400, "message":"There is no task upload!"})
    
    task = request.args.get("test")
    print(task)
    return jsonify({"status_code":200, "message":task})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)


