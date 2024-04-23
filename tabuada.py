#!/usr/bin/env python3

""" Imprime a tabuada do 1 ao 10. """
__version__ = "0.1.1"
__author__ = "Matheus"

# Iterable (objetos percorriveis)
# numeros = [1 ,2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))

for n1 in numeros:
    print("\n"+"{:*^20}".format(f"Tabuada do {n1}"))
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^20}".format(f"{n1} x {n2} = {resultado}"))
    print("-" * 20)
