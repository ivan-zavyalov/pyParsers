from pygments import lex


class Parser:
    def __init__(self):
        self.name = 'Parser'

    def parse(self, tokensArray):
        return tokensArray

    def analyze(self, code, lexer):
        return lex(code, lexer)
