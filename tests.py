import pytest

from main import app, greet, add
from utils import clamp, flatten


def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("World") == "Hello, World!"


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_clamp():
    assert clamp(5, 0, 10) == 5
    assert clamp(-1, 0, 10) == 0
    assert clamp(15, 0, 10) == 10


def test_flatten():
    assert flatten([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]
    assert flatten([]) == []


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok", "version": "1.0"}


def test_greet_endpoint(client):
    response = client.post("/greet", json={"name": "Alice"})
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Alice!"}


def test_add_endpoint(client):
    response = client.post("/add", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.get_json() == {"result": 5}


def test_clamp_endpoint(client):
    response = client.post("/clamp", json={"value": 15, "min": 0, "max": 10})
    assert response.status_code == 200
    assert response.get_json() == {"result": 10}


def test_flatten_endpoint(client):
    response = client.post("/flatten", json={"nested": [1, [2, 3], [4, [5]]]})
    assert response.status_code == 200
    assert response.get_json() == {"result": [1, 2, 3, 4, 5]}


def test_slugify_endpoint(client):
    response = client.post("/slugify", json={"text": "Hello World!"})
    assert response.status_code == 200
    assert response.get_json() == {"result": "hello-world"}


def test_mean_endpoint(client):
    response = client.post("/mean", json={"numbers": [1, 2, 3]})
    assert response.status_code == 200
    assert response.get_json() == {"result": 2.0}


def test_median_endpoint_odd(client):
    response = client.post("/median", json={"numbers": [1, 2, 3]})
    assert response.status_code == 200
    assert response.get_json() == {"result": 2}


def test_median_endpoint_even(client):
    response = client.post("/median", json={"numbers": [1, 2, 3, 4]})
    assert response.status_code == 200
    assert response.get_json() == {"result": 2.5}


def test_mode_endpoint_most_frequent(client):
    response = client.post("/mode", json={"numbers": [1, 2, 2, 3]})
    assert response.status_code == 200
    assert response.get_json() == {"result": 2}


def test_mode_endpoint_tie_returns_smallest(client):
    response = client.post("/mode", json={"numbers": [1, 1, 2, 2]})
    assert response.status_code == 200
    assert response.get_json() == {"result": 1}


def test_invalid_input_returns_bad_request(client):
    response = client.post("/add", json={"a": "not a number", "b": 3})
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_empty_slugify_returns_bad_request(client):
    response = client.post("/slugify", json={"text": ""})
    assert response.status_code == 400
    assert "error" in response.get_json()


if __name__ == "__main__":
    test_greet()
    test_add()
    test_clamp()
    test_flatten()
    print("All tests passed.")
