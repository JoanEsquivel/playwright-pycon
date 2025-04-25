from playwright.sync_api import Page


class TodoPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.todo_input = page.locator(".new-todo")

    @property
    def todo_items(self):
        return self.page.locator('[data-testid="todo-title"]')

    def load(self):
        self.page.goto("/todomvc/#/")

    def add_todo(self, todo: str):
        self.todo_input.fill(todo)
        self.page.keyboard.press("Enter")
