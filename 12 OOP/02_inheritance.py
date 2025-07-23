class animal:
    def __init__(self, name):
        self.name = name


class cat(animal):

    def __init__(self, name, type) -> None:
        super().__init__(name)
    pass


c = cat("kitty", "pet")
