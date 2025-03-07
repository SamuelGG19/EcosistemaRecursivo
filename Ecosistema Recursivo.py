import random


class Animal:
  def __init__(self):
    self.energia: int = 100
    self.movimiento: bool = False

  def reducir_energia(self):
    self.energia -= 5

  def comer(self):
    self.energia += 10


class Depredador(Animal):
  def reproduccion(self, matriz: list[list], direccion: str, nueva_direccion: int, i: int, j: int):
    if direccion == "arr" or (direccion == "N" and nueva_direccion == 1):
      try:
        if j-1 >= 0:
          if matriz[i][j-1] is None:
            matriz[i][j-1] = Depredador()
            return None
      except IndexError:
        pass

      try:
        if matriz[i][j+1] is None:
          matriz[i][j+1] = Depredador()
          return None
      except IndexError:
        pass

      try:
        if i-1 >= 0 and j-1 >= 0:
          if matriz[i-1][j-1] is None:
            matriz[i-1][j-1] = Depredador()
            return None
      except IndexError:
        pass

      try:
        if i-1 >= 0:
          if matriz[i-1][j+1] is None:
            matriz[i-1][j+1] = Depredador()
            return None
      except IndexError:
        pass

      return None

    if direccion == "abj" or (direccion == "N" and nueva_direccion == 2):
      try:
        if j-1 >= 0:
          if matriz[i][j-1] is None:
            matriz[i][j-1] = Depredador()
            return None
      except IndexError:
        pass

      try:
        if matriz[i][j+1] is None:
          matriz[i][j+1] = Depredador()
          return None
      except IndexError:
        pass

      try:
        if j-1 >= 0:
          if matriz[i+1][j-1] is None:
            matriz[i+1][j-1] = Depredador()
            return None
      except IndexError:
        pass

      try:
        if matriz[i+1][j+1] is None:
          matriz[i+1][j+1] = Depredador()
          return None
      except IndexError:
        pass

      return None

    if direccion == "izq" or (direccion == "N" and nueva_direccion == 3):
      try:
        if i-1 >= 0:
          if matriz[i-1][j] is None:
            matriz[i-1][j] = Depredador()
            return None
      except IndexError:
        pass

      try:
        if matriz[i+1][j] is None:
          matriz[i+1][j] = Depredador()
          return None
      except IndexError:
        pass

      try:
        if i-1 >= 0 and j-1 >= 0:
          if matriz[i-1][j-1] is None:
            matriz[i-1][j-1] = Depredador()
            return None
      except IndexError:
        pass

      try:
        if j-1 >= 0:
          if matriz[i+1][j-1] is None:
            matriz[i+1][j-1] = Depredador()
            return None
      except IndexError:
        pass

      return None

    if direccion == "der" or (direccion == "N" and nueva_direccion == 4):
      try:
        if i-1 >= 0:
          if matriz[i-1][j] is None:
            matriz[i-1][j] = Depredador()
            return None
      except IndexError:
        pass

      try:
        if matriz[i+1][j] is None:
          matriz[i+1][j] = Depredador()
          return None
      except IndexError:
        pass

      try:
        if i-1 >= 0:
          if matriz[i-1][j+1] is None:
            matriz[i-1][j+1] = Depredador()
            return None
      except IndexError:
        pass

      try:
        if matriz[i+1][j+1] is None:
          matriz[i+1][j+1] = Depredador()
          return None
      except IndexError:
        pass

      return None

  def __str__(self):
    if self.energia >= 20:
      return "D"
    else:
      return "d"

