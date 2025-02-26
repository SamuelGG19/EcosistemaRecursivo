import random


class Animal:
  def __init__(self):
    self.energia: int = 100

  def reducir_energia(self):
    self.energia -= 5

  def comer(self):
    self.energia += 10

  def reproduccion(self):
    pass

  def __str__(self):
    return f"A. E: {self.energia}"

class Depredador(Animal):

  def __str__(self):
    return f"D. E: {self.energia}"

class Presa(Animal):

  def __str__(self):
    return f"P. E: {self.energia}"

class Alimento:
  def __init__(self):
    self.energia: int = 100

  def reducir_energia(self):
    self.energia -= 5

  def __str__(self):
    return f"A. E: {self.energia}"

def generar_matriz(n: int, i: int = 0, j: int = 0,fila: list[Animal | Alimento | None] = [], matriz: list[list[Animal | Alimento | None]] = []) -> list[list[Animal | Alimento | None]]:
  if(i == n):
    return matriz
  if(j == n):
    matriz.append(fila)
    return generar_matriz(n, i+1, 0, [], matriz)
  num = random.randint(1, 100)
  if num > 90:
    fila.append(Depredador())
  elif num >= 43 and num <= 57:
    fila.append(Presa())
  elif num <= 10:
    fila.append(Alimento())
  else:
    fila.append(None)

  return generar_matriz(n, i, j+1, fila,  matriz)

def evolucion(matriz: list[list[str]], i: int = 0, j: int = 0):
  if i == len(matriz):
    return None
  if j == len(matriz[0]):
    return evolucion(matriz, i + 1, 0)
  if isinstance(matriz[i][j], Depredador):
    pass
    #return evolucion(matriz, i, j + 1)
  if isinstance(matriz[i][j], Presa):
    pass
    #return evolucion(matriz, i, j + 1)
  if isinstance(matriz[i][j], Alimento):
    pass
    #return ...

  return evolucion(matriz, i, j + 1)


m = generar_matriz(10)
for fila in m:
  print([str(objeto) if objeto else None for objeto in fila])