import json
import pytest


def return_todo_by_key(data, key):
    assert "todos" in data, "inputs are missing 'todos' key"
    todos = data["todos"]

    assert key in todos, f"key {key} is not found in input 'todos'"

    todo = todos[key]
    return todo


@pytest.fixture(scope="session")
def load_data():
    with open("data/inputs.json") as inputs_json:
        data = json.load(inputs_json)
    return data


@pytest.fixture
def load_todo(load_data):
    def _loader(key):
        return return_todo_by_key(load_data, key)

    return _loader
