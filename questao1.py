"""1 ) Para determinar se um candidato está qualificado para uma vaga de emprego, são aplicados dois critérios:
a) O candidato deve ter uma presença igual ou superior a 60% em um treinamento obrigatório.
b) O candidato deve ter uma média de desempenho igual ou superior a 7 em uma série de testes.

Para auxiliar na avaliação dos candidatos, você deve criar uma função que recebe uma lista de dicionários 
contendo o nome do candidato, a média de desempenho e a quantidade de horas de ausência do treinamento.
Com esses dados, a função deve calcular se o candidato está qualificado ou não.
A presença do candidato é calculada considerando que o treinamento teve um total de 60 horas e utilizando a fórmula:
(Total horas - número de faltas)/Total horas * 100;"""

def avaliar_candidatos():
    num_candidatos = int(input("Digite o número de candidatos: "))
    lista_candidatos = []
    qualificados = []
    desqualificados = []

    for i in range(num_candidatos):
        nome = input(f"Digite o nome do candidato {i + 1}: ")
        media_desempenho = float(input(f"Digite a média de desempenho do candidato {i + 1}: "))
        horas_faltas = int(input(f"Digite a quantidade de horas de faltas do treinamento para o candidato {i + 1}: "))

        candidato = {'nome': nome, 'media_desempenho': media_desempenho, 'horas_faltas': horas_faltas}
        lista_candidatos.append(candidato)

    for candidato in lista_candidatos:
        nome = candidato['nome']
        media_desempenho = candidato['media_desempenho']
        horas_faltas = candidato['horas_faltas']

        # presença
        total_horas_treinamento = 60
        presenca = ((total_horas_treinamento - horas_faltas) / total_horas_treinamento) * 100

        # calculo criterios
        if presenca >= 60 and media_desempenho >= 7:
            qualificados.append(nome)
        else:
            desqualificados.append(nome)

    # resultado
    if qualificados:
        print("Candidatos qualificados:")
        for qualificado in qualificados:
            print(f"- {qualificado}")
    else:
        print("Nenhum candidato qualificado.")

    if desqualificados:
        print("\nCandidatos desqualificados:")
        for desqualificado in desqualificados:
            print(f"- {desqualificado}")
    else:
        print("\nTodos os candidatos foram qualificados.")

# executar
avaliar_candidatos()
