import unittest

from modelos.jogo import Jogo
from parse import parse_jogos


class TestJogo(unittest.TestCase):

    def tes_ranking_kills_game(self):
        jogos = parse_jogos('teste.log')
        jogo1 = jogos[0]
        result = jogo1.ranking_kills_game()
        dict_test = [('Mocinha','0'), ('Isgalamido', '-5')]
        self.assertDictEqual(result, dict_test)


if __name__ == '__main__':
    unittest.main()