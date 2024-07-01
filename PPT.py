import random

jogadas = ['Pedra', 'Papel', 'Tesoura']  # Lista das Jogadas
# Placar
pt_maquina = 0
pt_usuario = 0

jogar_novamente = True  # Variável de Controle do Looping Para Jogar Novamente

while jogar_novamente:
    duracao = input('Vence quem atingir quantos pontos? ')  # Duração da Partida
    while not duracao.isdigit():  # Verificar se Duração == Inteiro
        print('Entrada inválida. Por favor, insira um número inteiro.')  # Caso Duração != Inteiro
        duracao = input('Vence quem atingir quantos pontos? ')  # Duração da Partida
    duracao = int(duracao)  # Conversão para Inteiro
    print('')  # Formatação no Output

    while pt_maquina < duracao and pt_usuario < duracao:  # Looping de Solicitar Outra Jogada Caso Não Acabe
        usuario = input('Qual sua jogada? ').capitalize()  # Jogada do Usuário
        while usuario not in jogadas:  # Verificação de Jogada Válidas
            print('Jogada inválida')  # Caso de Jogada Inválida
            usuario = input('Qual sua jogada? ').lower()  # Resolicitação da Jogada do Usuário

        if usuario in jogadas:
            maquina = random.choice(jogadas).capitalize()  # Jogada da Máquina
            print(maquina)

        # Combinações de Vitória / Derrota / Empate
        # Casos de Vitória
        if maquina == 'Papel' and usuario == 'Tesoura':
            print('Você ganhou.')
            pt_usuario += 1
        elif maquina == 'Pedra' and usuario == 'Papel':
            print('Você ganhou.')
            pt_usuario += 1
        elif maquina == 'Tesoura' and usuario == 'Pedra':
            print('Você ganhou.')
            pt_usuario += 1

        # Caasos de Derrota
        elif maquina == 'Papel' and usuario == 'Pedra':
            print('Você perdeu.')
            pt_maquina += 1
        elif maquina == 'Pedra' and usuario == 'Tesoura':
            print('Você perdeu.')
            pt_maquina += 1
        elif maquina == 'Tesoura' and usuario == 'Papel':
            print('Você perdeu.')
            pt_maquina += 1

        # Casos de Empate
        elif maquina == 'Tesoura' and usuario == 'Tesoura':
            print('Empate.')
        elif maquina == 'Papel' and usuario == 'Papel':
            print('Empate.')
        elif maquina == 'Pedra' and usuario == 'Pedra':
            print('Empate.')

        # Exibição do Placar
        placar = f'Você: {pt_usuario} x Máquina: {pt_maquina}'
        print(placar)
        print('')  # Formatação no Output

        # Resultado do Vencedor
        if pt_maquina == duracao:
            print('Você perdeu a partida :(')
            break
        if pt_usuario == duracao:
            print('Você venceu a partida :)')
            break

    # Controle de Jogar Novamente ou Finalizar
    replay = input('Deseja jogar novamente? (s/n) ').lower()  # Soliciação de Jogar Novamente
    while replay not in ['s', 'n']:  # Verificação de Resposta Válida
        print('Opção inválida!')  # Caso de Resposta Inválida
        replay = input('Deseja jogar novamente? (s/n) ').lower()  # Resolicitação de Jogar Novamente

    # Finalização da Rodada
    if replay == 's':  # Jogar Novamente
        print('')  # Formatação no Output
        # Zerar o Placar
        pt_maquina = 0
        pt_usuario = 0
    # Finalização do Jogo
    if replay == 'n':  # Não Jogar Novamente
        jogar_novamente = False  # Alterando a Variável de Controle para Finalizar o Looping

# Finalização Geral
print('Obrigado por jogar. Volte Sempre!')
