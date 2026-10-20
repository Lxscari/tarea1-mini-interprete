"""Pruebita de caracteres invalidos, debe de recharazarlos por parte del programa (usando Error) 
y no crashear o mandar error directo de python """
import pytest

from mini_interprete.cli import interpretar
from mini_interprete.errores import ErrorDeSintaxis #Importamos el Error de sintaxis para que sea el error lanzado y no el de pythin

def test_caracter_invalido():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("3 # 4")
