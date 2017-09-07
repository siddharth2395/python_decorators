def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            # print("Whoops! cannot divide")
            return "Whoops! cannot divide"

        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    return a / b


print divide(2, 3)
print divide(2, 0)
