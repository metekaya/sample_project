from flask import Flask, request, jsonify

from utils import clamp, flatten, slugify
from stats import mean, median, mode


def greet(name: str) -> str:
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    return a + b


app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "ok", "version": "1.0"})


@app.post("/greet")
def greet_endpoint():
    data = request.get_json(silent=True) or {}
    name = data.get("name", "World")
    return jsonify({"message": greet(name)})


@app.post("/add")
def add_endpoint():
    data = request.get_json(silent=True) or {}
    a = data.get("a", 0)
    b = data.get("b", 0)
    return jsonify({"result": add(a, b)})


@app.post("/clamp")
def clamp_endpoint():
    data = request.get_json(silent=True) or {}
    value = data.get("value", 0)
    min_val = data.get("min", 0)
    max_val = data.get("max", 0)
    return jsonify({"result": clamp(value, min_val, max_val)})


@app.post("/flatten")
def flatten_endpoint():
    data = request.get_json(silent=True) or {}
    nested = data.get("nested", [])
    return jsonify({"result": flatten(nested)})


@app.post("/slugify")
def slugify_endpoint():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "")
    return jsonify({"result": slugify(text)})


@app.post("/mean")
def mean_endpoint():
    data = request.get_json(silent=True) or {}
    numbers = data.get("numbers", [])
    return jsonify({"result": mean(numbers)})


@app.post("/median")
def median_endpoint():
    data = request.get_json(silent=True) or {}
    numbers = data.get("numbers", [])
    return jsonify({"result": median(numbers)})


@app.post("/mode")
def mode_endpoint():
    data = request.get_json(silent=True) or {}
    numbers = data.get("numbers", [])
    return jsonify({"result": mode(numbers)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
