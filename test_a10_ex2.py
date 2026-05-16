from a10_ex2 import calcular_frete 

def test_peso_1():
    i = 0.01
    while i <= 1.0:
        assert calcular_frete(i) == 5.00
        i += 0.01

def test_peso_2():
    i = 1.01
    while i <= 5.00:
        assert calcular_frete(i) == 10.00
        i += 0.01

def test_peso_3():
    i = 5.01
    while i <= 100.0:  
        assert calcular_frete(i) == 18.00
        i += 0.01

def test_peso_zero_e_negativo():
    assert calcular_frete(0.0) == 0.00
    assert calcular_frete(-0.1) == 0.00
    assert calcular_frete(-1.0) == 0.00
    assert calcular_frete(-5.0) == 0.00
    
        