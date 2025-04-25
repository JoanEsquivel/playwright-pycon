# Browser: It is a single instance of a web browser.
# Context: It is an isolated incognito-alike session within a browser instance. One browser may have multiple browser contexts. The recommended practice is for all tests to share one browser instance but for each test to have its own browser context.
# Page: It is a single tab or window within a browser context. A browser context may have multiple pages. Typically, an individual test should interact with only one page.

from playwright.sync_api import expect, Page


def test_add_new_todo(
    page: Page,
) -> None:
    # Given I am on the todo list page
    page.goto("/todomvc/#/")
    # When the user enters "Asistir a PyCon" into the add item input
    # page.locator('.new-todo').fill('Asistir a PyCon')
    page.get_by_role("textbox", name="What needs to be done?").fill(
        "Viajar a PyCon USA"
    )
    # And the user press the "enter" keyboard
    page.keyboard.press("Enter")
    # Then "Asistir a PyCon" should be added to the list
    # https://playwright.dev/python/docs/test-assertions
    expect(page.locator('[data-testid="todo-title"]')).to_have_text(
        "Viajar a PyCon USA"
    )
