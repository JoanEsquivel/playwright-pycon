import json
import pytest


@pytest.fixture(scope="session")
def load_json_data():
    def _loader(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return _loader