from a10_ex3 import converter_nota_para_para_conceito

def test_nota_Inválida():
    assert converter_nota_para_para_conceito(-0.1) == 'Nota inválida'
    assert converter_nota_para_para_conceito(-1.0) == 'Nota inválida'
    assert converter_nota_para_para_conceito(-5.0) == 'Nota inválida'
    i = 10.01
    while i < 0.0:
        assert converter_nota_para_para_conceito(i) == 'Nota inválida'
        i += 0.01

def test_nota_F():
    i = 0.0
    while i < 3.0:
        assert converter_nota_para_para_conceito(i) == 'F'
        i += 0.01

def test_nota_D():
    i = 3.0
    while i < 4.9:
        assert converter_nota_para_para_conceito(i) == 'D'
        i += 0.01

def test_nota_C():
    i = 5.0
    while i < 6.9:
        assert converter_nota_para_para_conceito(i) == 'C'
        i += 0.01

def test_nota_B():
    i = 7.0
    while i < 8.9:
        assert converter_nota_para_para_conceito(i) == 'B'
        i += 0.01

def test_nota_A():
    i = 9.0
    while i <= 10.0:
        assert converter_nota_para_para_conceito(i) == 'A'
        i += 0.01

    
    
    


