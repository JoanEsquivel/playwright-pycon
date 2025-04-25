import json
import os
import pytest


def get_todo_by_key(data, key):
    assert "todos" in data, "Missing 'todos' key in input data"
    todos = data["todos"]

    assert key in todos, f"Key '{key}' not found in 'todos'"
    return todos[key]


@pytest.fixture(scope="session")
def load_data():
    path = "data/inputs.json"
    if not os.path.exists(path):
        pytest.fail(f"Missing required input file: {path}")
    try:
        with open(path) as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        pytest.fail(f"Invalid JSON in {path}: {e}")


@pytest.fixture
def load_todo(load_data):
    def _loader(key):
        return get_todo_by_key(load_data, key)

    return _loader
