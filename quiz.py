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
       "sudo apt install espeak".
     * O som só funciona com internet. Caso não tenha ou seja fraca
       o programa funcionará de forma inconsistente, a menos que
       você desative-o na opção 5.

        Onde você pode me encontrar:  👽
     ------------------------------

  Autor:     Gabriel Santana
  Linkedin:  https://www.linkedin.com/in/gabrielsantana444
  Github:    https://github.com/GabrielSantos198
  Website:   https://gabrielsantana.herokuapp.com/
  E-mail:    gabrielsantana9807@gmail.com

  - Caso tenha gostado deixe sua 🌟, pra dar aquela força.
'''


# Do Python
from random import shuffle
import os
import platform
from time import sleep

# Meus
from topics import tecnologia, astronomia, geografia, curiosidades
from score import Recordes
from ascii_art import desenho


# Função pra limpar o buffer.
def limpar_buffer():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


# Função de fala.
som = True  # Caso False o som será desativado.
def falar_texto(msg):
    global som
    if som:
        os.system(f'espeak -v pt-br "{msg}"')


# Fazer pergunta da categoria escolhida pelo jogador.
continuar = True
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
                    Recordes(c).adicionar()
                    break
        else:
            limpar_buffer()
            desenho(0)
            Recordes(c).adicionar()
            falar_texto('Parabéns, você respondeu todas as perguntas dessa categoria corretamente.')
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
            falar_texto('Digite uma alternativa válida.')
        else:
            if alternativa in 'ABC':
                return alternativa
            print('\033[1;31mDigite uma alternativa válida.\033[m')
            falar_texto('Digite uma alternativa válida.')


# Função pra parar o programa até que alguma tecla seja pressionada.
def parar():
    global continuar
    try:
        proseguir = str(input('Aperte qualquer tecla para prosseguir.'))
    except KeyboardInterrupt:
        print('\033[1;33mPrograma interrompido.\033[m')
        continuar = False
    except:
        pass


# Código Base.
while continuar:
    topo = False  # Caso True server pras principais condições do laço se tornarem falsas até que o mesmo dê outra volta. É meio que um macete(Gambiarra), pois o continue do python não daria certo na situação abaixo.
    limpar_buffer()
    desenho(1)
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
            falar_texto('Digite uma opção válida.')
        else:
            if opcao >= 0 and opcao <= 8:
                break
            print('\033[1;31mDigite uma opção válida.\033[m')
            falar_texto('Digite uma opção válida.')

    if continuar:
        if opcao == 0:
            limpar_buffer()
            desenho(3)
            fazer_pergunta(tecnologia)
        elif opcao == 1:
            limpar_buffer()
            desenho(4)
            fazer_pergunta(astronomia)
        elif opcao == 2:
            limpar_buffer()
            desenho(5)
            fazer_pergunta(geografia)
        elif opcao == 3:
            limpar_buffer()
            desenho(6)
            fazer_pergunta(curiosidades)
        elif opcao == 4:
            limpar_buffer()
            desenho(7)
            fazer_pergunta(tecnologia+astronomia+geografia+curiosidades)
        elif opcao == 5:
            if som:
                som = False
                print('\033[1;33mDesativando Som...\033[m')
            else:
                som = True
                print('\033[1;33mAtivando Som...\033[m')
            topo = True
            sleep(2)
        elif opcao == 6:
            limpar_buffer()
            Recordes().ver()
            topo = True
            parar()
        elif opcao == 7:
            Recordes().reiniciar()
            topo = True
            sleep(2)
        elif opcao == 8:
            limpar_buffer()
            desenho(8)
            topo = True
            parar()

    # Pergunta se o jogador deseja continuar jogando.
    if continuar and topo == False:
        print()
        print('='*30)
        while True:
            try:
                escolha = str(input('Deseja ir um novo jogo? [S/N] ')).upper().strip()[0]
            except KeyboardInterrupt:
                print('\033[1;33mPrograma interrompido.\033[m')
                break
            except:
                print('\033[1;31mDigite uma alternativa válida.\033[m')
                falar_texto('Digite uma alternativa válida.')
            else:
                if escolha in 'SN':
                    if escolha == 'N':
                        continuar = False
                        print('\033[1;34mEncerrando...\033[m')
                        falar_texto('Encerrando')
                        sleep(2)
                    else:
                        print('\033[1;34mCarregando...\033[m')
                        falar_texto('Carregando')
                        sleep(2)
                    break
                print('\033[1;31mDigite uma alternativa válida.\033[m')
                falar_texto('Digite uma alternativa válida.')

