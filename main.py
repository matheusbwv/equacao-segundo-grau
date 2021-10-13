# equacao-segundo-grau

import math

a = float(input("insira o valor de A: "))
if a == 0:
    print("A equação não é de segundo grau!!")
else:
    b = float(input("insira o valor de B: "))
    c = float(input("insira o valor de C: "))

    delta = b**2 - (4*a*c)

    if delta <0:
        print("A equacao não possui raizes reais")
    elif delta == 0:
        x = -b / (2 * a)
        print("delta", delta)
        print("a equacao possui raiz real", x)
    elif delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("A equacao possui duas raizes")
        print("delta", delta)
        print("raiz 1", x1)
        print("raiz 2", x2)