class Presa(Animal):
  def reproduccion(self, matriz: list[list], direccion: int, i: int, j: int):
    if direccion == 1:
      if matriz[i][j - 1] is None:
        matriz[i][j - 1] = Presa()
        return None
      if matriz[i - 1][j] is None:
        matriz[i - 1][j] = Presa()
        return None
      return None

    if direccion == 2:
      try:
        if j-1 >= 0:
          if matriz[i][j-1] is None:
            matriz[i][j-1] = Presa()
            return None
      except IndexError:
        pass

      try:
        if matriz[i][j+1] is None:
          matriz[i][j+1] = Presa()
          return None
      except IndexError:
        pass

      try:
        if i-1 >= 0 and j-1 >= 0:
          if matriz[i-1][j-1] is None:
            matriz[i-1][j-1] = Presa()
            return None
      except IndexError:
        pass

      try:
        if i-1 >= 0:
          if matriz[i-1][j+1] is None:
            matriz[i-1][j+1] = Presa()
            return None
      except IndexError:
        pass

      return None

    if direccion == 3:
      if matriz[i][j + 1] is None:
        matriz[i][j + 1] = Presa()
        return None
      if matriz[i - 1][j] is None:
        matriz[i - 1][j] = Presa()
        return None
      return None

    if direccion == 4:
      try:
        if i-1 >= 0:
          if matriz[i-1][j] is None:
            matriz[i-1][j] = Presa()
            return None
      except IndexError:
        pass

      try:
        if matriz[i+1][j] is None:
          matriz[i+1][j] = Presa()
          return None
      except IndexError:
        pass

      try:
        if i-1 >= 0 and j-1 >= 0:
          if matriz[i-1][j-1] is None:
            matriz[i-1][j-1] = Presa()
            return None
      except IndexError:
        pass

      try:
        if j-1 >= 0:
          if matriz[i+1][j-1] is None:
            matriz[i+1][j-1] = Presa()
            return None
      except IndexError:
        pass

      return None

    if direccion == 5:
      try:
        if i-1 >= 0:
          if matriz[i-1][j] is None:
            matriz[i-1][j] = Presa()
            return None
      except IndexError:
        pass

      try:
        if matriz[i+1][j] is None:
          matriz[i+1][j] = Presa()
          return None
      except IndexError:
        pass

      try:
        if i-1 >= 0 and j-1 >= 0:
          if matriz[i-1][j+1] is None:
            matriz[i-1][j+1] = Presa()
            return None
      except IndexError:
        pass

      try:
        if matriz[i+1][j+1] is None:
          matriz[i+1][j+1] = Presa()
      except IndexError:
        pass

      return None

    if direccion == 6:
      if matriz[i][j - 1] is None:
        matriz[i][j - 1] = Presa()
        return None
      if matriz[i + 1][j] is None:
        matriz[i + 1][j] = Presa()
        return None
      return None

    if direccion == 7:
      try:
        if j-1 >= 0:
          if matriz[i][j-1] is None:
            matriz[i][j-1] = Presa()
            return None
      except IndexError:
        pass

      try:
        if matriz[i][j+1] is None:
          matriz[i][j+1] = Presa()
          return None
      except IndexError:
        pass

      try:
        if j-1 >= 0:
          if matriz[i+1][j-1] is None:
            matriz[i+1][j-1] = Presa()
            return None
      except IndexError:
        pass

      try:
        if matriz[i+1][j+1] is None:
          matriz[i+1][j+1] = Presa()
          return None
      except IndexError:
        pass

      return None

    if direccion == 8:
      if matriz[i][j + 1] is None:
        matriz[i][j + 1] = Presa()
        return None
      if matriz[i + 1][j] is None:
        matriz[i + 1][j] = Presa()
        return None
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
    if self.energia >= 20:
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
  if matriz[i][j].movimiento:
    return None

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

  if fila_nueva < 0 or columna_nueva < 0:
    return movimiento_presa(matriz, direccion % 8 + 1, i, j)

  try:
    if isinstance(matriz[fila_nueva][columna_nueva], Depredador):
      matriz[i][j] = None
      return None
    if isinstance(matriz[fila_nueva][columna_nueva], Presa):
      matriz[i][j].reproduccion(matriz, direccion, i, j)
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
  except IndexError:
    return movimiento_presa(matriz, direccion % 8 + 1, i, j)

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
  if not presas:
    presas = buscar_presa(matriz, fila, columna, 1, "arr", [])
    presas_cercanas = []

  if index == len(presas):
    try:
      distancia = min(presas_cercanas)
      if presas.index(distancia) == 0:
        return "arr"
      if presas.index(distancia) == 1:
        return "abj"
      if presas.index(distancia) == 2:
        return "izq"
      if presas.index(distancia) == 3:
        return "der"
    except ValueError:
      return "N"

  if presas[index] is not None:
    presas_cercanas.append(presas[index])
    return direccion_movimiento_depredador(matriz, fila, columna, index + 1, presas, presas_cercanas)

  return direccion_movimiento_depredador(matriz, fila, columna, index + 1, presas, presas_cercanas)

