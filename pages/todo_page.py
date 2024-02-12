from playwright.sync_api import Page

class TodoPage:
    URL = 'https://demo.playwright.dev/todomvc/#/'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.todo_input = page.locator('.new-todo')
        self.todo_item = page.locator('[data-testid="todo-title"]')

    def load(self) -> None:
            self.page.goto(self.URL)

    def add_todo(self, todo: str) -> None:
            self.todo_input.fill(todo)
            self.page.keyboard.press('Enter')


