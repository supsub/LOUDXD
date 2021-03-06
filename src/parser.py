from rply import ParserGenerator
from src.ast import *


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'DOT', 'SUM', 'SUB', 'VARIABLE', 'ASSIGN', 'INCREMENT', 'DECREMENT',
             'STRING', 'COMMA', 'FORMAT', 'ADDSUB_HELPER',
             'BIGGER', 'SMALLER', 'EQUAL', 'DIFFER',
             'IF', 'ELSE', 'START_BLOCK', 'END_BLOCK', 'SEPARATOR'
             ],
            precedence=[
                ('left', ['SUM', 'SUB', 'BIGGER', 'SMALLER', 'EQUAL', 'DIFFER']),
            ]
        )

    def parse(self):

        @self.pg.production('statements : ')
        def statements_end(p):
            return Statements(None, None)

        @self.pg.production('statements : statement DOT statements')
        def statements(p):
            return Statements(p[0], p[2])

        @self.pg.production('block_statements : statement SEPARATOR block_statements')
        def block_statements(p):
            return Statements(p[0], p[2])

        @self.pg.production('block_statements : statement')
        def block_statements_end(p):
            return Statements(p[0], None)

        @self.pg.production('statement : print_statement')
        @self.pg.production('statement : assignment_statement')
        @self.pg.production('statement : increment_statement')
        @self.pg.production('statement : decrement_statement')
        @self.pg.production('statement : if_statement')
        def statement(p):
            return p[0]

        @self.pg.production('print_statement : PRINT expression')
        @self.pg.production('print_statement : PRINT string')
        def print_statement(p):
            return Print(p[1])

        @self.pg.production('assignment_statement : VARIABLE ASSIGN expression')
        def assignment_statement(p):
            return Assignment(Identifier(p[0].value), p[2])

        ###
        # FOR STATEMENT
        ###

        ###
        # IF STATEMENT
        ###

        @self.pg.production('if_statement : IF expression START_BLOCK block_statements DOT END_BLOCK')
        def if_statement(p):
            return IfStatement(p[1], Statements(None, p[3]), None)

        @self.pg.production('if_statement : IF expression START_BLOCK block_statements DOT ' +
                            'ELSE  block_statements DOT END_BLOCK')
        def if_statement(p):
            return IfStatement(p[1], Statements(None, p[3]), Statements(None, p[6]))

        # INCREMENT
        @self.pg.production('increment_statement : INCREMENT VARIABLE ADDSUB_HELPER expression')
        def increment_statement(p):
            return Increment(p[1], p[3])

        # DECREMENT
        @self.pg.production('decrement_statement : DECREMENT VARIABLE ADDSUB_HELPER expression')
        def decrement_statement(p):
            return Decrement(p[1], p[3])

        # STRING FORMATTING
        @self.pg.production('string : STRING COMMA FORMAT expressions')
        def string_formatted(p):
            return String(p[0].value, p[3])

        @self.pg.production('expressions : expression')
        def expressions_to_single(p):
            return [p[0]]

        @self.pg.production('expressions : expression COMMA expressions')
        def expressions_fork(p):
            return [p[0]] + [p[2]]

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression BIGGER expression')
        @self.pg.production('expression : expression SMALLER expression')
        @self.pg.production('expression : expression EQUAL expression')
        @self.pg.production('expression : expression DIFFER expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)
            elif operator.gettokentype() == 'BIGGER':
                return Bigger(left, right)
            elif operator.gettokentype() == 'SMALLER':
                return Smaller(left, right)
            elif operator.gettokentype() == 'EQUAL':
                return Equal(left, right)
            elif operator.gettokentype() == 'DIFFER':
                return NtEqual(left, right)
            else:
                raise AssertionError("Niemożliwe")

        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def expression_paren(p):
            return p[1]

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)

        @self.pg.production('expression : VARIABLE')
        def identifier(p):
            return Identifier(p[0])

        @self.pg.production('expression : STRING')
        def expression_to_string(p):
            return String(p[0].value)

        @self.pg.error
        def error_handle(token):
            line = token.getsourcepos().lineno
            column = token.getsourcepos().colno
            raise SyntaxError("Bład składniowy w linijce nr {}, kolumnie nr {}".format(line, column))

    def get_parser(self):
        return self.pg.build()
