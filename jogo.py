
class Jogo:
    def __init__(self, linhas_do_jogo):
        self.linhas_do_jogo =linhas_do_jogo
    
    def Mostrar_linhas(self):
        for linha in self.linhas_do_jogo:
            print(linha)