import pytest  # Se imoprta para usar parametrización
from measure_area import me_area  # le damos la dirección donde
# está lo que vamos a probar


@pytest.mark.parametrize(  # primero parametrizamos para probar la
        # verificación de un integer.
        "input, expect",
        [
            (4, True),  # con un número simple
            ("10", True),  # un string de número
            ("a", False),  # un caracter
            ("2.5", False)  # y uno de una fracción
        ]
)
def test_integer(input, expect):  # Prueba si es entero o no y
    # compara con lo esperado.
    assert me_area.measure(input) == expect


@pytest.mark.parametrize(  # Parametriza para varios tests
        "input_a, expected",
        [
            (4, (16, 50.2656)),  # uno sencillo con 4
            ("2.5", "ERR3"),  # un string de una fracción
            ("10", (100, 314.16)),  # uno de 10
            ("a", "ERR3"),  # una letra
            ("1", (1, 3.1416)),  # un uno
            ("0", (0, 0))  # si alguien se quiere poner creativo poniendo 0
        ]
)
def test_measure(input_a, expected):  # Prueba si las salidas de área
    # de cuadrado y círculo son correctas
    # o si retorna el error
    assert me_area.measure_area(input_a) == expected

from measure_area import divide
def divide_string(frase, op):
#  Debe verificar que el parámetro frase sea un string. En caso de no cumplir 
#  esta limitación el código retorna un código de error único

    if not type(frase) == str:
        return "ERR1", "ERR1", "ERR1" #  ERR1 es: No ingresó un string como frase
        #  Siempre se retornan 3 variables: código de error, primera string, segunda string.
        #  Debe verificar que el parámetro operación sea un número entero. 
        # En caso de no cumplir esta limitación el código retorna un código de error único

    if not type(op)==int and not(op==1 or op==2):
        return "ERR2", "ERR2", "ERR2" 
    #  ERR2 es "No se ingresó un entero válido como operación." 
    #  Siempre se retornan 3 variables: código de error, primera string, segunda string.
    string1=""
    string2=""
# Parámetro Operación 1: Separa las mayúsculas de las minúsculas de la string generando dos strings.
# Todo número pertenece a las mayúsculas, todo carácter no alfanumérico pertenece a las minúsculas.

    if op == 1:
        for i in frase:
            if i in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890":
                string1+=i
            else: string2+=i
        return "ALLOK", string1, string2
#  Siempre se retornan 3 variables: código de error, primera string, segunda string.
#  Parámetro Operación 2: Divide la string por la mitad, en caso de caracteres impares
#  la primera mitad tendrá la mayor cantidad de caracteres.

    if op==2:
        if op==2:
            if len(frase) % 2 == 0:
                string1 = frase[0:len(frase)//2]
                string2 = frase[len(frase)//2:]
            else:
                string1 = frase[0:(len(frase)//2+1)]
                string2 = frase[(len(frase)//2+1):]
                return "ALLOK", string1, string2


def test_op():
    assert divide.divide_string("D1e2a3d#4B5e6e7f8$!", 1) == ("ALLOK", "D1234B5678", "ead#eef$!")
    assert divide.divide_string("D1e2a3d#4B5e6e7f8$!", 2) == ("ALLOK", "D1e2a3d#4B", "5e6e7f8$!")


def test_ERR1():
    assert divide.divide_string(0, 1) == ("ERR1", "ERR1", "ERR1")
# Una prueba que verifica que el método 
# divide_string retorna el error correcto si
# se le pasa algo distinto de un número entero como entrada del segundo
# parámetro.

def test_ERR2():
    assert divide.divide_string("D1e2a3d#4B5e6e7f8$!", "a") == ("ERR2", "ERR2", "ERR2")
