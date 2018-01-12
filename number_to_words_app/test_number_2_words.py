import unittest
from number_2_words import number_to_words


class TestNumberToWords(unittest.TestCase):
    """Fails when input isn't integer."""
    def test_number_to_words_zero(self):
        self.assertEqual(number_to_words(0), 'zero')

    def test_number_to_words_negative(self):
        self.assertEqual(number_to_words(-1), 'minus jeden ')

    def test_number_to_words_ones(self):
        self.assertEqual(number_to_words(1), 'jeden ')
        self.assertEqual(number_to_words(9), 'dziewięć ')

    def test_number_to_words_tens(self):
        self.assertEqual(number_to_words(11), 'jedenaście ')
        self.assertEqual(number_to_words(19), 'dziewiętnaście ')

    def test_number_to_words_twenties(self):
        self.assertEqual(number_to_words(21), 'dwadzieścia jeden ')
        self.assertEqual(number_to_words(98), 'dziewięćdziesiąt osiem ')

    def test_number_to_words_hudreds(self):
        self.assertEqual(number_to_words(211), 'dwieście jedenaście ')
        self.assertEqual(number_to_words(984), 'dziewięćset osiemdziesiąt '
                                               'cztery ')

    def test_number_to_words_grammar_groups_thousand(self):
        self.assertEqual(number_to_words(1545), 'jeden tysiąc pięćset '
                                                'czterdzieści pięć ')
        self.assertEqual(number_to_words(23895), 'dwadzieścia trzy tysiące '
                                                 'osiemset dziewięćdziesiąt '
                                                 'pięć ')
        self.assertEqual(number_to_words(15457), 'piętnaście tysięcy '
                                                 'czterysta pięćdziesiąt '
                                                 'siedem ')

    def test_number_to_words_grammar_groups_million(self):
        self.assertEqual(number_to_words(1875963), 'jeden milion osiemset '
                                                   'siedemdziesiąt pięć '
                                                   'tysięcy dziewięćset '
                                                   'sześćdziesiąt trzy ')
        self.assertEqual(number_to_words(2389555), 'dwa miliony trzysta '
                                                    'osiemdziesiąt dziewięć '
                                                    'tysięcy pięćset '
                                                   'pięćdziesiąt pięć ')
        self.assertEqual(number_to_words(15123541), 'piętnaście milionów sto '
                                                    'dwadzieścia trzy tysiące '
                                                    'pięćset czterdzieści '
                                                    'jeden ')

    def test_number_to_words_grammar_groups_milliard(self):
        self.assertEqual(number_to_words(1987384651),
                         'jeden miliard dziewięćset osiemdziesiąt siedem '
                         'milionów trzysta osiemdziesiąt cztery tysiące '
                         'sześćset pięćdziesiąt jeden ')
        self.assertEqual(number_to_words(2123456789),
                         'dwa miliardy sto dwadzieścia trzy miliony czterysta '
                         'pięćdziesiąt sześć tysięcy siedemset osiemdziesiąt'
                         ' dziewięć ')
        self.assertEqual(number_to_words(5123456789),
                         'pięć miliardów sto dwadzieścia trzy miliony '
                         'czterysta pięćdziesiąt sześć tysięcy siedemset '
                         'osiemdziesiąt dziewięć ')

    def test_number_to_words_grammar_groups_billion(self):
        self.assertEqual(number_to_words(1987384605010),
                         'jeden bilion dziewięćset osiemdziesiąt siedem '
                         'miliardów trzysta osiemdziesiąt cztery miliony'
                         ' sześćset pięć tysięcy dziesięć ')
        self.assertEqual(number_to_words(2987384605010),
                         'dwa biliony dziewięćset osiemdziesiąt siedem '
                         'miliardów trzysta osiemdziesiąt cztery miliony'
                         ' sześćset pięć tysięcy dziesięć ')
        self.assertEqual(number_to_words(5987384605010),
                         'pięć bilionów dziewięćset osiemdziesiąt siedem '
                         'miliardów trzysta osiemdziesiąt cztery miliony '
                         'sześćset pięć tysięcy dziesięć ')

    def test_number_to_words_grammar_groups_billiard(self):
        self.assertEqual(number_to_words(1090807384605010),
                         'jeden biliard dziewięćdziesiąt bilionów osiemset '
                         'siedem miliardów trzysta osiemdziesiąt cztery '
                         'miliony sześćset pięć tysięcy dziesięć ')
        self.assertEqual(number_to_words(2090807384605010),
                         'dwa biliardy dziewięćdziesiąt bilionów osiemset '
                         'siedem miliardów trzysta osiemdziesiąt cztery '
                         'miliony sześćset pięć tysięcy dziesięć ')
        self.assertEqual(number_to_words(5090807384605010),
                         'pięć biliardów dziewięćdziesiąt bilionów osiemset '
                         'siedem miliardów trzysta osiemdziesiąt cztery '
                         'miliony sześćset pięć tysięcy dziesięć ')

    def test_number_to_words_grammar_groups_trillion(self):
        self.assertEqual(number_to_words(1090807030804605010),
                         'jeden trylion dziewięćdziesiąt biliardów osiemset '
                         'siedem bilionów trzydzieści miliardów osiemset '
                         'cztery miliony sześćset pięć tysięcy dziesięć ')


if __name__ == "__main__":
    unittest.main(verbosity=2)
