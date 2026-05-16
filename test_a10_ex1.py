from a10_ex1 import acao_semaforo

def test_cor_vermelho():
    assert acao_semaforo('vermelho') == 'Pare'
    
def test_cor_amarelo():
    assert acao_semaforo('amarelo') == 'Atenção'

def test_cor_verde():
    assert acao_semaforo('verde') == 'Siga'

def test_cor_invalida():
    # for i not in 'vermelho' or 'v'
    assert acao_semaforo(not  'vermelho') == 'Cor Inválida'
    assert acao_semaforo(not  'amarelo') == 'Cor Inválida'
    assert acao_semaforo(not  'verde') == 'Cor Inválida'