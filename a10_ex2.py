def calcular_frete(peso_kg: float):
    if peso_kg <= 0.00:
        return 0.00
    elif peso_kg <= 1.00:
        return 5.00
    elif peso_kg <= 5.00:
        return 10.00
    else:
        return 18.00

