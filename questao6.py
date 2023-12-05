"""6) Um jogador de um jogo de vídeo game deseja subir de nível em seu personagem ao atingir 50 inimigos derrotados. 
Enquanto esse número não é alcançado, uma mensagem indicando quantos inimigos ainda faltam é exibida na tela."""

inimigos_derrotados = 0
nivel = 0

while inimigos_derrotados < 50:
    # solicitar qtos inimigos derrotados
    derrotas = int(input("Digite o número de inimigos derrotados até agora: "))
    
    # validacao
    if derrotas < 0:
        print("Número inválido. Tente novamente.")
        continue
    
    # verificar numero total > 50 (erro)
    if inimigos_derrotados + derrotas > 50:
        print("Erro!!!!! O total de inimigos derrotados não pode ultrapassar 50.")
        continue
    
    # Incrementar o contador de inimigos derrotados
    inimigos_derrotados += derrotas
    
    # mensagem com base na qtd
    resto_inimigos = 50 - inimigos_derrotados
    if resto_inimigos == 1:
        print("Falta 1 inimigo para você mudar de nível!")
    else:
        print(f"Faltam {resto_inimigos} inimigos para você mudar de nível!")

print("\nVocê atingiu o próximo nível!")
nivel = 1
