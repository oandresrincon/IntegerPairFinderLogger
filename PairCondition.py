def encontrar_parejas(limit):
    for a in range(2, limit):
        for b in range(2, limit):
            if (a - 1) % (3 * b - 1) == 0 and (b - 1) % (3 * a - 1) == 0:
                print(f"Pareja encontrada: a = {a}, b = {b}")

limite_superior = 1000  # Puedes ajustar este límite según tus necesidades
encontrar_parejas(limite_superior)
