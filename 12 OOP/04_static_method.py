class animal:
    def __init__(self, name) -> None:
        self.name = name

    @classmethod
    def class_method(cls) -> None:
        print(cls)

    @staticmethod
    def classname() :
        return "animal"


print(animal.classname())
a = animal("lion")
a.class_method()
