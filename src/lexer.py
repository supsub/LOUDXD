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
        ###
        #if
        ###
        self.lexer.add('IF', r'Jeżeli')        
        self.lexer.add('START_BLOCK', r'wykonaj')       
        ###
        #for
        ###
        # Semi Colon
        self.lexer.add('DOT', r'\.')
        # Operators +,-
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        # 
        self.lexer.add('INCREMENT', r'Zwiększ')
        # 
        self.lexer.add('DECREMENT', r'Zmniejsz')
        # +,- operations helper 
        self.lexer.add('ADDSUB_HELPER', r'o')
        # *,/ operations helper
        self.lexer.add('DIVMUL_HELPER', r'przez')
        # assignment
        self.lexer.add('ASSIGN', r'jest równe')
        #bigger >
        self.lexer.add('BIGGER', r'jest wieksze od')
        #smaller <
        self.lexer.add('SMALLER', r'jest mniejsze od')
        #equal ==
        self.lexer.add('EQUAL', r'równa się')
        #!= differ
        self.lexer.add('DIFFER', r'jest różne od')
            
        #variable name, ex. response_time or latencySegID  
        self.lexer.add('VARIABLE', r'(_|[a-zA-Z])(_|[a-zA-Z]|[0-9])*')

        self.lexer.add("STRING", r'\"[^\"]*\"')

        self.lexer.add("COMMA", r'\,')

        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()