import random

jogadas = ['Pedra', 'Papel', 'Tesoura']  # Lista das Jogadas
# Placar
pt_maquina = 0
pt_usuario = 0

jogar_novamente = True  # Variável de Controle do looping externo

while jogar_novamente:
    duracao = int(input('Vence quem atingir quantos pontos? '))  # Duração da Partida
    usuario = input('Qual sua jogada? ').lower()  # Jogada do Usuário
    maquina = random.choice(jogadas).lower()  # Jogada da Máquina
    print(maquina)

    # Combinações de Vitória / Derrota / Empate
    while True:
        if maquina == 'papel' and usuario == 'tesoura':
            print('Você ganhou')
            pt_usuario += 1
        elif maquina == 'papel' and usuario == 'pedra':
            print('Você perdeu')
            pt_maquina += 1
        elif maquina == 'pedra' and usuario == 'papel':
            print('Você ganhou')
            pt_usuario += 1
        elif maquina == 'pedra' and usuario == 'tesoura':
            print('Você perdeu')
            pt_maquina += 1
        elif maquina == 'tesoura' and usuario == 'pedra':
            print('Você ganhou')
            pt_usuario += 1
        elif maquina == 'tesoura' and usuario == 'papel':
            print('Você perdeu')
            pt_maquina += 1
        elif maquina == 'tesoura' and usuario == 'tesoura':
            print('Empate')
        elif maquina == 'papel' and usuario == 'papel':
            print('Empate')
        elif maquina == 'pedra' and usuario == 'pedra':
            print('Empate')
        else:
            print('Jogada inválida!')
        # Exibição do Placar
        placar = f'Você: {pt_usuario} x Maquina: {pt_maquina}'
        print(placar)
        print('')

        # Resultado do Vencedor
        if pt_maquina == duracao:
            print('Você perdeu a partida')
            break
        if pt_usuario == duracao:
            print('Você venceu a partida!!')
            break
        # Próxima Jogada Caso Não Acabou a Partida
        else:
            usuario = input('Próxima jogada: ').lower()  # Jogada do Usuário
            maquina = random.choice(jogadas).lower()  # Jogada da Máquina
            print(maquina)

    # Controle de Jogar Novamente ou Finalizar
    replay = input('Deseja jogar novamente? (s/n) ').lower()
    while replay not in ['s', 'n']:
        print('Opção inválida!')
        replay = input('Deseja jogar novamente? (s/n) ').lower()

    # Finalização da Rodada
    if replay == 's':
        print('')
        # Zerar o Placar
        pt_maquina = 0
        pt_usuario = 0
    # Finalização do Jogo
    if replay == 'n':
        jogar_novamente = False
# Finalização Geral
print('Obrigado por jogar. Volte Sempre!')
