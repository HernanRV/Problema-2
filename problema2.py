def frase():
    cadena = input('Escribe una frase: ')
    lista = cadena.split(' ')
    lista.reverse()
    print(' '.join(lista))
