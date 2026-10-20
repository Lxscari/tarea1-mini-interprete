"""Pruebas del evaluador: del AST a un numero."""

import pytest
from mini_interprete.cli import interpretar
from mini_interprete.errores import ErrorDeEvaluacion

def test_suma():
    assert interpretar("3 + 4") == 7


def test_resta():
    assert interpretar("10 - 3") == 7


def test_multiplicacion():
    assert interpretar("6 * 7") == 42


def test_division():
    assert interpretar("10 / 2") == 5


def test_precedencia_sin_parentesis():
    assert interpretar("3 + 4 * 2") == 11


def test_precedencia_con_parentesis():
    assert interpretar("(3 + 4) * 2") == 14


def test_division_encadenada():
    assert interpretar("8 / 4 / 2") == 1.0


def test_division_real():
    assert interpretar("10 / 4") == 2.5


def test_numeros_con_ceros_inciales():
    assert interpretar("007 + 2") == 9


def test_jerarquia():
    assert interpretar("3 + 4 * 2 - 1") == 10


def test_multiples_espacios():
    assert interpretar("3   +   4") == 7


def test_division_entre_cero():
    with pytest.raises(ErrorDeEvaluacion):
        interpretar("10 / 0")