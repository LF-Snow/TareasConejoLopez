class me_area:  # Para que sea método se mete en la class me_area

    def measure(r):  # Verifica si r es entero y retorna 1 si lo es
        try:
            int(r)
        except ValueError:  # En caso ValueError no es entero, retorna 0
            return False
        return True

    def measure_area(r):  # método para medir el área o dar error
        if me_area.measure(r):  # Si es entero entra y calcula
            cuad = int(r)*int(r)  # Mult como int
            circ = 3.1416*cuad
            circ = round(circ, 4)  # Lo redondea por comodidad
            return (cuad, circ)
        else:  # Si NO es entero, retorna este error único
            return ("ERR3")  # Caracter inválido / no es entero


class divide:

    def divide_string(frase, op):
        if not type(frase) == str:  # Debe verificar que frase sea string.
            return "ERR1", "ERR1", "ERR1"
            # ERR1 es "No se ingresó un string como frase.".
            # Siempre se retornan 3 variables:
            # código de error,
            # primera string,
            # segunda string.

    # Debe verificar que el parámetro operación sea un número entero.
    # En caso de no cumplir esta limitación
    # el código retorna un código de error único

        if not type(op) == int and not (op == 1 or op == 2):
            return "ERR2", "ERR2", "ERR2"
            # ERR2 es "No se ingresó un entero válido como operación."
            # Siempre se retornan 3 variables:
            # código de error,
            # primera string,
            # segunda string.
        string1 = ""
        string2 = ""
    # Parámetro Operación 1: Separa las mayúsculas de las
    # minúsculas de la string generando dos strings.
    # Todo número pertenece a las mayúsculas,
    # todo carácter no alfanumérico pertenece a las minúsculas.
        if op == 1:
            for i in frase:
                if i in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890":
                    string1 += i
                else:
                    string2 += i
            return "ALLOK", string1, string2
            # Siempre se retornan 3 variables: código de error,
            # primera string, y segunda string
    # Parámetro Operación 2: Divide la string por la mitad,
    # en caso de caracteres impares
    # la primera mitad tendrá la mayor cantidad de caracteres.
        if op == 2:
            if op == 2:
                if len(frase) % 2 == 0:
                    string1 = frase[0:len(frase)//2]
                    string2 = frase[len(frase)//2:]
                else:
                    string1 = frase[0:(len(frase)//2+1)]
                    string2 = frase[(len(frase)//2+1):]
                    return "ALLOK", string1, string2
                    # Siempre se retornan 3 variables:
                    # código de error, primera string, segunda string.
