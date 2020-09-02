import math

print('Podaj wspolczynniki funkcji kwadratowej: ')

a = float(input())
b = float(input())
c = float(input())

if a!=0:

    delta = b*b - 4*a*c

    if delta > 0:
        x1 = -b-math.sqrt(delta)
        x2 = -b+math.sqrt(delta)
        print('x1 = ', x1)
        print('x2 = ', x2)
    elif delta < 0:
        print('brak rozwiazan')
    else:
        x = -b/2*a
        print('x = ', x)

else:
    x = -c/b
    print('x = ', x)