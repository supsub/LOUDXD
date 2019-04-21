from rply import ParserGenerator
from src.ast import Number, Sum, Sub, Print, Statement, Statements, Assignment, Identifier


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB','IDENTIFIER','EQUALS'],
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

        @self.pg.production('statement : print_statement SEMI_COLON')
        @self.pg.production('statement : assignment_statement SEMI_COLON')
        def statement(p):
            return p[0]

        @self.pg.production('print_statement : PRINT OPEN_PAREN expression CLOSE_PAREN')
        def print_statement(p):
            return Print(p[2])

        @self.pg.production('assignment_statement : IDENTIFIER EQUALS expression')
        def assignment_statement(p):
            return Assignment(Identifier(p[0].value),p[2])

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