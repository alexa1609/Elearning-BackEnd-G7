from re import L


edad_roberta = 20

if edad_roberta >= 18 :
    print('Si puede entrar a la discoteca')
else:
    print('No puedes entrar, anda al cine')

edad_martin = 70
if edad_martin >= 65:
    print('Esa persona esta jubilada')
elif edad_martin >= 18:
    print('Esa persona es mayor de edad')
elif edad_martin >= 0:
    print('Esa persona es menor de edad')
else:
    print('Edad imposible')

#la forma para ingresar valores al programa desde consola
data = input("Hola, ingresa tu talla de polo:") # siempre lo convierte a string
print(type(data))
if data == 'xl' :
    print('El polo recien llegara a fin de mes')
elif data == 'l' or data == 'm':
    input('Ingresa el color del polo')
elif data == 's':
    print('Solamente hay en color morado')
else:
    print('Talla incorrecta')


