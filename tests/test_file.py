from src.lexer import Lexer
from src.parser import Parser

def test_empty():
    source = ""

    lexer = Lexer().get_lexer()
    tokens = lexer.lex(source)

    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    context = {}
    parser.parse(tokens).eval(context)

def test_test():
    source = """a jest równe 2.
                Zwiększ a o 5.
                Wypisz na ekranie a.
                b jest równe 4+a-(2-a).
                Zmniejsz b o b+1.
                c jest równe "jestem sobie zmienna c".
                Wypisz na ekranie b+b.
                Wypisz na ekranie "ELO :P".
                Wypisz na ekranie "Wpisałem w puste miejsca  _, _, _!", w puste miejsce wpisz "siema",1,(2-5).
                Wypisz na ekranie "Wpisałem w puste miejsce _, _!", w puste miejsce wpisz "elo", "siemano".
                Wypisz na ekranie "zmienna a = _, zmienna b = _, zmienna c = _!", w puste miejsce wpisz a,b,c.
                Wypisz na ekranie b jest wieksze od b.
                Wypisz na ekranie b jest mniejsze od b.
                Wypisz na ekranie b równa się b.
                Wypisz na ekranie b jest różne od b.
                Jeżeli b jest mniejsze od b to wypisz na ekranie "b<b". Tyle.
                Jeżeli a jest mniejsze od b to wypisz na ekranie "a<b". Tyle.
                Jeżeli b jest mniejsze od a to wypisz na ekranie "b<a". Tyle.
                """

    lexer = Lexer().get_lexer()
    tokens = lexer.lex(source)

    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    context = {}
    parser.parse(tokens).eval(context)

def test_if():
    source = """
                b jest równe 5.
                Wypisz na ekranie b.
                Jeżeli b równa się b to wypisz na ekranie "jestem w body" 
                oraz wypisz na ekranie "dalej w body"
                oraz wypisz na ekranie "chyba bangla". 
                Tyle.
                Wypisz na ekranie "już poza body".
                """

    lexer = Lexer().get_lexer()
    tokens = lexer.lex(source)

    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    context = {}
    parser.parse(tokens).eval(context)

def test_advanced_if():
    source = """
                Jeżeli 5 jest wieksze od 3 to 
                    jeżeli 5 jest wieksze od 4 to 
                    wypisz na ekranie "jestem w zagnieżdżonym ifie" 
                    oraz wypisz na ekranie "5 jest większe od 3 i 4". 
                    Tyle. 
                Tyle.
                Wypisz na ekranie "zagnieżdzony if działa".
                """

    lexer = Lexer().get_lexer()
    tokens = lexer.lex(source)

    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    context = {}
    parser.parse(tokens).eval(context)

def test_if_else():
    source = """
                Jeżeli 2 jest wieksze od 3 to wypisz na ekranie "jestem w ifie".
                W przeciwnym razie wypisz na ekranie "jestem w  elsie".
                Tyle.
                Wypisz na ekranie "ifelse działa".
                """

    lexer = Lexer().get_lexer()
    tokens = lexer.lex(source)

    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    context = {}
    parser.parse(tokens).eval(context)