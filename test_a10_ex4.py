from a10_ex4 import calcular_bonus

def test_bonus_bom():
    assert calcular_bonus(1000.0, "Bom") == 100.0

def test_bonus_excelente():
    assert calcular_bonus(1000.0, "Excelente") == 200.0

def test_bonus_regular():
    assert calcular_bonus(1000.0, "Regular") == 20.0

def test_bonus_salario_negativo():
    assert calcular_bonus(-500.0, "Bom") == 0.0

def test_bonus_avaliacao_invalida():
    assert calcular_bonus(1000.0, "Mais ou Menos") == 0.0
    assert calcular_bonus(1000.0, "Ruim") == 0.0
    assert calcular_bonus(1000.0, "") == 0.0