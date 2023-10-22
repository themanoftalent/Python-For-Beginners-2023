fib_array = [0, 1]


def fib(n):
    if n < len(fib_array):
        return fib_array[n]
    else:
        temp_fib = fib(n - 1) + fib(n - 2)
        fib_array.append(temp_fib)
        return temp_fib


print(fib(40))
