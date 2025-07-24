
def generate():
    num = 0
    while True:
        yield num
        num += 1
        if (num > 1000):
            return


for val in generate():
    print(val)

nums = [1, 2, 3, 4, 5, 6, 7]
listt = (num**2 for num in nums)

for num in listt:
    print(num)