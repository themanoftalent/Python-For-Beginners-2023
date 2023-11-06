def fiboon(n):
    a = 1
    b = 1

    for i in range (n - 1):
        a, b = b, b + a
    return a


print (fiboon (7))
