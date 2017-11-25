import Parser
from parsers.swift.ImmutableParser import ImmutableParser
from parsers.swift.ParserTypes import ParserTypes
from pygments.lexers.objective import SwiftLexer
from pygments import lex


class SwiftParser(Parser.Parser):
    def __init__(self):
        super().__init__()
        self.data = []
        self.lexemAnalyzer = SwiftLexer()

    def analyzeAll(self, allstrings):
        output = []
        for line in allstrings:
            output.append(self.analyzeString(line))

    def analyzeString(self, inputline):
        tokens = lex(inputline)
        for token in tokens:
            t = token
        return 'test'

    def parse(self, tokensarray):
        skip = False
        tokens_to_parse = []
        parser_type = ParserTypes.Undefined

        for token in tokensarray:
           if token[1] == '\n':
               skip = False
               parser = self.getParser(parser_type, tokens_to_parse)
               parser.parse()
               print(parser)
               tokens_to_parse.clear()
               parser_type = ParserTypes.Undefined
           elif skip:
               tokens_to_parse.append(token)
           elif str(token[0]) == 'Token.Keyword.Declaration' and token[1] == 'let':
               parser_type = ParserTypes.Immutable
               tokens_to_parse.append(token)
               skip = True
        return ''

    def getParser(self, parserType, tokens):
        if parserType == ParserTypes.Immutable:
            return ImmutableParser(tokens)
        return ImmutableParser(tokens)