def div_check(function):
    def inner(a, b):
        print("hi")
        if b == 0:
            return "Give a valid input"
        return function(a, b)

    return inner


@div_check
def div(a, b):
    return a / b


print(div(20, 0))
