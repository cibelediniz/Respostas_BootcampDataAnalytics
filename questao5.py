"""
5) Na variável países_ano, temos uma lista de listas, em que cada elemento é uma lista de dois elementos, 
em que o primeiro é o nome de um país e o segundo é o ano em que a nação foi fundada.

lista_paises = [["Brasil", "1500"],["Mexico","1519"], ["Inglaterra", "927"], ["Espanha","1978"], ["Escocia", "843"]]

Você deseja criar uma nova lista de listas a partir do exemplo (lista_paises), em que cada elemento é uma lista de dois
elementos, sendo o primeiro o nome do país (como é na lista original) e o segundo é o número de anos desde a fundação do país (considere que o ano atual é 2023).
"""

# lista original
lista_paises = [["Brasil", "1500"], ["Mexico", "1519"], ["Inglaterra", "927"], ["Espanha", "1978"], ["Escocia", "843"]]
ano_atual = 2023

# criar lista (nome pais e qts anos de fundacao)
paises_ano = [[pais, ano_atual - int(ano)] for pais, ano in lista_paises]

# print nova lista
print(paises_ano)
