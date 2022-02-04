# Meus
from topics import tecnologia, astronomia, geografia, curiosidade
# Terceiros
from random import shuffle
import os, platform


# Função pra limpar o buffer.
def limpar_buffer():
    if platform.system()=="Windows":
        os.system('cls')
    else: 
        os.system('clear')


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
            alternativa = validar_alternativa()
            if continuar:
                if alternativa == 'A' and catg[c][1][0] == catg[c][2] or alternativa == 'B' and catg[c][1][1] == catg[c][2] or alternativa == 'C' and catg[c][1][2] == catg[c][2]:
                    print('\033[1;32mParabéns você acertou.\033[m')
                    c +=1
                else:
                    print(f'\033[1;31mQue pena você errou.\033[1;33m Resposta Correta: {catg[c][2]}\033[m')
                    continuar = False
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


# Função que valida e retorna a alternativa do jogador.
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
            else:
                print('\033[1;31mDigite uma alternativa válida.\033[m')


print(r'''
  _______________________________________
           ___          _
          / _ \  _   _ (_) ____
         | | | || | | || ||_  /
         | |_| || |_| || | / /
          \__\_\ \__,_||_|/___|
  ----------------------------------------
                               \
      Categorias                \

    [0] Tecnologia                 .--.
    [1] Astronomia                |o_o |
    [2] Geografia                 |:_/ |
    [3] Curiosidade              //   \ \
    [4] Gerais                  (|     | )
                                /'\_   _/`\
                                \___)=(___/
''')


# Escolha de categoria.
while continuar:
    try:
        opcao = int(input('Opção: '))
    except KeyboardInterrupt:
        print('\033[1;33mPrograma interrompido.\033[m')
        continuar = False
    except:
        print('\033[1;31mDigite uma opção válida.\033[m')
    else:
        if opcao >= 0 and opcao <= 4:
            break
        else:
            print('\033[1;31mDigite uma opção válida.\033[m')

# Chamar função passando a categoria escolhida como parâmetro.
if continuar:
    if opcao == 0:
        fazer_pergunta(tecnologia)
    elif opcao == 1:
        fazer_pergunta(astronomia)
    elif opcao == 2:
        fazer_pergunta(geografia)
    elif opcao == 3:
        fazer_pergunta(curiosidade)
    elif opcao == 4:
        pass
    else:
        pass
