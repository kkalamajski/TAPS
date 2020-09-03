from functools import partial

def multiplication(a,b,c):
    return a*b*c

g = partial(multiplication, 2)

print(g(5,2))
