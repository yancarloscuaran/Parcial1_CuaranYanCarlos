import operator
texto = 'Quiero alejarme y caminar caminar caminar A tierras lejanas llegar y admirar admirar Por verdes y limpias praderas andar andar Y bajo las estrellas dormir y soñar soñar soñar'

lista = texto.lower().split()
rep = []
repeticiones = []
for numpalabras in lista:
    rep.append(lista.count(numpalabras))

for conteo in range(0, len(lista)):
    repeticiones.append((lista[conteo], rep[conteo]))
cadena = list(set(repeticiones))
cadena = sorted(cadena, key=operator.itemgetter(1))

for conteo in range(0, len(cadena)):
    print('La palabra '+ "(" + cadena[conteo][0]+ ")" + ' se repite ' + str(cadena[conteo][1]) + ' veces.')