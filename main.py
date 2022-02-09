'''
  Responda perguntas divertidas e teste sua inteligência
  nesse incrível jogo escrito 100% em Python. Aprenda so-
  bre Tecnologia, Astronomia, Geografia e descubra coisas
  que você nem imaginava. Jogue muito e acerte o máximo
  que conseguir. E para que o jogo não venha se tornar
  monótono, novas atualizações de código e +perguntas serão
  com frequência acrescentadas.

  Obs:
     * As pull requests são bem vindas caso você tenha alguma
       ideia de melhoria no código.
     * Qualquer erro de exceção será tratado normalmente.
     * Ctrl-c Interrompe o programa a qualquer momento.
     * Não se esqueça de baixar o pacote espeak em seu OS,
       para que o programa possa falar. No linux basta rodar
       "sudo apt-get install espeak".

        Onde você pode me encontrar:  👽
     ------------------------------

  Autor:     Gabriel Santana
  Linkedin:  https://www.linkedin.com/in/gabrielsantana444
  Github:    https://github.com/GabrielSantos198
  Website:   https://gabrielsantana.herokuapp.com/
  E-mail:    gabrielsantana9807@gmail.com
            
  - Caso tenha gostado deixe sua 🌟, pra dar aquela força.
'''


# Terceiros
from random import shuffle
import os
import platform
from time import sleep
# Meus
from topics import tecnologia, astronomia, geografia, curiosidades


# Função pra limpar o buffer.
def limpar_buffer():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


# Função de fala.
def falar_texto(msg):
    os.system(f'espeak -vpt-br "{msg}"')


continuar = True
# Fazer pergunta da categoria escolhida pelo jogador.
def fazer_pergunta(catg):
    global continuar
    shuffle(catg)
    c = 0
    while continuar:
        if c <= len(catg)-1:
            shuffle(catg[c][1])
            print(f'Questão: {catg[c][0]}\n(A) {catg[c][1][0]}\n(B) {catg[c][1][1]}\n(C) {catg[c][1][2]}')
            falar_texto(catg[c][0])
            alternativa = validar_alternativa()
            if continuar:
                if alternativa == 'A' and catg[c][1][0] == catg[c][2] or alternativa == 'B' and catg[c][1][1] == catg[c][2] or alternativa == 'C' and catg[c][1][2] == catg[c][2]:
                    print('\033[1;32mParabéns você acertou.\033[m')
                    falar_texto('Parabéns você acertou.')
                    print()
                    c +=1
                else:
                    print(f'\033[1;31mQue pena você errou.\033[1;33m Resposta Correta: {catg[c][2]}\033[m')
                    falar_texto('Que pena você errou.')
                    break
        else:
            print(r'''
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""`
Parabéns, você respondeu todas as perguntas
      dessa categoria corretamente.
            ''')
            break


# Função que valida e retorna a resposta do jogador.
def validar_alternativa():
    global continuar
    while True:
        try:
            alternativa = str(input('Alternativa: ')).upper().strip()[0]
        except KeyboardInterrupt:
            print('\033[1;33mPrograma interrompido.\033[m')
            continuar = False
            break
        except:
            print('\033[1;31mDigite uma alternativa válida.\033[m')
        else:
            if alternativa in 'ABC':
                return alternativa
                break
            print('\033[1;31mDigite uma alternativa válida.\033[m')


