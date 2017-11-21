from pygments import lex
from pygments.lexers.objective import SwiftLexer

from parsers import SwiftParser

def main():
    swift_parser = SwiftParser.SwiftParser()
    file = open("samples/letSample.txt", "r")
    text = file.readlines()
    all_text_lines = ''
    for str in text:
        all_text_lines += str
    swift_lexer = SwiftLexer()
    smth = lex(all_text_lines, swift_lexer)
    parse(swift_parser, smth)  # comment that to get all tokens printed

    for item in smth:
        print(item)


def parse(parser, tokens):
    return parser.parse(tokens)


main()
