# Commands:
# To check an individual file: ruff check tests/test_fixtures_todos_lint.py
# To check the whole framework ruff check .
# To fix everything(if possible): ruff tests/test_fixtures_todos_lint.py --fix
# To format: ruff format .

from playwright.sync_api import expect, Page
from pages.todo_page import TodoPage

# Example 1: Unused Import
# import pytest


def test_add_new_todo_pom_fixture(page: Page, load_todo) -> None:
    todo = load_todo("todo1")
    todo_page = TodoPage(page)
    todo_page.load()
    todo_page.add_todo(todo)
    expect(todo_page.todo_item).to_have_text(todo)
    # Example 2: Unused Variable
    # var = "https://example.com/this/is/a/very/long/url/that/exceeds/the/typical/line/length/limit/and/should/be/broken/up/for/readability"
    # Example 3: Identation error
    #    todo_page.add_todo(todo)
    # Example 4: Missing Import
    # assert os.path.exists("somefile.txt")
    # Example 5: Multiple Statements on One Line
    # page.goto("https://example.com"); assert page.title() == "Example Domain"
    # Example 6: Trailing Whitespace
    # todo_page.add_todo(todo)
