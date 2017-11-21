from parsers.swift.BuiltinTypes import BuiltinTypes


class ImmutableParser:
    def __init__(self, tokens):
        self.structure = {}
        self.inputTokens = tokens
        self.letPiece = ''
        self.variable_name = ''
        self.variable_type = BuiltinTypes.Unknown
        self.variable_type_name = ''
        self.variable_value = ''
        self.isOptional = False

    def __str__(self):
        return "code: {0} \r\n " \
               "variable_name: {1} \r\n " \
               "variable_type: {2} \r\n " \
               "variable_type_name: {3} \r\n " \
               "value: {4} \r\n " \
               "isOptional: {5} ".format(self.letPiece, self.variable_name, self.variable_type, self.variable_type_name, self.variable_value, self.isOptional)

    def parse(self):
        should_declare_type = False
        should_specify_value = False
        should_specify_instance = False

        for token in self.inputTokens:
            if str(token[0]) == 'Token.Name.Variable':
                self.variable_name = token[1]

            elif str(token[0]) == 'Token.Name.Builtin':
                self.variable_type = BuiltinTypes[token[1]]

            elif str(token[0]) == 'Token.Name':
                if should_declare_type:
                    self.variable_type = BuiltinTypes.Class
                    self.variable_type_name = token[1]
                elif should_specify_instance:
                    self.variable_value += token[1]

            elif str(token[0]).startswith('Token.Literal'):
                if should_specify_value:
                    self.variable_value += token[1]
                    if self.variable_type == BuiltinTypes.Unknown:
                        ind = str(token[0]).rindex('.') + 1
                        self.variable_type = BuiltinTypes[str(token[0])[ind:]]

            elif str(token[0]) == 'Token.Text':
                if token[1] == '\n':
                    break
                elif should_declare_type and self.variable_type != BuiltinTypes.Unknown:
                    should_declare_type = False
                elif should_specify_instance:
                    self.variable_value += token[1]
                elif should_specify_value and self.variable_value.__len__() > 0:
                    should_specify_value = False

            elif str(token[0]) == 'Token.Punctuation':  # should be the last
                if token[1] == ':':
                    should_declare_type = True
                elif token[1] == '=':
                    if self.variable_type == BuiltinTypes.Class:
                        should_specify_instance = True
                    else:
                        should_specify_value = True
                elif token[1] == ')':
                    self.variable_value += token[1]
                    should_specify_instance = False
                elif should_specify_instance:
                    self.variable_value += token[1]
                elif token[1] == '?' and should_declare_type:
                    self.isOptional = True
                    should_declare_type = False

            self.letPiece += token[1]
