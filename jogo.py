
class Jogo:
    total_de_kills = 0
    players = []
    kills = {}
    
    def __init__(self, linhas_do_jogo, game):
        self.linhas_do_jogo =linhas_do_jogo
        self.game = game
    
    def Mostrar_linhas(self):
        for linha in self.linhas_do_jogo:
            print(linha)