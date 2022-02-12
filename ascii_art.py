# Uma única função que contém todos os desenhos ascii do programa.
def desenho(num):
    if num == 0:
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
    elif num == 1:
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
    elif num == 3:
        print(r'''
   _                             _                _
  | |_  ___   ___  _ __    ___  | |  ___    __ _ (_)  __ _
  | __|/ _ \ / __|| '_ \  / _ \ | | / _ \  / _` || | / _` |
  | |_|  __/| (__ | | | || (_) || || (_) || (_| || || (_| |
   \__|\___| \___||_| |_| \___/ |_| \___/  \__, ||_| \__,_|
                                            |___/
        ''')
    elif num == 4:
        print(r'''
      _          _                                         _
     / \    ___ | |_  _ __  ___   _ __    ___   _ __ ___  (_)  __ _
    / _ \  / __|| __|| '__|/ _ \ | '_ \  / _ \ | '_ ` _ \ | | / _` |
   / ___ \ \__ \| |_ | |  | (_) || | | || (_) || | | | | || || (_| |
  /_/   \_\|___/ \__||_|   \___/ |_| |_| \___/ |_| |_| |_||_| \__,_|
        ''')
    elif num == 5:
        print(r'''
    ____                                   __  _
   / ___|  ___   ___    __ _  _ __  __ _  / _|(_)  __ _
  | |  _  / _ \ / _ \  / _` || '__|/ _` || |_ | | / _` |
  | |_| ||  __/| (_) || (_| || |  | (_| ||  _|| || (_| |
   \____| \___| \___/  \__, ||_|   \__,_||_|  |_| \__,_|
                        |___/
        ''')
    elif num == 6:
        print(r'''
    ____              _              _      _             _
   / ___|_   _  _ __ (_)  ___   ___ (_)  __| |  __ _   __| |  ___  ___
  | |   | | | || '__|| | / _ \ / __|| | / _` | / _` | / _` | / _ \/ __|
  | |___| |_| || |   | || (_) |\__ \| || (_| || (_| || (_| ||  __/\__ \
   \____|\__,_||_|   |_| \___/ |___/|_| \__,_| \__,_| \__,_| \___||___/
        ''')
    elif num == 7:
        print(r'''
    ____                    _
   / ___|  ___  _ __  __ _ (_) ___
  | |  _  / _ \| '__|/ _` || |/ __|
  | |_| ||  __/| |  | (_| || |\__ \
   \____| \___||_|   \__,_||_||___/
        ''')
    elif num == 8:
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
       "sudo apt install espeak".
     * O som só funciona com internet. Caso não tenha ou seja fraca
       o programa funcionará de forma inconsistente, a menos que
       você desative-o na opção 5.\033[m

    Onde você pode me encontrar:  👽
    ------------------------------

    Autor:     Gabriel Santana
    Linkedin:  https://www.linkedin.com/in/gabrielsantana444
    Github:    https://github.com/GabrielSantos198
    Website:   https://gabrielsantana.herokuapp.com/
    E-mail:    gabrielsantana9807@gmail.com

    - Caso tenha gostado deixe sua 🌟, pra dar aquela força.
        ''')
    elif num == 9:
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
        _              _  ___
       | |_ ___  _ __ / |/ _ \
       | __/ _ \| '_ \| | | | |
       | || (_) | |_) | | |_| |
        \__\___/| .__/|_|\___/
                |_|
        ''')

