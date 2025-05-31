import random


def gen_pares(n):
    matriz = []
    for _ in range(n):
        x = random.randint(-81, 81)
        y = random.randint(-81, 81)
        matriz.append([x, y])
    return matriz


def filtrar(pares):
    resultado = []
    for p in pares:
        if p[0] > 0 and p[1] < 0:
            resultado.append(p)
    return resultado


#pitagoras
def dist(p):
    return (p[0]**2 + p[1]**2)**0.5


def max_dist_divide_vence(pares):
    if len(pares) == 1:
        return pares[0]
    elif len(pares) == 0:
        return None

    mitad = len(pares) // 2

    izq = []
    for i in range(mitad):
        izq.append(pares[i])

    der = []
    for i in range(mitad, len(pares)):
        der.append(pares[i])

    izquierda = max_dist_divide_vence(izq)
    derecha = max_dist_divide_vence(der)

    if izquierda is None:
        return derecha
    if derecha is None:
        return izquierda
    
    if dist(izquierda) >= dist(derecha):
        return izquierda
    else:
        return derecha

def main():
    n = int(input("Ingrese la cantidad de pares: "))
    matriz = gen_pares(n)

    print("\nCoordenadas generadas:")
    for p in matriz:
        print(p)

    pares_filtrados = filtrar(matriz)
    if len(pares_filtrados) == 0:
        print("\nNo se encontraron coordenadas con valor  positivo en X y negatvo en Y.")
        return

    mas_lejana = max_dist_divide_vence(pares_filtrados)

    print(f"\nLa coordenada más alejda del origen (0,0) que tiene X positivo e Y negativo es: {mas_lejana}")
    print(f"Distancia: {dist(mas_lejana):.2f}")

if __name__ == "__main__":
    main()
