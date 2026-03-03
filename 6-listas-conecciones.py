#Emily Torres
#Listas
lista = ["Emily", "Torres", 98, True]
print(lista[3])
#Lista de frutas
frutas = ['mango', 'fresa', 'platano', 'arandano', 'manzana']
print(frutas[3])
frutas[1] = 'granada'
print(frutas)
#Matriz
matriz = [
    [1,2,3],
    [4,6,1],
    [0,1,0]
]
print(matriz[0][1])
#Lista de numeros
numeros = [1,2,3,4,5,6,7,8,9,0]
print(numeros[:3])
print(numeros[1:5])
print(numeros[::2])
print(numeros[1::2])
print(numeros[::-1])
#Ciclo for en las listas
for i in numeros:
    print(i*10)
for f in frutas:
    print(f)
#Metodos en las listas
print('---------metodos')
frutas = ['mango', 'fresa', 'platano', 'arandano', 'manzana']
#Agregar un nuevo dato
frutas.append('ciruela')
print(frutas)
#insert
frutas.insert(2,'pera')
print(frutas)
#Remove
frutas.remove('arandano')
print(frutas)
#Optener o eliminar el ultimo dato - POP()
frutas.pop()
print(frutas)
#sort() - ordenar la lista
frutas.sort()
print(frutas)
#Reverse()
frutas.reverse()
print(frutas)
#len
cantidad = len(frutas)
print(cantidad)
#Index - encuentra el indicie
indice = frutas.index('manzana')
print(indice)
