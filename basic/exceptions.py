
class StoryError(Exception):
    def __init__(self, name):
        self.name = name