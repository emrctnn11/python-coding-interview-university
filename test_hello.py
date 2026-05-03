from hello import greet


def test_greet_basic():
    assert greet("World") == "Greetings, World!"


def test_greet_empty():
    assert greet("" == "Hello, !")
