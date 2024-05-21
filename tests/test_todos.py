# Browser: It is a single instance of a web browser.
# Context: It is an isolated incognito-alike session within a browser instance. One browser may have multiple browser contexts. The recommended practice is for all tests to share one browser instance but for each test to have its own browser context.
# Page: It is a single tab or window within a browser context. A browser context may have multiple pages. Typically, an individual test should interact with only one page.

from playwright.sync_api import expect,Page
from pages.todo_page import TodoPage

def test_add_new_todo(page: Page,) -> None:

    # Given I am on the todo list page
    page.goto('/todomvc/#/')
    # When the user enters "Buy milk" into the add item input
    page.locator('.new-todo').fill('Buy milk')
    # And the user press the "enter" keyboard
    page.keyboard.press('Enter')
    # Then "Buy milk" should be added to the list
    expect(page.locator('[data-testid="todo-title"]')).to_have_text('Buy milk')

def test_add_new_todo_pom(page: Page) -> None:
    todo_page = TodoPage(page)
    todo_page.load()
    todo_page.add_todo('Buy milk')
    expect(todo_page.todo_item).to_have_text('Buy milk')

def test_add_new_todo_pom_fixture(page: Page, load_todo) -> None:
    todo = load_todo('todo1')
    todo_page = TodoPage(page)
    todo_page.load()
    todo_page.add_todo(todo)
    expect(todo_page.todo_item).to_have_text(todo)
