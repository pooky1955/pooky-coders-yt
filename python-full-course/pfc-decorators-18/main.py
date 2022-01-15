def create_decorate_run_n_times(n):
    def decorate_n_times(some_function):
        def new_function():
            for i in range(n):
                some_function()
        return new_function
    return decorate_n_times


def decorate_run_two_times(some_function):
    def new_function():
        some_function()
        some_function()
    return new_function

@create_decorate_run_n_times(5)
def greet():
    print("Hello!")

greet()
# decorated_triple_greet()
