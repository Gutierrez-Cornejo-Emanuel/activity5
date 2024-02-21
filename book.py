

class Book():
    def __init__(self, title) -> None:
        self.title = title

    def __eq__(self, other):
        return self.title == other.title
    def __str__(self):
        return self.title
    def __repr__(self):
        return self.title
    