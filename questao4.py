"""4) O chefe decidiu premiar os melhores funcionários de sua empresa com um brinde. 
Para isso ele vai entregar um brinde para todos os funcionários que tiverem uma performance superior a média da equipe.

Elabore uma função que recebe uma lista de nome em formato de dict (dicionário) com nome do funcionário
e a média do funcionário (Valor de 0 a 10). Esta função deve calcular a média da equipe, identificar 
quais funcionários tem média igual ou superior a média da equipe e retornar uma lista com o nome dos funcionários
que possuem média igual ou superior a média da equipe. A ordem dos nomes da lista de retorno deve ser em ordem decrescente."""

class Funcionario:
    def __init__(self, nome, media):
        self.nome = nome
        self.media = media

class Equipe:
    def __init__(self):
        self.funcionarios = []

    def add_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def calcular_media_equipe(self):
        medias = [funcionario.media for funcionario in self.funcionarios]
        return sum(medias) / len(medias) if medias else 0

    def premiar_funcionarios(self):
        media_equipe = self.calcular_media_equipe()

        # ordenar funcionarios por media
        funcionarios_ordenados = sorted(self.funcionarios, key=lambda x: x.media, reverse=True)

        # pegar nome dos funcionarios premiados
        premiados = [funcionario.nome for funcionario in funcionarios_ordenados if funcionario.media >= media_equipe]

        return premiados

# entrada usuario
equipe = Equipe()
numero_funcionarios = int(input("Digite o numero de funcionarios: "))

for i in range(numero_funcionarios):
    nome = input(f"Digite o nome do funcionario {i + 1}: ")
    media = float(input(f"Digite a media do funcionario {i + 1} (de 0 a 10): "))
    funcionario = Funcionario(nome, media)
    equipe.add_funcionario(funcionario)

# Chamar a função e exibir resultados
funcionarios_premiados = equipe.premiar_funcionarios()

if funcionarios_premiados:
    print("\nFuncionarios premiados:")
    for nome in funcionarios_premiados:
        print(nome)
else:
    print("\nNenhum funcionario atingiu a media da equipe.")
