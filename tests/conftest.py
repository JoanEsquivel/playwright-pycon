import json
import pytest

from playwright.sync_api import Playwright
from testlib.inputs import User

#HELPERS 

# _build_todo function to handle the dictionary structure of the todos
def _build_todo(inputs, key):
    assert 'todos' in inputs, "inputs are missing 'todos' key"
    todos = inputs['todos']

    assert key in todos, f"key {key} is not found in input 'todos'"

    todo = todos[key]
    return todo

def _build_user(inputs, index):
  assert 'users' in inputs, "inputs are missing 'users' key"
  users = inputs['users']

  assert len(users) > index, f"index {index} is out of range for input 'users'"
  assert 'username' in users[index], f"input 'users[{index}]' is missing 'username'"
  assert 'password' in users[index], f"input 'users[{index}]' is missing 'password'"
  user = User(users[index]['username'], users[index]['password'])

  return user

@pytest.fixture(scope="session")
def test_inputs():
    with open('data/inputs.json') as inputs_json:
        data = json.load(inputs_json)
    return data


@pytest.fixture
def load_todo(test_inputs):
    def _loader(key):
        return _build_todo(test_inputs, key)
    return _loader

@pytest.fixture(scope='session')
def user(test_inputs):
  return _build_user(test_inputs, 0)