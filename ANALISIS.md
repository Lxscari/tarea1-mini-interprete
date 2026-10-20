# Análisis — Tarea 1

**Integrantes:**
1.Arely Ramirez Espejel
2. Gael Alonso Barajas Lascari
3.  -

**Fork:**
**Rama:**

> Contesten en este archivo. Respuestas breves y concretas: se califica que
> hayan entendido, no la extensión.

---

## 1. Arquitectura

### 1.1 ¿Cuál es la responsabilidad de cada componente?

| Componente | Qué recibe | Qué entrega | De qué es responsable |
|---|---|---|---|
| `lexer` | Una cadena de texto con una expresion | Una lista de Tokens | Reconoce los numeros, operadores y los simbolos validos |
| `parser` | Una lista de tokens | Un AST  | Comprueba la estructura de la expresion dada en lexer y apartir de ella construye un AST respetando las reglas |
| `ast` | Datos necesarios para representar una expresion  | Nodos que representan una expresion  | Define la estructura del arbol y la relacion entre los nodos |
| `evaluator` | El AST | Un resultado numerico | Recorre el arbol y nos da el valor de la expresion |

### 1.2 ¿Qué recorrido sigue una expresión desde que se recibe como texto hasta que produce un resultado?

> Usen `(3 + 4) * 2` como ejemplo y muestren cómo se ve entre etapa y etapa.

| Etapa | Cómo se ve `(3 + 4) * 2` aquí |
|---|---|
| texto | `"(3 + 4) * 2"` |
| tokens | [PAR_IZQ, NUMERO(3), MAS, NUMERO(4), PAR_DER, POR, NUMERO(2)] |
| AST | Nodo POR con un nodo MAS a la izquierda (3 + 4) y a la derecha 2 |
| resultado | 14 |

> Para el renglón del AST, dibújenlo **primero ustedes** y después comprueben
> con `python3 interprete.py --arbol "(3 + 4) * 2"`. Si su dibujo y el del
> programa no coinciden, uno de los dos está mal, y averiguar cuál es
> justamente el trabajo.

---

## 2. Las pruebas que ya estaban

### 2.1 ¿Qué pruebas venían incluidas?

| Prueba | Componente | Comportamiento que verifica | ¿Cuántos operadores usa? | ¿Normal, frontera o inválida? |
|---|---|---|---|---|
| test_suma | Evaluator | Verifica que 3 + 4 = 7 | 1 | Normal |
| test_resta | Evaluator | Verifica que 10 - 3 = 7 | 1 | Normal |
| test_multiplicacion | Evaluator | Verifica 6 * 7 = 42 | 1 | Normal |
| test_divsion | Evaluator | Verifica que 10 / 2 = 5 | 1 | Normal |
| test_precedencia_sin_parentesis | Evaluator | Verifica que la multiplicación se realice antes que la suma | 2 | Normal |
| test_precedencias_con_parentesis | Evaluator | Verifica que los parentesis cambian el orden de operación | 2 | Normal |
| test_contruye_el_arbol_de_una_suma | Parser | Verifica que se contruya correctamente el AST de una suma | 1 | Normal |
| test_la_multiplicacion_se_agrupa_antes_que_la_suma | Parser | Verifica que se construya el arbol respetando la precedencia | 2 | Normal |
| test_los_parentesis_cambian_la_agrupacion | Parser | Verifica que se construya el AST de acuerdo a los parentesis | 2 | Normal |
| test_tokeniza_un_solo_numero | Lexer | Reconoce un numero sin operadores | 0 | Frontera |
| test_tokeniza_una_suma | Lexer | Convierte una suma en tokens con sus posiciones | 1 | Normal |
| test_los_espacios_no_producen_tokens | Lexer | Ignora los espacios al tokenizar | 1 | Frontera |
| test_tokeniza_parentesis | Lexer | Reconoce los parentesis y el número | 0 | Normal |


### 2.2 ¿Qué comportamientos **no** estaban probados?

