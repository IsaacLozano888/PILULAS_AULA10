
from a10_ex5 import aplicar_cupom

def test_cupom10_valido():
    assert aplicar_cupom("CUPOM10", 50.0) == 0.10
    assert aplicar_cupom("cupom10", 50.0) == 0.10  
    assert aplicar_cupom("CupOm10", 50.0) == 0.10

def test_cupom25_valido():
    assert aplicar_cupom("CUPOM25", 150.0) == 0.25
    assert aplicar_cupom("cupom25", 150.0) == 0.25

def test_cupom25_invalido_valor_baixo():
    assert aplicar_cupom("CUPOM25", 50.0) == 0.0
    assert aplicar_cupom("CUPOM25", 100.0) == 0.0  

def test_descontovip_valido():
    assert aplicar_cupom("DESCONTOVIP", 600.0) == 0.35
    assert aplicar_cupom("descontovip", 600.0) == 0.35

def test_descontovip_invalido_valor_baixo():
    assert aplicar_cupom("DESCONTOVIP", 400.0) == 0.0
    assert aplicar_cupom("DESCONTOVIP", 500.0) == 0.0  

def test_cupom_invalido():
    assert aplicar_cupom("CUPOM_FALSO", 1000.0) == 0.0
    assert aplicar_cupom("", 100.0) == 0.0