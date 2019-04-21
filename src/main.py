from src.lexer import Lexer
from src.parser import Parser



text_input = ""
with open("input.txt", "r") as f:
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