import re

class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)
                    return
            self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def __len__(self):
        count = 0
        for entry in self.table:
            if entry:
                count += len(entry)
        return count


keywords = ["invoc", "bool", "float", "string", "char", "for", "while", "ciki", "else", "scriePeCer", "return"]
operators = ["++", "+", "-", "**", "*", "/", "%", "=", "==", "!=", "<", ">", "<=", ">=", "||", "!"]
delimiters = ["(", ")", ";", "{", "}", "[", "]", " ", "\t", "\n"]
token_codes = HashTable()


def initialize_token_codes():
    global token_codes
    token_codes.put("identifier", 0)
    token_codes.put("constant", 1)
    assign_token_codes(keywords, 2)
    assign_token_codes(operators, len(token_codes))
    assign_token_codes(delimiters, len(token_codes))

def assign_token_codes(tokens, starting_code):
    global token_codes
    code = starting_code
    for token in tokens:
        token_codes.put(token, code)
        code += 1

def is_keyword(token):
    return token in keywords

def is_operator(token):
    return token in operators

def is_part_of_operator(op):
    return op == '!' or op == '+' or op == '*' or is_operator(op)

def is_delimiter(token):
    return token in delimiters

def is_identifier(token):
    pattern = r"^[a-zA-Z]([a-zA-Z0-9_])*$"
    return bool(re.match(pattern, token))

def is_constant(token):
    numeric_pattern = r"^(0|[+\-]?[1-9][0-9]*|[+\-]?[1-9][0-9]*\.[0-9]+|[1-9][0-9]*\.[0.9]+)$"
    char_pattern = r"^\'[a-zA-Z0-9_?!#*./%+=<>;)(}{ ]\'"
    string_pattern = r"^\"[a-zA-Z0-9_?!#*./%+=<>;)(}{ ]+\""
    return any(re.match(pattern, token) for pattern in [numeric_pattern, char_pattern, string_pattern])

def get_code_for_token(token):
    return token_codes.get(token)


initialize_token_codes()
