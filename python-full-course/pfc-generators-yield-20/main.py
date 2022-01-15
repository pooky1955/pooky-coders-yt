def generate_range(n):
    counter = 1
    while counter <= n:
        yield counter
        counter += 1

def generate_yos():
    while True:
        print("next!")
        yield "yo"

iterator = generate_yos()
next(iterator)
next(iterator)
