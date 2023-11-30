"""Crie uma função que recebe uma palavra (string), separa todos os caracteres em uma lista, retorna esta lista e quantidade de letras."""

def separar_caracteres(palavra):
    lista_caracteres = list(palavra)
    quant_letras = sum(c.isalpha() for c in lista_caracteres)
    return lista_caracteres, quant_letras

palavra_usuario = input("Digite uma palavra: ")

if not palavra_usuario.isalpha():
    if ' ' in palavra_usuario:
        print("Isso não é uma palavra, é uma frase. Por favor, digite apenas uma palavra.")
    else:
        print("Isso não é uma palavra. Por favor, digite apenas letras.")
else:
    caracteres, quant_letras = separar_caracteres(palavra_usuario)

    print(f"Lista de caracteres: {caracteres}")
    print(f"Quantidade de letras: {quant_letras}")
