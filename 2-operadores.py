#Operadores en python
#1. Operadores aritmeticos
suma = 5 + 5
resta = 10 - 6
multipliacion = 5 * 5
division = 10 / 2
modulo = 10 % 2
exponente = 10 ** 2
print (suma)
print(resta)
print (multipliacion)
print(division)
print(modulo)
print(exponente)
print('El resultado de la suma es:', suma)
print('El resultado de la resta es:', resta)
print('El resultado de la multiplicacion es:', multipliacion)
print('El resultado de la division es:', division)
print('El resultado del modulo es:', modulo)
print('El resultado del exponente es:', exponente)

#2. Operadores de comparacion
print (5 == 5)  #es '==' igual a
print (5 != 5)  #'!= se lee como diferente de
print (10 > 5) #mayor que
print (10 < 5) #menor que
print (10 >= 5) #mayor igual que
print (10 <= 5) #menor igual que

#3. Operadores logicos
v = True
f = False
#3.1 and (y)
print('----------AND')
print(v and v)
print(v and f)
print(f and v)
print(f and f)
#3.2 or (o)
print('----------OR')
print(v or v)
print(v or f)
print(f or v)
print(f or f)
#3.3 not (negacion)
print('----------NOT')
print(not v)
print(not f)
#Operadores de asignación
#4.1 Suma y asigna (+=)
print('--------------+=')
edad = 20
edad += 5
print(edad)
#4.2 Resta y asigna (-=)
print('----------------=')
saldo = 100
saldo -= 10
print(saldo)
#4.3 multiplica y asigna (*=)
print('--------------*=')
precio = 30
precio *= 5
print(precio)
#4.4 Divide y asigna (/=)
print('--------------/=')
total = 200
total /= 2
print(total)