from main import greet, add
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


if __name__ == "__main__":
    test_greet()
    test_add()
    test_clamp()
    test_flatten()
    print("All tests passed.")
