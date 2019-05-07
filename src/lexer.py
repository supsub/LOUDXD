from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        
        #Bigger >
        self.lexer.add('BIGGER', r'>')
        
        #Smaller <
        self.lexer.add('SMALLER', r'<')
        
        #Equal ==
        self.lexer.add('EQUAL', r'==')
        
        #Not Equal !=
        self.lexer.add('NOT_EQUAL', r'!=')
        
        #For
        self.lexer.add('FOR', r'for')
        
        #If
        self.lexer.add('IF', r'if')
        
        
        
        # Print
        self.lexer.add('PRINT', r'print')
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')
        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        # Number
        self.lexer.add('NUMBER', r'\d+')

        self.lexer.add('IDENTIFIER', r'(_|[a-zA-Z])(_|[a-zA-Z]|[0-1])*')

        self.lexer.add('EQUALS', r'\=')
        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()