# Código Base.
while continuar:
    topo = False  # Caso True server pras principais condições do laço se tornarem falsas até que o mesmo dê outra volta. É meio que um macete(Gambiarra), pois o continue do python não daria certo na situação abaixo.
    limpar_buffer()
    print(r'''
 ______________________________________________
              ___          _
             / _ \  _   _ (_) ____
            | | | || | | || ||_  /
            | |_| || |_| || | / /
             \__\_\ \__,_||_|/___|
 ----------------------------------------------
                                       \
  Categorias:        Outros:            \
                                          .--.
[0] Tecnologia    [5] Som On/Off         |o_o |
[1] Astronomia    [6] Ver Pontuação      |:_/ |
[2] Geografia     [7] Reiniciar pontos  //   \ \
[3] Curiosidades  [8] Sobre            (|     | )
[4] Gerais                             /'\_   _/`\
                                       \___)=(___/
 ''')

    # Escolha de categoria ou outros.
    while True:
        try:
            opcao = int(input('Opção: '))
        except KeyboardInterrupt:
            print('\033[1;33mPrograma interrompido.\033[m')
            continuar = False
            break
        except:
            print('\033[1;31mDigite uma opção válida.\033[m')
        else:
            if opcao >= 0 and opcao <= 4:
                break
            elif opcao == 8:
                limpar_buffer()
                print('''
  Responda perguntas divertidas e teste sua inteligência
  nesse incrível jogo escrito 100% em Python. Aprenda so-
  bre Tecnologia, Astronomia, Geografia e descubra coisas
  que você nem imaginava. Jogue muito e acerte o máximo
  que conseguir. E para que o jogo não venha se tornar
  monótono, novas atualizações de código e +perguntas serão
  com frequência acrescentadas.

  Obs:\033[33m
     * As pull requests são bem vindas caso você tenha alguma
       ideia de melhoria no código.
     * Qualquer erro de exceção será tratado normalmente.
     * Ctrl-c Interrompe o programa a qualquer momento.
     * Não se esqueça de baixar o pacote espeak em seu OS,
       para que o programa possa falar. No linux basta rodar
       "sudo apt-get install espeak".\033[m

        Onde você pode me encontrar:  👽
     ------------------------------

  Autor:     Gabriel Santana
  Linkedin:  https://www.linkedin.com/in/gabrielsantana444
  Github:    https://github.com/GabrielSantos198
  Website:   https://gabrielsantana.herokuapp.com/
  E-mail:    gabrielsantana9807@gmail.com
            
  - Caso tenha gostado deixe sua 🌟, pra dar aquela força.
                ''')
                try:
                    proseguir = str(input('Aperte qualquer tecla para prosseguir.'))
                except KeyboardInterrupt:
                    print('\033[1;33mPrograma interrompido.\033[m')
                    continuar = False
                    break
                except:
                    pass
                else:
                    pass
                topo = True
                break
            else:
                print('\033[1;31mDigite uma opção válida.\033[m')

    # Mostrar o título da categoria escolhida pelo jogador e chama a função principal passando a categoria como parâmetro.
    if continuar and topo == False:
        limpar_buffer()
        if opcao == 0:
            print(r'''
         _                             _                _
        | |_  ___   ___  _ __    ___  | |  ___    __ _ (_)  __ _
        | __|/ _ \ / __|| '_ \  / _ \ | | / _ \  / _` || | / _` |
        | |_|  __/| (__ | | | || (_) || || (_) || (_| || || (_| |
         \__|\___| \___||_| |_| \___/ |_| \___/  \__, ||_| \__,_|
                                                 |___/
            ''')
            fazer_pergunta(tecnologia)
        elif opcao == 1:
            print(r'''
            _          _                                         _
           / \    ___ | |_  _ __  ___   _ __    ___   _ __ ___  (_)  __ _
          / _ \  / __|| __|| '__|/ _ \ | '_ \  / _ \ | '_ ` _ \ | | / _` |
         / ___ \ \__ \| |_ | |  | (_) || | | || (_) || | | | | || || (_| |
        /_/   \_\|___/ \__||_|   \___/ |_| |_| \___/ |_| |_| |_||_| \__,_|
            ''')
            fazer_pergunta(astronomia)
        elif opcao == 2:
            print(r'''
          ____                                   __  _
         / ___|  ___   ___    __ _  _ __  __ _  / _|(_)  __ _
        | |  _  / _ \ / _ \  / _` || '__|/ _` || |_ | | / _` |
        | |_| ||  __/| (_) || (_| || |  | (_| ||  _|| || (_| |
         \____| \___| \___/  \__, ||_|   \__,_||_|  |_| \__,_|
                             |___/
            ''')
            fazer_pergunta(geografia)
        elif opcao == 3:
            print(r'''
          ____              _              _      _             _
         / ___|_   _  _ __ (_)  ___   ___ (_)  __| |  __ _   __| |  ___  ___
        | |   | | | || '__|| | / _ \ / __|| | / _` | / _` | / _` | / _ \/ __|
        | |___| |_| || |   | || (_) |\__ \| || (_| || (_| || (_| ||  __/\__ \
         \____|\__,_||_|   |_| \___/ |___/|_| \__,_| \__,_| \__,_| \___||___/
            ''')
            fazer_pergunta(curiosidades)
        else:
            print(r'''
          ____                    _
         / ___|  ___  _ __  __ _ (_) ___
        | |  _  / _ \| '__|/ _` || |/ __|
        | |_| ||  __/| |  | (_| || |\__ \
         \____| \___||_|   \__,_||_||___/
            ''')
            fazer_pergunta(tecnologia+astronomia+geografia+curiosidades)

    # Pergunta se o jogador deseja continuar jogando.
    if continuar and topo == False:
        print()
        sleep(2)
        limpar_buffer()
        print('='*30)
        while True:
            try:
                escolha = str(input('Deseja ir um novo jogo? [S/N] ')).upper().strip()[0]
            except KeyboardInterrupt:
                print('\033[1;33mPrograma interrompido.\033[m')
                continuar = False
                break
            except:
                print('\033[1;31mDigite uma alternativa válida.\033[m')
            else:
                if escolha in 'SN':
                    if escolha == 'N':
                        continuar = False
                        print('\033[1;34mEncerrando...\033[m')
                        sleep(2)
                    else:
                        print('\033[1;34mCarregando...\033[m')
                        sleep(2)
                    break
                print('\033[1;31mDigite uma alternativa válida.\033[m')