> Ninguna entrada inválida: No hay una sola prueba con ErrorDeSintaxis
> ni ErrorDeEvaluacion, aunque la sección 7 (README) exige que toda entrada inválida
> se rechace con ErrorDeSintaxis y nunca con un error de Python que truene  el programa. En
> si no se probaba:
> un carácter desconocido (3 # 4),
> una expresión incompleta (3 +),
> la entrada vacía (""),
> paréntesis sin cerrar ((3 + 4) o de más ((3 + 4))),
> dos números sin operador (3 4),
> el menos unario (-3).
> La asociatividad: Nunca aparecen dos operadores de la misma precedencia
> seguidos (10 - 3 - 2, 8 / 4 / 2), así que no se comprobaba que se
> agruparan a la izquierda.
> La división entre cero, que debe dar ErrorDeEvaluacion.
> La división real. test_division usa 10 / 2 == 5, y eso pasa
> aunque el resultado fuera el entero 5. Nunca se prueba un caso como10 / 4 = 2.5.
> La posición en los mensajes de error. La sección 7 del README la pide segun las reglas de sintaxis, pero
> ninguna prueba revisa la posición de un error.
> Los ceros a la izquierda (007 es 7), declarados en la sección 7 del README.

---

## 3. Las pruebas que agregaron

### 3.1 ¿Cuáles son casos normales, cuáles frontera y cuáles inválidos?

| Prueba (archivo::nombre) | Entrada | Esperado | Categoría | ¿Por qué esa categoría? |
|---|---|---|---|---|
| test_la_resta_se_agrupa_de_izquierda_a_derecha (test_parser.py) | 10 - 3 - 2 | AST equivalente a (10 - 3) - 2 | Frontera | Porque comprueba la asociatividad cuando se encadenan operadores de la misma precedencia |
| test_division_encadenada (test_evaluator.py) | 8 / 4 / 2 | 1 | Frontera | Comprueba la asociatividad de la division encadenanda|
| test_numeros_con_ceros_inciales (test_evaluator.py) | 007 + 2 | 9 | Frontera | Comprueba que los 0 iniciales no cambian el valor numerico |
| test_jerarquia (test_evaluator.py) | 3 + 4 * 2 - 1 | 10 | Normal | Comprueba la precedencia en una expresión con varios operadores |
| test_division_real (test_evaluator.py) | 10 / 4 | 2.5 | Normal | Comprueba que la división produce resultados reales |
| test_multiples_espacios (test_evaluator.py) | 3  +  4 | 7 | Frontera | Comprueba que los espacios en las expresiones no afecten el resultado |
| test_division_entre_cero (test_evaluator.py) | 10 / 0 | Lanzar ErrorDeEvaluacion | Inválida | La sintaxis si es valida, pero la operacion no se puede realizar  |
| test_posicion_caracter_invalido (test_invalidos.py) | 3 # 4 | Lanzar ErrorDeSintaxis | Inválida | El caracter # no está permitido |
| test_menos_unario_invalido (test_invalidos.py) | -3 | Lanzar ErrorDeSintaxis | Inválida | El signo menos unario no forma parte de la sintaxis |
| test_expresion_incompleta (test_invalidos.py) | 3 +  | Lanzar ErrorDeSintaxis | Inválida | Falta un operando después del operador |
| test_entradavacia (test_invalidos.py) | "" | Lanzar ErrorDeSintaxis | Inválida | No hay expresión que analizar |
| test_parentesis_sincerrar (test_invalidos.py) | (3 + 4 | Lanzar ErrorDeSintaxis | Inválida | Falta un parentesis de cierre|

---

## 4. Los defectos

### 4.1 ¿Qué defecto reveló primero una prueba nueva?
> El primero fue que el lexer ignoraba los caracteres que no reconocía o mejor dicho invalidos.
> La prueba test_invalidos::test_caracter_invalido (commit cae16a0) usa la
> entrada 3 # 4, que debería rechazarse o tirar , pero el intérprete regresaba 3
> sin dar ningún error.

> El lexer saltaba el # en silencio y producía los tokens [NUMERO(3), NUMERO(4)].
> Después el parser armaba el árbol con el 3, dejaba el 4 sin usar.  O sea que esta prueba destapó dos defectos a la vez:
> uno en el lexer (ignorar caracteres) y otro en el parser (ignorar tokens
> sobrantes).

### 4.2 ¿Por qué el comportamiento observado era incorrecto?

> Al revisar el programa, encontramos varios defectos que hacían que algunas expresiones no se procesaran correctamente. 
>Primero, cuando escribíamos una expresión con un carácter inválido, como 3 # 4, el programa devolvía 3 en lugar de
> lanzar un ErrorDeSintaxis, como establece la sección 7 del README.
> También encontramos un problema con la asociatividad de los operadores. Por ejemplo, 10 - 3 - 2 daba 9, porque el
> programa agrupaba la expresión como 10 - (3 - 2), cuando debería evaluarla de izquierda a derecha: (10 - 3) - 2, cuyo
> resultado es 5. Este error no se notaba con la suma o la multiplicación, porque cambiar el orden de agrupación no modifica
> el resultado en esos casos; sí se hace evidente con la resta y la división.
> Además, descubrimos que algunas entradas incompletas o mal formadas provocaban errores internos de Python en lugar de los
> errores que debía manejar el intérprete. Por ejemplo, las expresiones 3 +, una entrada vacía ("") y (3 + 4 provocaban un
> IndexError. Esto incumple la regla que establece que las entradas inválidas deben rechazarse mediante ErrorDeSintaxis, nunca
> mediante una excepción interna de Python.
> Por último, encontramos que el programa aceptaba expresiones con tokens sobrantes. Por ejemplo, 3 4 devolvía 3 y (3 + 4))
> devolvía 7, ignorando la parte sobrante de la entrada. Esto también incumple la regla de que las expresiones inválidas deben
> rechazarse con ErrorDeSintaxis, ya que el intérprete debería comprobar que toda la entrada se haya procesado correctamente. 

### 4.3 ¿Qué cambio realizaron?

| Defecto | Entrada que lo revela | Daba | Debería dar | Commit rojo | Commit verde |
|---|---|---|---|---|---|
| Caracteres inválidos ignorados | 3 # 4 | 3 | ErrorDeSintaxis | cae16a0 | 4efa3e0 |
| Asociatividad a la derecha | 10 - 3 - 2 | 9 | 5 | d81c73d | bee9f6b |
| Expresion incompleta | 3 + | IndexError | ErrorDeSintaxis | 85ae49f | d336851 |
| Entrada vacía | "" | IndexError | ErrorDeSintaxis | 72e9d7b | d336851 |
| Parentesis sin cerrar | (3 + 4 | IndexError | ErrorDeSintaxis | 0021cbf | d336851 |
| Tokens sobrantes | 3 4 | 3 | ErrorDeSintaxis | 0393001 | 589f75b |
| Tokens sobrantes | (3 + 4)) | 7 | ErrorDeSintaxis | 0393001 | 589f75b |

### 4.4 ¿Cómo saben que la corrección es general y no sólo hace pasar ese ejemplo?
> Las correcciones son generales porque solucionan la causa de los errores, no sólo los ejemplos que encontramos. 
> El lexer ahora rechaza cualquier carácter inválido, _avanzar() evita que el parser genere un IndexError cuando 
> faltan tokens y parsear() detecta si quedan tokens sin procesar.
> También corregimos la asociatividad de la suma, resta, multiplicación y división para que las operaciones del 
> mismo nivel se resuelvan de izquierda a derecha. Lo comprobamos con pruebas como 10 - 3 - 2 = 5 y 8 / 4 / 2 = 1.0.
> Por último, verificamos que las 13 pruebas originales siguieran pasando y agregamos pruebas para comprobar que los
> errores se detectaran correctamente, incluida la posición del carácter inválido. Así confirmamos que los cambios
> corrigen los defectos sin alterar el comportamiento que ya funcionaba. 

---

## 5. Diseño

### 5.1 ¿Qué duplicación o señal de mal diseño encontraron?

> Encontramos una duplicación entre _expresion() y _termino(), porque ambos metodos contaban con codigo que hacía practicamente
> lo mismo, al tener esta logica repetida, si se necesitara cambiar, se tendría que cambiar en ambos metodos.
> Otra cosa fue que si se necesitara agregar otro operador, se tendrian que modificar varios archivos, lo que requiere realizar varios cambios y 
> aumentar el esfuerzo de mantenimiento.

### 5.2 ¿Qué refactorización realizaron, y por qué conserva el comportamiento?

> Se refactorizo el parser para eliminar la duplicación que había entre _expresion() y _termino().
> Se creo el método _operaciones_en_cadena(), el cual recibe la función del siguiente nivel de análisi 
> y operadores permitidos.
> Se sigue conservando el comportamiento, ya que el nuevo método creado realiza los mismos pasos que se realizaban 
> en _expresion() y _termino(), pero cada uno sigue analizando sus propios operadores.

### 5.3 ¿Sería pertinente usar Factory Method, Adapter o ninguno?

> No seria necesario niguno, ya que en este caso no se tienen distintas formas para crear objetos, ni tampoco se busca conectar 
> componentes de distintas interfaces, como seria el caso de Factory Method y Adapter respectivamente. Solo complicarian un poco
> el codigo sin aportar ventaja alguna. Pero se podrían adaptar si se viera una necesidad a futuro.  

### 5.4 ¿Qué parte del sistema sería más difícil de modificar si se agregara un operador nuevo?

> Se tendrían que realizar varios cambios en todo el código, se tendría que agregar el operador en lexer para que lo reconozca, definir
> la manera en el que parser lo procesara y su nivel de procedencia, y agregar sus operaciones en evaluator. Al igual que realizar sus
> pruebas respectivas.

---

## Antes de la declaración: inténtenlo primero ustedes

Usar IA o no es decisión de cada quien, y el curso la permite. Pero **les
pedimos, por favor, que primero hagan el análisis por su cuenta.**

No es una prueba de honestidad. Es que el orden cambia lo que aprenden:

1. **Primero ustedes.** Lean el código, corran las pruebas, escriban sus
   respuestas. Aunque queden incompletas, aunque no encuentren todo.

2. **Después, si quieren, la IA** — pero como contraste, no como sustituto.
   Y entonces contesten dos preguntas, en `DECLARACION_IA.md`:

   - **¿Qué encontró que ustedes no habían notado?**
     Eso es aprendizaje, y se declara sin ninguna pena.

   - **¿Qué *no* encontró, que en este curso sí consideramos un problema?**
     Ésta es la interesante. Una herramienta suele decir que el código
     "funciona bien" y no señalar, por ejemplo, la **duplicación** — porque
     duplicar no rompe nada, el programa corre igual. Pero ustedes ya saben
     por qué eso sí es un mal diseño, y saben nombrarlo. La herramienta no
     tomó esa clase.

> Si invierten el orden se pierden justamente lo segundo: **no se puede notar
> lo que a una herramienta le faltó si uno nunca se formó una opinión propia
> antes de preguntarle.** Y que un programa funcione no implica que esté bien
> diseñado — eso lo dijimos en clase mucho antes de esta tarea.

---

## Declaración de uso de Inteligencia Artificial

Va en `DECLARACION_IA.md`, no aquí. Es obligatoria, pero **no da ni quita
puntos**: es un reporte adicional que se revisa aparte y se les devuelve con
comentarios.

**No se evalúa cuánta IA usaron.** Se evalúa si pueden dar cuenta de lo que
entregaron. *"No usamos"* es una declaración válida y completa; *"lo
descartamos porque..."* es de las mejores respuestas posibles.
