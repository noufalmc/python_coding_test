def capitalize(function):
    def inner():
        string = function()
        return string.upper()
    return inner

@capitalize
def string():
    return "good morning"

print(string())