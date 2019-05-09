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
        # command separator
        self.lexer.add('DOT', r'\.')
        # argument separator
        self.lexer.add("COMMA", r'\,')
        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        # variable name like response_time or latencySegID
        self.lexer.add('VARIABLE', r'(_|[a-zA-Z])(_|[a-zA-Z]|[0-9])*')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        # # Variable(as a type, so int, string, number etc)
        # self.lexer.add('VARIABLE', r'Zmienna')
        # ++
        self.lexer.add('INCREMENT', r'Zwiększ')
        # --
        self.lexer.add('DECREMENT', r'Zmniejsz')
        # +/-
        self.lexer.add('ADDSUB_HELPER', r'o')
         # * /
        self.lexer.add('DIVMUL_HELPER', r'przez')
        # assignment 
        self.lexer.add('ASSIGN', r'jest równa')
        # string
        self.lexer.add("STRING", r'\"[^\"]*\"')
        
        ###
        #comparisons
        ###
        #bigger >
        self.lexer.add('BIGGER', r'jest większe')
        #smaller <
        self.lexer.add('SAMLLLER', r'jest mniejsze')
        #equal ==
        self.lexer.add('EQUAL', r'równa się')
        #!= differ
        self.lexer.add('DIFFER', r'jest różne od')
        
        ###
        #if
        ###
        
        ###
        #for
        ###


        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()