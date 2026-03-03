#1. AND (Y) (ambos verdaderos)
#2. OR (O) ()
#3. NOT (NEGACION) (invierte, si es verdadero se vuelve falso y viceversa)
#Emily Torres
v = True
f = False
print(v and f) #false
nota = 11
print(nota >=10 and nota <=10)
edad = 18
print(18 == edad or edad > 10)
#----------
#Emily Torres Menendez
nota1 = 5
nota2 = 15
nota3 = 20
#promedio: sumas tres notas y divides entre tres
promedio = (nota1 + nota2 + nota3)/ 3
print(promedio)
if (promedio>= 17):
    print('Excelente')
elif (promedio >= 14):
    print('Bueno')
elif (promedio >= 11):
    print('Regular')
elif (promedio <= 10):
    print('Reprobado')