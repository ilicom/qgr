import time
import os
import math
from math import sqrt


while True:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    print("\nD = (",b, "*", b,") - 4 *", a, "*", c)

    d2 = (b * b) - 4 * a * c

    if d2 == 0:
        d = sqrt(d2)
        x = (-b + d) / (2 * a)

        print("\n", d, "\n")

        print("\n\nx = (", -b, "+", d, ") / (2 *", a, ")")

        print("\n\nEine reele Lösung: x =", x)
    
    elif d2 < 0:       
        print("\nKeine reele Lösung!")

    else:
        d = sqrt(d2)
        print('-----------------------------------------------')
        print('D =', d)

        print('-----------------------------------------------')

        print("x1 = (", -b, "+", d, ") / (2 *", a, ")")

        print("x2 = (", -b, "-", d, ") / (2 *", a, ")")

        print('-----------------------------------------------')

        x1 = (-b + d) / (2 * a)

        x2 = (-b - d) / (2 * a)

        print("\nX1 =", x1, "\n\nX2 =", x2 )
    
    g = input("\nPress Enter!")
    os.system('cls||clear')