from flask import Flask, request, jsonify

from utils import clamp, flatten, slugify
from stats import mean, median, mode
from validators import (
    validate_number,
    validate_number_list,
    validate_string,
    validate_clamp_args,
    validate_nested_list,
)
from errors import bad_request, not_implemented_error


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
    try:
        name = validate_string(name, "name")
    except ValueError as e:
        return bad_request(str(e))
    return jsonify({"message": greet(name)})


@app.post("/add")
def add_endpoint():
    data = request.get_json(silent=True) or {}
    try:
        a = validate_number(data.get("a", 0), "a")
        b = validate_number(data.get("b", 0), "b")
    except ValueError as e:
        return bad_request(str(e))
    return jsonify({"result": add(a, b)})


@app.post("/clamp")
def clamp_endpoint():
    data = request.get_json(silent=True) or {}
    try:
        value, min_val, max_val = validate_clamp_args(
            data.get("value", 0),
            data.get("min", 0),
            data.get("max", 0),
        )
    except ValueError as e:
        return bad_request(str(e))
    return jsonify({"result": clamp(value, min_val, max_val)})


@app.post("/flatten")
def flatten_endpoint():
    data = request.get_json(silent=True) or {}
    try:
        nested = validate_nested_list(data.get("nested", []), "nested")
    except ValueError as e:
        return bad_request(str(e))
    return jsonify({"result": flatten(nested)})


@app.post("/slugify")
def slugify_endpoint():
    data = request.get_json(silent=True) or {}
    try:
        text = validate_string(data.get("text", ""), "text")
    except ValueError as e:
        return bad_request(str(e))
    return jsonify({"result": slugify(text)})


@app.post("/mean")
def mean_endpoint():
    data = request.get_json(silent=True) or {}
    try:
        numbers = validate_number_list(data.get("numbers", []), "numbers")
    except ValueError as e:
        return bad_request(str(e))
    return jsonify({"result": mean(numbers)})


@app.post("/median")
def median_endpoint():
    data = request.get_json(silent=True) or {}
    try:
        numbers = validate_number_list(data.get("numbers", []), "numbers")
        result = median(numbers)
    except ValueError as e:
        return bad_request(str(e))
    except NotImplementedError:
        return not_implemented_error("median")
    return jsonify({"result": result})


@app.post("/mode")
def mode_endpoint():
    data = request.get_json(silent=True) or {}
    try:
        numbers = validate_number_list(data.get("numbers", []), "numbers")
        result = mode(numbers)
    except ValueError as e:
        return bad_request(str(e))
    except NotImplementedError:
        return not_implemented_error("mode")
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
