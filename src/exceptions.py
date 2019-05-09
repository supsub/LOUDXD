class Wyjatek(Exception):
    def __init__(self,token):
        self.line = token.getsourcepos().lineno
        self.column = token.getsourcepos().colno

class ZlyKlucz(Wyjatek):
    def __init__(self, token):
        Wyjatek.__init__(self,token)
        Exception.__init__(self,(f"Błąd w linijce nr {self.line}, kolumnie nr {self.column},  "
         f" Nie istnieje zmienna o nazwie \"{token.value}\"."))