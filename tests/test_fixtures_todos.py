from playwright.sync_api import expect, Page
from pages.todo_page import TodoPage


def test_add_new_todo_pom_fixture(page: Page, load_todo) -> None:
    todo = load_todo("todo1")
    todo_page = TodoPage(page)
    todo_page.load()
    todo_page.add_todo(todo)
    expect(todo_page.todo_items).to_have_text(todo)
