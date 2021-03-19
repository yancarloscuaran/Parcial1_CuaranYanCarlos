texto = 'En muchas partes del cuerpo como son las manos, las orejas o los pies, están representados todos los órganos y partes del cuerpo. Incidiendo sobre estas zonas se pueden crear arcos reflejos que actúen directamente sobre cualquier órgano del cuerpo y que solucionen cualgquier anomalía que exista.'


lista = texto.split()
conteo = []
for numpalabras in lista:
    conteo.append(lista.count(numpalabras))

print("Repetidas"+ "\n" + str(list(zip(lista, conteo))))