import random


class Animal:
  def __init__(self):
    self.energia: int = 100
    self.movimiento: bool = False

  def reducir_energia(self):
    self.energia -= 5

  def comer(self):
    self.energia += 10

  def reproduccion(self, matriz: list[list], direccion: str | int, i: int = 0, j: int = 0):
    pass


class Depredador(Animal):
  def reproduccion(self, matriz: list[list], direccion: str, i: int = 0, j: int = 0):
    if direccion == "arr":
      try:
        if matriz[i][j-1] is None:
          matriz[i][j-1] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i][j+1] is None:
          matriz[i][j+1] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i-1][j-1] is None:
          matriz[i-1][j-1] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i-1][j+1] is None:
          matriz[i-1][j+1] = Presa()
      except IndexError:
        pass

      return None

    if direccion == "abj":
      try:
        if matriz[i][j-1] is None:
          matriz[i][j-1] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i][j+1] is None:
          matriz[i][j+1] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i+1][j-1] is None:
          matriz[i+1][j-1] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i+1][j+1] is None:
          matriz[i+1][j+1] = Presa()
      except IndexError:
        pass

      return None

    if direccion == "izq":
      try:
        if matriz[i-1][j] is None:
          matriz[i-1][j] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i+1][j] is None:
          matriz[i+1][j] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i-1][j-1] is None:
          matriz[i-1][j-1] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i+1][j-1] is None:
          matriz[i+1][j-1] = Presa()
      except IndexError:
        pass

      return None

    if direccion == "der":
      try:
        if matriz[i-1][j] is None:
          matriz[i-1][j] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i+1][j] is None:
          matriz[i+1][j] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i-1][j+1] is None:
          matriz[i-1][j+1] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i+1][j+1] is None:
          matriz[i+1][j+1] = Presa()
      except IndexError:
        pass

      return None

  def __str__(self):
    if self.energia >= 20:
      return "D"
    else:
      return "d"

class Presa(Animal):
  def reproduccion(self, matriz: list[list], direccion: int, i: int = 0, j: int = 0):
    if direccion == 1:
      if matriz[i][j-1] is None:
        matriz[i][j-1] = Presa()
      if matriz[i-1][j] is None:
        matriz[i-1][j] = Presa()
      return None

    if direccion == 2:
      try:
        if matriz[i][j-1] is None:
          matriz[i][j-1] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i][j+1] is None:
          matriz[i][j+1] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i-1][j-1] is None:
          matriz[i-1][j-1] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i-1][j+1] is None:
          matriz[i-1][j+1] = Presa()
      except IndexError:
        pass

      return None

    if direccion == 3:
      if matriz[i][j+1] is None:
        matriz[i][j+1] = Presa()
      if matriz[i-1][j] is None:
        matriz[i-1][j] = Presa()
      return None

    if direccion == 4:
      try:
        if matriz[i-1][j] is None:
          matriz[i-1][j] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i+1][j] is None:
          matriz[i+1][j] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i-1][j-1] is None:
          matriz[i-1][j-1] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i+1][j-1] is None:
          matriz[i+1][j-1] = Presa()
      except IndexError:
        pass

      return None

    if direccion == 5:
      try:
        if matriz[i-1][j] is None:
          matriz[i-1][j] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i+1][j] is None:
          matriz[i+1][j] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i-1][j+1] is None:
          matriz[i-1][j+1] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i+1][j+1] is None:
          matriz[i+1][j+1] = Presa()
      except IndexError:
        pass

      return None

    if direccion == 6:
      if matriz[i][j-1] is None:
        matriz[i][j-1] = Presa()
      if matriz[i+1][j] is None:
        matriz[i+1][j] = Presa()
      return None

    if direccion == 7:
      try:
        if matriz[i][j-1] is None:
          matriz[i][j-1] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i][j+1] is None:
          matriz[i][j+1] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i+1][j-1] is None:
          matriz[i+1][j-1] = Presa()
      except IndexError:
        pass

      try:
        if matriz[i+1][j+1] is None:
          matriz[i+1][j+1] = Presa()
      except IndexError:
        pass

      return None

    if direccion == 8:
      if matriz[i][j+1] is None:
        matriz[i][j+1] = Presa()
      if matriz[i+1][j] is None:
        matriz[i+1][j] = Presa()
      return None

  def __str__(self):
    if self.energia >= 20:
      return "P"
    else:
      return "p"

class Alimento:
  def __init__(self):
    self.energia: int = 100

  def reducir_energia(self):
    self.energia -= 5

  def __str__(self):
    if self.energia <= 20:
      return "A"
    else:
      return "a"

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

