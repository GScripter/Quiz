class Recordes:
    def __init__(self, pontos=0):
        self.pontos = pontos

    def adicionar(self):
        nums = []
        # Abre arquivo, adiciona os pontos feitos na rodada e fecha.
        arquivo = open('score.txt', 'a')
        arquivo.write(f'{self.pontos}\n')
        arquivo.close()
        # Abre arquivo, joga todos os valos do arquivo na lista acima, ordena do maior pro menor e fecha.
        arquivo = open('score.txt', 'r')
        num = ''
        for r in arquivo:
            for n in r:
                if n.isnumeric():
                    num += n
            if int(num) not in nums:
                nums.append(int(num))
            num = ''
        nums.sort(reverse=True)
        arquivo.close()
        # Limpar todo o arquivo.
        open('score.txt', 'w').close()
        # Abre arquivo, joga os 10 primeiros valores da lista acima e fecha o arquivo.
        arquivo = open('score.txt', 'a')
        for c, l in enumerate(nums):
            if c <= 9:
                arquivo.write(f'{l}\n')
        arquivo.close()


    def ver(self):
        try:
            arquivo = open('score.txt', 'r')
        except FileNotFoundError:
            print('\033[33mArquivo "score.txt" Inexistente.\033[m')
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
        _              _  ___
       | |_ ___  _ __ / |/ _ \
       | __/ _ \| '_ \| | | | |
       | || (_) | |_) | | |_| |
        \__\___/| .__/|_|\___/
                |_|
            ''')
            cont = 0
            print(f'{"="*20:^38}')
            for num, arq in enumerate(arquivo):
                if num == 10:
                    break
                elif num == 0:
                    print(f'\033[33m{num+1:>14}º   >>>   {arq}\033[m', end='')
                elif num == 1:
                    print(f'{num+1:>14}º   >>>   {arq}', end='')
                elif num == 2:
                    print(f'\033[95m{num+1:>14}º   >>>   {arq}\033[m', end='')
                else:
                    print(f'\033[90m{num+1:>14}º   >>>   {arq}\033[m', end='')
                cont += 1
            if cont == 0:
                print(f'{"nenhum":>22}')
            print(f'{"="*20:^38}')
            arquivo.close()
            print()


    def reiniciar(self):
        try:
            open('score.txt', 'w').close()
        except FileNotFoundError:
            print('\033[33mArquivo "score.txt" Inexistentes.\033[m')
        else:
            print('\033[32mPontuações de jogo reiniciadas.\033[m')
