"""Pruebita de caracteres invalidos, debe de recharazarlos por parte del programa (usando Error) 
y no crashear o mandar error directo de python """
import pytest

from mini_interprete.cli import interpretar
from mini_interprete.errores import ErrorDeSintaxis #Importamos el Error de sintaxis para que sea el error lanzado y no el de pythin

def test_caracter_invalido():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("3 # 4")

def test_posicion_caracter_invalido():  #Checa que la posicion del caracter invalido efectivamente sea la 2 o la del operador
    with pytest.raises(ErrorDeSintaxis) as error:
        interpretar("3 # 4")
    assert error.value.posicion == 2

def test_menos_unario_invalido():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("-3")

def test_expresion_incompleta():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("3 +")

def test_entradavacia():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("")

def test_parentesis_sincerrar():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("(3 + 4")

def test_dos_numeros_sin_operador():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("3 4")

def test_parentecis_extra():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("(3 + 4))")