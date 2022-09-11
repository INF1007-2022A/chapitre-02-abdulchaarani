# nombre = float(input("Nombre?: "))
# carre = (nombre)**2
# racine = nombre**(1/2)

# print(f"Le carre de {nombre} est {carre}")
# print(f"La racine carree de {nombre} est {racine:.2f}")

def add(*args):
  return sum(*args)

import math
def print_base(n, b, digits):
  result = [None] * (int(math.log(n, b)) + 1)

  for i in range(len(result)):
    result[i] = n % b
    n = n // b

  return ''.join(map(lambda d: digits[d], reversed(result)))