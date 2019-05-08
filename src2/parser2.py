from rply import ParserGenerator
from src2.ast2 import Number, Sum, Sub, Print, Statement, Statements, Assignment, Identifier, Increment, Decrement


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'DOT', 'SUM', 'SUB','IDENTIFIER', 'EQUALS', 'INCREMENT', 'DECREMENT',
            #polish keywords
            'ZMIENNA','O'
             ],
            precedence=[
                ('left', ['SUM', 'SUB']),
            ]
        )

    def parse(self):

        @self.pg.production('program : statements')
        def program(p):
            return p[0]


        @self.pg.production('statements : statement statements')
        def statements(p):
            return Statements(p[0],p[1])

        @self.pg.production('statements : statement')
        def statements_end(p):
            return Statement(p[0])

        @self.pg.production('statement : print_statement DOT')
        @self.pg.production('statement : assignment_statement DOT')
        @self.pg.production('statement : increment_statement DOT')
        @self.pg.production('statement : decrement_statement DOT')
        def statement(p):
            return p[0]

        @self.pg.production('print_statement : PRINT expression')
        def print_statement(p):
            return Print(p[1])

        @self.pg.production('assignment_statement : ZMIENNA IDENTIFIER EQUALS expression')
        def assignment_statement(p):
            return Assignment(Identifier(p[1].value),p[3])

        @self.pg.production('increment_statement : INCREMENT IDENTIFIER O expression')
        def increment_statement(p):
            return Increment(p[1].value,p[3])

        @self.pg.production('decrement_statement : DECREMENT IDENTIFIER O expression')
        def decrement_statement(p):
            return Decrement(p[1].value, p[3])

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)

        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def expression_paren(p):
            return p[1]

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)

        @self.pg.production('expression : IDENTIFIER')
        def identifier(p):
            return Identifier(p[0].value)



        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()