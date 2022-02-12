from ascii_art import desenho


class Recordes:
    def __init__(self, potuacao_partida=0):
        self.pontuacao_partida = potuacao_partida

    def adicionar(self):
        pontuacoes = []
        # Abre arquivo, adiciona a pontuação da rodada e fecha.
        arquivo = open('score.txt', 'a')
        arquivo.write(f'{self.pontuacao_partida}\n')
        arquivo.close()
        # Abre arquivo, joga todos os valos do arquivo na lista, ordena do maior pro menor e fecha.
        arquivo = open('score.txt', 'r')
        pontuacao = ''
        for linha in arquivo:
            for caracter in linha:
                if caracter.isnumeric():
                    pontuacao += caracter
            if int(pontuacao) not in pontuacoes:
                pontuacoes.append(int(pontuacao))
            pontuacao = ''
        pontuacoes.sort(reverse=True)
        arquivo.close()
        # Limpar todo o arquivo.
        open('score.txt', 'w').close()
        # Abre arquivo, joga os 10 primeiros valores da lista e fecha arquivo.
        arquivo = open('score.txt', 'a')
        for contagem, ponto in enumerate(pontuacoes):
            if contagem <= 9:
                arquivo.write(f'{ponto}\n')
        arquivo.close()

    def ver(self):
        try:
            arquivo = open('score.txt', 'r')
        except FileNotFoundError:
            print('\033[33mArquivo "score.txt" Inexistente.\033[m')
        else:
            cont = 0
            desenho(9)
            print(f'{"="*20:^38}')
            for posicao, pontuacao in enumerate(arquivo):
                if posicao == 10:
                    break
                elif posicao == 0:
                    print(f'\033[33m{posicao+1:>14}º   >>>   {pontuacao}\033[m', end='')
                elif posicao == 1:
                    print(f'{posicao+1:>14}º   >>>   {pontuacao}', end='')
                elif posicao == 2:
                    print(f'\033[95m{posicao+1:>14}º   >>>   {pontuacao}\033[m', end='')
                else:
                    print(f'\033[90m{posicao+1:>14}º   >>>   {pontuacao}\033[m', end='')
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
