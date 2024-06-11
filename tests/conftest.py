import json
import pytest

from playwright.sync_api import Playwright

def _returnTodoByKey(data, key):
    assert 'todos' in data, "inputs are missing 'todos' key"
    todos = data['todos']

    assert key in todos, f"key {key} is not found in input 'todos'"

    todo = todos[key]
    return todo


@pytest.fixture(scope="session")
def loadData():
    with open('data/inputs.json') as inputs_json:
        data = json.load(inputs_json)
    return data


@pytest.fixture
def load_todo(loadData):
    def _loader(key):
        return _returnTodoByKey(loadData, key)
    return _loader
