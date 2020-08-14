# add an `Item` class
# The item should have `name` and `description` attributes
#   * Hint: the name should be one word for ease in parsing later
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

    def on_take(self):
        print(f"You have picked up {self.name}")