def movimiento_presa(matriz: list[list[Animal | Alimento | None]], direccion: int, i: int, j: int):
  matriz[i][j].reducir_energia()
  if matriz[i][j].energia == 0:
    matriz[i][j] = None
    return None

  if direccion == 1:
    fila_nueva = i - 1
    columna_nueva = j - 1
  elif direccion == 2:
    fila_nueva = i - 1
    columna_nueva = j
  elif direccion == 3:
    fila_nueva = i - 1
    columna_nueva = j + 1
  elif direccion == 4:
    fila_nueva = i
    columna_nueva = j - 1
  elif direccion == 5:
    fila_nueva = i
    columna_nueva = j + 1
  elif direccion == 6:
    fila_nueva = i + 1
    columna_nueva = j - 1
  elif direccion == 7:
    fila_nueva = i + 1
    columna_nueva = j
  elif direccion == 8:
    fila_nueva = i + 1
    columna_nueva = j + 1

  if isinstance(matriz[fila_nueva][columna_nueva], Depredador):
    matriz[i][j] = None
    return None
  if isinstance(matriz[fila_nueva][columna_nueva], Presa):
    matriz[i][j].reproduccion(matriz, direccion)
    matriz[i][j].movimiento = True
    return None
  if isinstance(matriz[fila_nueva][columna_nueva], Alimento):
    matriz[i][j].comer()
    matriz[fila_nueva][columna_nueva] = matriz[i][j]
    matriz[i][j] = None
    matriz[fila_nueva][columna_nueva].movimiento = True
    return None

  matriz[fila_nueva][columna_nueva] = matriz[i][j]
  matriz[i][j] = None
  matriz[fila_nueva][columna_nueva].movimiento = True
  return None

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

def direccion_movimiento_depredador(matriz: list[list[Animal | Alimento | None]], fila: int, columna: int, index: int = 0, presas: list[int | None] = [], presas_cercanas: list[int] = []) -> str:
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
    return direccion_movimiento_depredador(matriz, fila, columna, index + 1, presas, presas_cercanas)

  return direccion_movimiento_depredador(matriz, fila, columna, index + 1, presas, presas_cercanas)

def movimiento_depredador(matriz: list[list[Animal | Alimento | None]], i: int, j: int):
  matriz[i][j].reducir_energia()
  if matriz[i][j].energia == 0:
    matriz[i][j] = None
    return None

  direccion = direccion_movimiento_depredador(matriz, i, j)
  if direccion == "arr":
    fila_nueva = i-1
    columna_nueva = j
  if direccion == "abj":
    fila_nueva = i+1
    columna_nueva = j
  if direccion == "izq":
    fila_nueva = i
    columna_nueva = j-1
  if direccion == "der":
    fila_nueva = i
    columna_nueva = j+1
  if direccion == "N":
    nueva_direccion = random.randint(1, 4)
    if nueva_direccion == 1:
      fila_nueva = i-1
      columna_nueva = j
    if nueva_direccion == 2:
      fila_nueva = i+1
      columna_nueva = j
    if nueva_direccion == 3:
      fila_nueva = i
      columna_nueva = j-1
    if nueva_direccion == 4:
      fila_nueva = i
      columna_nueva = j+1

  if isinstance(matriz[fila_nueva][columna_nueva], Depredador):
    matriz[i][j].reproduccion(matriz, direccion)
    matriz[i][j].movimiento = True
    return None
  if isinstance(matriz[fila_nueva][columna_nueva], Presa) or isinstance(matriz[fila_nueva][columna_nueva], Alimento):
    matriz[i][j].comer()
    matriz[fila_nueva][columna_nueva] = matriz[i][j]
    matriz[i][j] = None
    matriz[fila_nueva][columna_nueva].movimiento = True
    return None

  matriz[fila_nueva][columna_nueva] = matriz[i][j]
  matriz[i][j] = None
  matriz[fila_nueva][columna_nueva].movimiento = True
  return None

def evolucion(matriz: list[list[Animal | Alimento | None]], i: int = 0, j: int = 0):
  if i == len(matriz):
    return None
  if j == len(matriz[0]):
    return evolucion(matriz, i + 1, 0)

  if isinstance(matriz[i][j], Presa):
    direccion = random.randint(1, 8)
    movimiento_presa(matriz, direccion, i, j)
    return evolucion(matriz, i, j + 1)

  if isinstance(matriz[i][j], Depredador):
    movimiento_depredador(matriz, i, j)
    return evolucion(matriz, i, j + 1)

  if isinstance(matriz[i][j], Alimento):
    matriz[i][j].reducir_energia()
    if matriz[i][j].energia == 0:
      matriz[i][j] = None
    return evolucion(matriz, i, j+1)

  return evolucion(matriz, i, j + 1)

def imprimir_matriz(matriz: list[list[Animal | Alimento | None]], i: int = 0, j: int = 0, fila: list[str] = []):
  if i == len(matriz):
    return None
  if j == len(matriz):
    print(fila)
    return imprimir_matriz(matriz, i+1, 0, [])

  if matriz[i][j] is not None:
    fila.append(str(matriz[i][j]))
    return imprimir_matriz(matriz, i, j+1, fila)

  fila.append(" ")
  return imprimir_matriz(matriz, i, j+1, fila)

if __name__ == "__main__":
  m = generar_matriz(10)
  imprimir_matriz(m)