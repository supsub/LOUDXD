from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('PRINT', r'Wypisz na ekranie')
        self.lexer.add("FORMAT", r'\w puste miejsce wpisz ')
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # Semi Colon
        self.lexer.add('DOT', r'\.')
        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        # Number
        self.lexer.add('NUMBER', r'\d+')

        self.lexer.add('ZMIENNA', r'Zmienna')

        self.lexer.add('INCREMENT', r'Zwiększ')

        self.lexer.add('DECREMENT', r'Zmniejsz')

        self.lexer.add('O', r'o')

        self.lexer.add('EQUALS', r'jest równa')

        self.lexer.add('IDENTIFIER', r'(_|[a-zA-Z])(_|[a-zA-Z]|[0-9])*')

        self.lexer.add("STRING", r'\"[^\"]*\"')

        self.lexer.add("COMMA", r'\,')



        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()