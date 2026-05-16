def converter_nota_para_para_conceito( nota: float):
    if nota <0.0 or nota > 10.1:
        return 'Nota inválida'
    elif nota < 3.0:
        return 'F'
    elif nota <= 4.9:
        return 'D'
    elif nota <= 6.9:
        return 'C'
    elif nota < 8.9:
        return 'B'
    elif nota <= 10.0:
        return 'A'
        