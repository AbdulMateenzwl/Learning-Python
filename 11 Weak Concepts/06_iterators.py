class EvenNumbers:
    def __iter__(self):
        self.n = 2 
        return self

    def __next__(self):
        if(self.n > 100):
            raise StopIteration
        x = self.n
        self.n += 2 
        return x

even = EvenNumbers()
it = iter(even)

for num in even:
    print(num)