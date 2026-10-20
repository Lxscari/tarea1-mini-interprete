"""De los tokens al AST.

La gramatica que reconoce este parser es:

    expresion := termino  (('+' | '-') termino)*
    termino   := factor   (('*' | '/') factor)*
    factor    := NUMERO | '(' expresion ')'

Los tres niveles son lo que hace que  3 + 4 * 2  se agrupe como  3 + (4 * 2)
y no como  (3 + 4) * 2 : la multiplicacion vive un nivel mas abajo, asi que
se arma primero.
"""

from .ast import Numero, OperacionBinaria
from .errores import ErrorDeSintaxis
from .tokens import TipoToken

OPERADORES_SUMA = (TipoToken.MAS, TipoToken.MENOS)
OPERADORES_PRODUCTO = (TipoToken.POR, TipoToken.ENTRE)


class Parser:

    def __init__(self, tokens: list):
        self.tokens = tokens
        self.pos = 0

    def parsear(self):
        """Construye el AST de la lista de tokens."""
        return self._expresion()

    def _actual(self):
        """El token en la posicion actual, o None si ya no quedan."""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def _avanzar(self):
        """Consume el token actual y lo regresa."""
        token = self._actual()  #es mas facil utilizar la funcion _actual en ves de repetir codigo
        if token is None: #esto namas salta si no quedan tokens 
            posicion = self.tokens[-1].posicion + 1 if self.tokens else 0   #este if / else es el que nos maneja el caso de que sea vacia no hay token y la posicion es 0
            raise ErrorDeSintaxis("La expresion termino antes de tiempo", posicion)
        self.pos += 1
        return token

    def _expresion(self):
        return self._operaciones_en_cadena(
            siguiente_nivel=self._termino,
            operadores=OPERADORES_SUMA,
        )

    def _termino(self):
        return self._operaciones_en_cadena(
            siguiente_nivel=self._factor,
            operadores=OPERADORES_PRODUCTO,
        )

    def _operaciones_en_cadena(self, siguiente_nivel, operadores):
        izquierda = siguiente_nivel()
        while True:
            actual = self._actual()
            if actual is None or actual.tipo not in operadores:
                break
            operador = self._avanzar()
            derecha = siguiente_nivel()
            izquierda = OperacionBinaria(operador.valor, izquierda, derecha)
        return izquierda

    def _factor(self):
        token = self._avanzar()

        if token.tipo == TipoToken.NUMERO:
            return Numero(token.valor)

        if token.tipo == TipoToken.PAR_IZQ:
            nodo = self._expresion()
            cierre = self._avanzar()
            if cierre.tipo != TipoToken.PAR_DER:
                raise ErrorDeSintaxis("se esperaba ')'", cierre.posicion)
            return nodo

        raise ErrorDeSintaxis(f"token inesperado {token.valor!r}", token.posicion)
