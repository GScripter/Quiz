# Meus
from topics import tecnologia, astronomia, geografia, curiosidades
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
                    print()
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
            else:
                print('\033[1;31mDigite uma alternativa válida.\033[m')


limpar_buffer()
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
    [3] Curiosidades             //   \ \
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


# Mostrar o título da categoria escolhida pelo jogador e chama a função principal passando a categoria como parâmetro.
if continuar:
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
        print('''
        _          _                                         _
       / \    ___ | |_  _ __  ___   _ __    ___   _ __ ___  (_)  __ _
      / _ \  / __|| __|| '__|/ _ \ | '_ \  / _ \ | '_ ` _ \ | | / _` |
     / ___ \ \__ \| |_ | |  | (_) || | | || (_) || | | | | || || (_| |
    /_/   \_\|___/ \__||_|   \___/ |_| |_| \___/ |_| |_| |_||_| \__,_|
        ''')
        fazer_pergunta(astronomia)
    elif opcao == 2:
        print('''
      ____                                   __  _
     / ___|  ___   ___    __ _  _ __  __ _  / _|(_)  __ _
    | |  _  / _ \ / _ \  / _` || '__|/ _` || |_ | | / _` |
    | |_| ||  __/| (_) || (_| || |  | (_| ||  _|| || (_| |
     \____| \___| \___/  \__, ||_|   \__,_||_|  |_| \__,_|
                         |___/
        ''')
        fazer_pergunta(geografia)
    elif opcao == 3:
        print('''
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
