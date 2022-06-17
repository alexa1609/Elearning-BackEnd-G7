# Operadores aritmeticos

edad_juan = 40
edad_maria = 34

#SUMA
print(edad_juan + edad_maria)

#RESTA
print(edad_juan - edad_maria)

#MULTIPLICACION
print(edad_juan * edad_maria)

#DIVISION
print(edad_juan / edad_maria)

#MODULO
print(edad_juan % edad_maria)

#COCIENTE
print(edad_juan // edad_maria)

# En el caso de los caracteres Strings
# Cuando hacemos una sumatoria en los Strings se hara una concatenacion
# print(*{} - {}*.format(20,19))
mes = 'Junio'
temporada = 'invierno'
print(mes + temporada)
# y si hacemos uso de la multiplicacion hara que se repita N veces
print(mes * 5)

#------------------------------------------------------------------------------

# Operadores aritmeticos

edad_martha = 30
edad_marco = 25
# and Y > basta con que una de las dos condiciones sea F para que todo sea F
print(edad_marco > 18 and edad_marco > edad_martha)
# or 0 > basta con que una sea V para que todo sea V
print(edad_marco > 18 or edad_marco > edad_martha)
# not NO > invierte el resultado
print(not edad_marco > 50)

# Ejercicios
edad_eduardo= 18
edad_renato = 26
edad_laura = 35


# Como saber si eduardo es mayor de edad
print(edad_eduardo >= 18)

# Como saber si eduardo es mayor que laura
print(edad_eduardo > edad_laura)

# Como saber si renato es menor que laura pero mayor que eduardo
print (edad_renato < edad_laura and edad_renato > edad_eduardo)

# como saber si laura puede ser mayor que renato o menor que eduardo
print(edad_laura > edad_renato or edad_laura < edad_eduardo)


# Operadores de Asignacion
# = Asignacion
edad = 50

# += Incremento
edad += 1 #edad++

# -= Decremento
edad -= 1 #edad--

# *= Multiplicador
edad *=1

# /= Division
edad /= 2