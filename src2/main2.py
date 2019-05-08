from src2.lexer2 import Lexer
from src2.parser2 import Parser



text_input = ""
with open("input2.txt", "r") as f:
    line = f.readline()
    while line:
        text_input+=line
        line = f.readline()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval({})