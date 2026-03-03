while False:
    print('Luci')
pass
#Emily Torres
#Valida contraseña
password_correcta = "123456"
intentos = 0
while True:
    password = input('Ingrese por favor su contraseña: ')
    intentos += 1
    if (password == password_correcta):
        print('Contraseña correcta 👌')
    else:
        print('Contraseña incorrecta 😕')
        if(intentos >= 3):
            print('Tarjeta bloqueada')
            break