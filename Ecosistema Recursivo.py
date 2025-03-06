import random


class Animal:
  def __init__(self):
    self.energia: int = 100
    self.movimiento: bool = False

  def reducir_energia(self):
    self.energia -= 5

  def comer(self):
    self.energia += 10

  def reproduccion(self, matriz: list[list], direccion: str, i: int = 0, j: int = 0):
    pass


class Depredador(Animal):
  def reproduccion(self, matriz: list[list], direccion: str, i: int = 0, j: int = 0):
    if direccion == "arr":
      if isinstance(matriz[i-1][j], Depredador):
        try:
          matriz[i][j-1] = Depredador()
        except IndexError:
          pass
        try:
          matriz[i][j+1] = Depredador()
        except IndexError:
          pass
        try:
          matriz[i-1][j-1] = Depredador()
        except IndexError:
          pass
        try:
          matriz[i-1][j+1] = Depredador()
        except IndexError:
          pass

    if direccion == "abj":
      try:
        matriz[i][j-1] = Depredador()
      except IndexError:
        pass
      try:
        matriz[i][j+1] = Depredador()
      except IndexError:
        pass
      try:
        matriz[i+1][j-1] = Depredador()
      except IndexError:
        pass
      try:
        matriz[i+1][j+1] = Depredador()
      except IndexError:
        pass

    if direccion == "izq":
      try:
        matriz[i-1][j] = Depredador()
      except IndexError:
        pass
      try:
        matriz[i+1][j] = Depredador()
      except IndexError:
        pass
      try:
        matriz[i-1][j-1] = Depredador()
      except IndexError:
        pass
      try:
        matriz[i+1][j-1] = Depredador()
      except IndexError:
        pass

    if direccion == "der":
      try:
        matriz[i-1][j] = Depredador()
      except IndexError:
        pass
      try:
        matriz[i+1][j] = Depredador()
      except IndexError:
        pass
      try:
        matriz[i-1][j+1] = Depredador()
      except IndexError:
        pass
      try:
        matriz[i+1][j+1] = Depredador()
      except IndexError:
        pass

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

def generar_matriz(n: int, i: int = 0, j: int = 0, fila: list[Animal | Alimento | None] = [], matriz: list[list[Animal | Alimento | None]] = []) -> list[list[Animal | Alimento | None]]:
  if i == n:
    return matriz
  if j == n:
    matriz.append(fila)
    return generar_matriz(n, i+1, 0, [], matriz)
  num = random.randint(1, 100)
  if num > 90:
    fila.append(Depredador())
  elif 43 <= num <= 57:
    fila.append(Presa())
  elif num <= 10:
    fila.append(Alimento())
  else:
    fila.append(None)

  return generar_matriz(n, i, j+1, fila,  matriz)


def buscar_presa(matriz: list[list[Animal | Alimento | None]], fila: int, columna: int, index: int = 1, direccion: str = "arr", distancia: list[int | None] = []):
  if direccion == "arr":
    if 0 <= fila - index < len(matriz):
      if isinstance(matriz[fila - index][columna], Presa):
        distancia.append(index)
        return buscar_presa(matriz, fila, columna, 1, "abj", distancia)

      return buscar_presa(matriz, fila, columna, index + 1, direccion, distancia)

    distancia.append(None)
    return buscar_presa(matriz, fila, columna, 1, "abj", distancia)

  if direccion == "abj":
    if 0 <= fila + index < len(matriz):
      if isinstance(matriz[fila + index][columna], Presa):
        distancia.append(index)
        return buscar_presa(matriz, fila, columna, 1, "izq", distancia)

      return buscar_presa(matriz, fila, columna, index + 1, direccion, distancia)

    distancia.append(None)
    return buscar_presa(matriz, fila, columna, 1, "izq", distancia)

  if direccion == "izq":
    if 0 <= columna - index < len(matriz):
      if isinstance(matriz[fila][columna - index], Presa):
        distancia.append(index)
        return buscar_presa(matriz, fila, columna, 1, "der", distancia)

      return buscar_presa(matriz, fila, columna, index + 1, direccion, distancia)

    distancia.append(None)
    return buscar_presa(matriz, fila, columna, 1, "der", distancia)

  if direccion == "der":
    if 0 <= columna + index < len(matriz):
      if isinstance(matriz[fila][columna + index], Presa):
        distancia.append(index)
        return buscar_presa(matriz, fila, columna, 1, "F", distancia)

      return buscar_presa(matriz, fila, columna, index + 1, direccion, distancia)

    distancia.append(None)
    return buscar_presa(matriz, fila, columna, 1, "F", distancia)

  if direccion == "F":
    return distancia


