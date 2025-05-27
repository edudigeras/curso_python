def calcular_media(lista):
    total = 0
    for i in lista:   
            total +=i
    media = total / len(lista)

    return media

numeros = [7,9,8,7]
print(calcular_media(numeros))