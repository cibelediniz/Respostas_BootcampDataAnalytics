"""3) Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule
quanto poderia comprar de cada moeda estrangeira. Considere a tabela de conversão abaixo:

Valor convertido em real:

Dólar Americano: 4,91
Peso Argentino: 0,02
Dólar Australiano: 3,18
Dólar Canadense: 3,64
Franco Suiço: 0,42
Euro: 5,36
Libra esterlina: 6,21"""


taxas_conversao = {
    'Dólar Americano': 4.91,
    'Peso Argentino': 0.02,
    'Dólar Australiano': 3.18,
    'Dólar Canadense': 3.64,
    'Franco Suiço': 0.42,
    'Euro': 5.36,
    'Libra esterlina': 6.21
}

# solicita valor do usuario em reais
valor_usuario = float(input("Digite o valor em reais na sua carteira: R$ "))

# opcoes de moeda
print("\nOpções de moeda:")
for i, moeda in enumerate(taxas_conversao.keys(), start=1):
    print(f"{i}. {moeda}")

# solicita que o usuario selecione a moeda
opcao_moeda = int(input("\nEscolha o número da moeda que deseja verificar: "))

# validacao
if 1 <= opcao_moeda <= len(taxas_conversao):
    moeda_selecionada = list(taxas_conversao.keys())[opcao_moeda - 1]
    taxa_selecionada = taxas_conversao[moeda_selecionada]

    # calc e print
    valor_convertido = valor_usuario / taxa_selecionada
    print(f"\nValor convertido em {moeda_selecionada}: $ {valor_convertido:.2f}")
else:
    print("Opção inválida. Por favor, escolha uma moeda válida.")
