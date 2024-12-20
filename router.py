from flask import Flask, request, jsonify
from dynamic_routes import dynamic_route_with_semantics

app = Flask(__name__)

@app.route('/route', methods=['POST'])
def route_request():
    data = request.json
    request_text = data.get("text", "")
    metrics = data.get("metrics", {})
    model = dynamic_route_with_semantics(request_text, metrics)
    return jsonify({"routed_model": model})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
