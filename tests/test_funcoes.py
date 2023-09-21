import pytest
from ..db.db_utils import cadastra_usuario, busca_usuario, busca_usuarios, atualiza_usuario


# Cadastra usuario
@pytest.mark.simples
def test_cadastra_usuario_idade():
    assert cadastra_usuario('Gabriel', 30, '12345678910', 'Rua X', 'gabrielfmendesm@gmail.com') == True

@pytest.mark.simples
def test_cadastra_usuario_idade_incorreta():
    assert cadastra_usuario('Gabriel', -1, '12345678910', 'Rua X', 'gabrielfmendesm@outlook.com') == False
    assert cadastra_usuario('Gabriel', 121, '12345678910', 'Rua X', 'gabrielfmendesm@outlook.com') == False

@pytest.mark.simples
def test_cadastra_usuario_cpf():
    assert cadastra_usuario('Gabriel', 30, '12345678910', 'Rua X', 'gabrielfmendesm@outlook.com') == True

@pytest.mark.simples
def test_cadastra_usuario_cpf_tamanho():
    assert cadastra_usuario('Gabriel', 30, '123456789101', 'Rua X', 'gabrielfmendesm@outlook.com') == False

@pytest.mark.simples
def test_cadastra_usuario_email():
    assert cadastra_usuario('Gabriel', 30, '12345678910', 'Rua X', 'gabrielfmendesm@outlook.com') == True

@pytest.mark.simples
def test_cadastra_usuario_email_formato():
    assert cadastra_usuario('Gabriel', 30, '12345678910', 'Rua X', 'gabrielfmendesmoutlook.com') == False



# Busca usuario
@pytest.mark.simples
def test_busca_usuario():
    usuario = busca_usuario(1)
    assert usuario is not None

@pytest.mark.simples
def test_busca_usuario_inexistente():
    assert busca_usuario(-1) == None
    assert busca_usuario(1000) == None



# Busca usuarios
@pytest.mark.lista
def test_busca_usuarios():
    usuarios = busca_usuarios()
    assert len(usuarios) > 0




# Atualiza usuario
@pytest.mark.simples
def test_atualiza_usuario_idade():
    assert atualiza_usuario(1, 'Gabriel', 30, '12345678910', 'Rua X', 'gabrielfmendesm@outlook.com') == True

@pytest.mark.simples
def test_atualiza_usuario_idade_incorreta():
    assert atualiza_usuario(1, 'Gabriel', -1, '12345678910', 'Rua X', 'gabrielfmendesm@outlook.com') == False
    assert atualiza_usuario(1, 'Gabriel', 121, '12345678910', 'Rua X', 'gabrielfmendesm@outlook.com') == False

@pytest.mark.simples
def test_atualiza_usuario_cpf_tamanho():
    assert atualiza_usuario(1, 'Gabriel', 30, '12345678910', 'Rua X', 'gabrielfmendesm@outlook.com') == True

@pytest.mark.simples
def test_atualiza_usuario_cpf_tamanho():
    assert atualiza_usuario(1, 'Gabriel', 30, '123456789101', 'Rua X', 'gabrielfmendesm@outlook.com') == False

@pytest.mark.simples
def test_atualiza_usuario_email():
    assert atualiza_usuario(1, 'Gabriel', 30, '12345678910', 'Rua X', 'gabrielfmendesm@outlook.com') == True

@pytest.mark.simples
def test_atualiza_usuario_email_formato():
    assert atualiza_usuario(1, 'Gabriel', 30, '12345678910', 'Rua X', 'gabrielfmendesmoutlook.com') == False
