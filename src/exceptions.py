class Wyjatek(Exception):
    def __init__(self,token):
        self.line = token.getsourcepos().lineno
        self.column = token.getsourcepos().colno

class ZlyKlucz(Wyjatek):
    def __init__(self, token):
        Wyjatek.__init__(self,token)
        Exception.__init__(self,("Błąd w linijce nr {}, kolumnie nr {},  ".format(self.line, self.column) +
         " Nie istnieje zmienna o nazwie \"{}\".".format(token.value)))