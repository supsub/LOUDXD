from src.lexer import Lexer
from src.parser import Parser


def test_test():
    source = """Zmienna a jest równa 2.
                Zwiększ a o 5.
                Wypisz na ekranie a.
                Zmienna b jest równa 4+a-(2-a).
                Zmniejsz b o b+1.
                Zmienna c jest równa "jestem sobie zmienna c".
                Wypisz na ekranie b+b.
                Wypisz na ekranie "ELO :P".
                Wypisz na ekranie "Wpisałem w puste miejsca  _, _, _!", w puste miejsce wpisz "siema",1,(2-5).
                Wypisz na ekranie "Wpisałem w puste miejsce _, _!", w puste miejsce wpisz "elo", "siemano".
                Wypisz na ekranie "zmienna a = _, zmienna b = _, zmienna c = _!", w puste miejsce wpisz a,b,c."""

    lexer = Lexer().get_lexer()
    tokens = lexer.lex(source)

    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    context = {}
    parser.parse(tokens).eval(context)