def movimiento_depredador(matriz: list[list[Animal | Alimento | None]], i: int, j: int):
  if matriz[i][j].movimiento:
    return None

  matriz[i][j].reducir_energia()
  if matriz[i][j].energia == 0:
    matriz[i][j] = None
    return None

  direccion = direccion_movimiento_depredador(matriz, i, j)
  nueva_direccion = 0
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

  if fila_nueva < 0 or columna_nueva < 0:
    return movimiento_depredador(matriz, i, j)

  try:
    if isinstance(matriz[fila_nueva][columna_nueva], Depredador):
      matriz[i][j].reproduccion(matriz, direccion, nueva_direccion, i, j)
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
  except IndexError:
    return movimiento_depredador(matriz, i, j)

def evolucion(matriz: list[list[Animal | Alimento | None]], i: int = 0, j: int = 0, simulaciones: int = 0):
  if i == len(matriz):
    return None
  if j == len(matriz[0]):
    return evolucion(matriz, i + 1, 0, simulaciones)

  if simulaciones % 5 == 4:
    num = random.randint(1, 10)
    if num == 1:
      matriz[i][j] = Alimento()

  if isinstance(matriz[i][j], Presa):
    direccion = random.randint(1, 8)
    movimiento_presa(matriz, direccion, i, j)
    return evolucion(matriz, i, j + 1, simulaciones)

  if isinstance(matriz[i][j], Depredador):
    movimiento_depredador(matriz, i, j)
    return evolucion(matriz, i, j + 1, simulaciones)

  if isinstance(matriz[i][j], Alimento):
    matriz[i][j].reducir_energia()
    if matriz[i][j].energia == 0:
      matriz[i][j] = None
    return evolucion(matriz, i, j+1, simulaciones)

  return evolucion(matriz, i, j + 1, simulaciones)

def imprimir_matriz(matriz: list[list[Animal | Alimento | None]], i: int = 0, j: int = 0, fila: list[str] = []):
  if i == len(matriz):
    return None
  if j == len(matriz):
    print(fila)
    return imprimir_matriz(matriz, i+1, 0, [])

  if isinstance(matriz[i][j], Animal):
    matriz[i][j].movimiento = False

  if matriz[i][j] is not None:
    fila.append(str(matriz[i][j]))
    return imprimir_matriz(matriz, i, j+1, fila)

  fila.append(" ")
  return imprimir_matriz(matriz, i, j+1, fila)

def sin_organismos_vivos(matriz: list[list[Animal | Alimento | None]], i: int = 0, j: int = 0, cont: int = 0) -> int:
  if i == len(matriz):
    return cont
  if j == len(matriz):
    return sin_organismos_vivos(matriz, i+1, 0, cont)

  if matriz[i][j] is None:
    return sin_organismos_vivos(matriz, i, j+1, cont+1)

  return sin_organismos_vivos(matriz, i, j+1, cont)

def simulacion(matriz: list[list[Animal | Alimento | None]], sim: str = "", index: int = 0):
  if index == 100:
    print("Límite de iteraciones alcanzado.")
    return None
  if sin_organismos_vivos(matriz, 0, 0, 0) == len(matriz)**2:
    print("No quedan organismos vivos.")
    return None
  if sim == "":
    sim = input("¿Continuar simulación? (Y/N): ").upper()
  if sim == "N":
    print("Simulación terminada.")
    return None
  if sim != "Y":
    return simulacion(matriz, "", 0)

  evolucion(matriz, simulaciones=index)
  imprimir_matriz(matriz, 0, 0, [])
  return simulacion(matriz, "", index+1)


if __name__ == "__main__":
  m = generar_matriz(5)
  imprimir_matriz(m, 0, 0, [])
  simulacion(m, "", 0)