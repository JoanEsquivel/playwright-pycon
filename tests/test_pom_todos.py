from playwright.sync_api import expect, Page
from pages.todo_page import TodoPage


def test_add_new_todo(page: Page) -> None:
    todo_page = TodoPage(page)
    todo_page.load()
    todo_page.add_todo("Asistir a PyCon")
    expect(todo_page.todo_item).to_have_text("Asistir a PyCon")