def movimiento_depredador(matriz: list[list[Animal | Alimento | None]], fila: int, columna: int, index: int = 0, presas: list[int | None] = [], presas_cercanas: list[int] = []) -> str:
  if presas == []:
    presas = buscar_presa(matriz, fila, columna, 1, "arr", [])

  if index == len(presas):
    try:
      distancia = min(presas_cercanas)
    except ValueError:
      return "N"
    else:
      if presas.index(distancia) == 0:
        return "arr"
      if presas.index(distancia) == 1:
        return "abj"
      if presas.index(distancia) == 2:
        return "izq"
      if presas.index(distancia) == 3:
        return "der"

  if presas[index] is not None:
    presas_cercanas.append(presas[index])
    return movimiento_depredador(matriz, fila, columna, index + 1, presas, presas_cercanas)

  return movimiento_depredador(matriz, fila, columna, index + 1, presas, presas_cercanas)


def evolucion(matriz: list[list[Animal | Alimento | None]], i: int = 0, j: int = 0):
  if i == len(matriz):
    return None
  if j == len(matriz[0]):
    return evolucion(matriz, i + 1, 0)
  if isinstance(matriz[i][j], Presa):
    pass
    #return evolucion(matriz, i, j + 1)
  if isinstance(matriz[i][j], Depredador):
    matriz[i][j].reducir_energia()
    if matriz[i][j].energia == 0:
      matriz[i][j] = None
      return evolucion(matriz, i, j+1)

    direccion = movimiento_depredador(matriz, i, j)
    if direccion == "arr":
      if isinstance(matriz[i-1][j], Depredador):
        matriz[i][j].reproduccion(matriz, direccion)
        matriz[i][j].movimiento = True
        return evolucion(matriz, i, j + 1)
      if isinstance(matriz[i-1][j], Presa) or isinstance(matriz[i-1][j], Alimento):
        matriz[i][j].comer()
        matriz[i-1][j] = matriz[i][j]
        matriz[i][j].movimiento = True
        return evolucion(matriz, i, j + 1)

      matriz[i-1][j] = matriz[i][j]
      matriz[i][j].movimiento = True
      return evolucion(matriz, i, j + 1)

    if direccion == "abj":
      if isinstance(matriz[i+1][j], Depredador):
        matriz[i][j].reproduccion(matriz, direccion)
        matriz[i][j].movimiento = True
        return evolucion(matriz, i, j + 1)
      if isinstance(matriz[i+1][j], Presa) or isinstance(matriz[i+1][j], Alimento):
        matriz[i][j].comer()
        matriz[i+1][j] = matriz[i][j]
        matriz[i][j].movimiento = True
        return evolucion(matriz, i, j + 1)

      matriz[i+1][j] = matriz[i][j]
      matriz[i][j].movimiento = True
      return evolucion(matriz, i, j + 1)

    if direccion == "izq":
      if isinstance(matriz[i][j-1], Depredador):
        matriz[i][j].reproduccion(matriz, direccion)
        matriz[i][j].movimiento = True
        return evolucion(matriz, i, j + 1)
      if isinstance(matriz[i][j-1], Presa) or isinstance(matriz[i][j-1], Alimento):
        matriz[i][j].comer()
        matriz[i][j-1] = matriz[i][j]
        matriz[i][j].movimiento = True
        return evolucion(matriz, i, j + 1)

      matriz[i][j-1] = matriz[i][j]
      matriz[i][j].movimiento = True
      return evolucion(matriz, i, j + 1)

    if direccion == "der":
      if isinstance(matriz[i][j+1], Depredador):
        matriz[i][j].reproduccion(matriz, direccion)
        matriz[i][j].movimiento = True
        return evolucion(matriz, i, j + 1)
      if isinstance(matriz[i][j+1], Presa) or isinstance(matriz[i][j+1], Alimento):
        matriz[i][j].comer()
        matriz[i][j+1] = matriz[i][j]
        matriz[i][j].movimiento = True
        return evolucion(matriz, i, j + 1)

      matriz[i][j+1] = matriz[i][j]
      matriz[i][j].movimiento = True
      return evolucion(matriz, i, j + 1)

    if direccion == "N":
      nueva_direccion = random.randint(1, 4)
      if nueva_direccion == 1:
        if isinstance(matriz[i - 1][j], Depredador):
          matriz[i][j].reproduccion(matriz, direccion)
          matriz[i][j].movimiento = True
          return evolucion(matriz, i, j + 1)
        if isinstance(matriz[i - 1][j], Presa) or isinstance(matriz[i - 1][j], Alimento):
          matriz[i][j].comer()
          matriz[i - 1][j] = matriz[i][j]
          matriz[i][j].movimiento = True
          return evolucion(matriz, i, j + 1)

        matriz[i - 1][j] = matriz[i][j]
        matriz[i][j].movimiento = True
        return evolucion(matriz, i, j + 1)

      if nueva_direccion == 2:
        if isinstance(matriz[i + 1][j], Depredador):
          matriz[i][j].reproduccion(matriz, direccion)
          matriz[i][j].movimiento = True
          return evolucion(matriz, i, j + 1)
        if isinstance(matriz[i + 1][j], Presa) or isinstance(matriz[i + 1][j], Alimento):
          matriz[i][j].comer()
          matriz[i + 1][j] = matriz[i][j]
          matriz[i][j].movimiento = True
          return evolucion(matriz, i, j + 1)

        matriz[i + 1][j] = matriz[i][j]
        matriz[i][j].movimiento = True
        return evolucion(matriz, i, j + 1)

      if nueva_direccion == 3:
        if isinstance(matriz[i][j - 1], Depredador):
          matriz[i][j].reproduccion(matriz, direccion)
          matriz[i][j].movimiento = True
          return evolucion(matriz, i, j + 1)
        if isinstance(matriz[i][j - 1], Presa) or isinstance(matriz[i][j - 1], Alimento):
          matriz[i][j].comer()
          matriz[i][j - 1] = matriz[i][j]
          matriz[i][j].movimiento = True
          return evolucion(matriz, i, j + 1)

        matriz[i][j - 1] = matriz[i][j]
        matriz[i][j].movimiento = True
        return evolucion(matriz, i, j + 1)

      if nueva_direccion == 4:
        if isinstance(matriz[i][j + 1], Depredador):
          matriz[i][j].reproduccion(matriz, direccion)
          matriz[i][j].movimiento = True
          return evolucion(matriz, i, j + 1)
        if isinstance(matriz[i][j + 1], Presa) or isinstance(matriz[i][j + 1], Alimento):
          matriz[i][j].comer()
          matriz[i][j + 1] = matriz[i][j]
          matriz[i][j].movimiento = True
          return evolucion(matriz, i, j + 1)

        matriz[i][j + 1] = matriz[i][j]
        matriz[i][j].movimiento = True
        return evolucion(matriz, i, j + 1)

  if isinstance(matriz[i][j], Alimento):
    pass
    #return ...

  return evolucion(matriz, i, j + 1)


m = generar_matriz(10)
for fila in m:
  print([str(objeto) if objeto else " " for objeto in fila])