def number_to_words(number):
    """Convert int number into string - return word in Polish"""

    ONES = ('', 'jeden ', 'dwa ', 'trzy ', 'cztery ', 'pięć ',
            'sześć ', 'siedem ', 'osiem ', 'dziewięć ')

    TENS = ('', 'jedenaście ', 'dwanaście ', 'trzynaście ', 'czternaście ',
            'piętnaście ', 'szesnaście ', 'siedemnaście ', 'osiemnaście ',
            'dziewiętnaście ')

    TWENTIES = ('', 'dziesięć ', 'dwadzieścia ', 'trzydzieści ',
                  'czterdzieści ',
                'pięćdziesiąt ', 'sześćdziesiąt ', 'siedemdziesiąt ',
                'osiemdziesiąt ', 'dziewięćdziesiąt ')

    HUNDREDS = ('', 'sto ', 'dwieście ', 'trzysta ', 'czterysta ', 'pięćset ',
                'sześćset ', 'siedemset ', 'osiemset ', 'dziewięćset ')

    GRAMMAR_GROUPS = (
        ('', '', ''),
        ('tysiąc ', 'tysiące ', 'tysięcy '),
        ('milion ', 'miliony ', 'milionów '),
        ('miliard ', 'miliardy ', 'miliardów '),
        ('bilion ', 'biliony ', 'bilionów '),
        ('biliard ', 'biliardy ', 'biliardów '),
        ('trylion ', 'tryliony ', 'tryliardów ')
    )

    verbal_notation = ''

    if number == 0:
        verbal_notation = 'zero'
    if number < 0:
        sign = 'minus '
        number = -number
    else:
        sign = ''

    i = 0
    while number != 0:
        hundreds = number % 1000 // 100
        tens = number % 100 // 10
        ones = number % 10
        if tens == 1 and ones > 0:
            twenties = ones
            tens = 0
            ones = 0
        else:
            twenties = 0
        if ones == 1 and hundreds + tens + twenties == 0:
            grammar_group = 0
        elif ones in (2, 3, 4):
            grammar_group = 1
        else:
            grammar_group = 2
        if grammar_group >= 0 and hundreds + tens + twenties + ones > 0:
            verbal_notation = HUNDREDS[hundreds] + TWENTIES[tens] + \
                              TENS[twenties] + ONES[ones] + \
                              GRAMMAR_GROUPS[i][grammar_group] + verbal_notation
        i = i + 1
        number = number // 1000
    return sign + verbal_notation
