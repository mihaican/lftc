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

def assign_token_codes(tokens, starting_code):
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
    numeric_pattern = r"^(0|[+\-]?[1-9][0-9]*|[+\-]?[1-9][0-9]*\.[0.9]+)$"
    char_pattern = r"^\'[a-zA-Z0-9_?!#*./%+=<>;)(}{ ]\'"
    string_pattern = r"^\"[a-zA-Z0-9_?!#*./%+=<>;)(}{ ]+\""
    return any(re.match(pattern, token) for pattern in [numeric_pattern, char_pattern, string_pattern])

def get_code_for_token(token):
    return token_codes.get(token)

def initialize_token_codes():
    global token_codes
    token_codes = HashTable()
    token_codes.put("identifier", 0)
    token_codes.put("constant", 1)
    assign_token_codes(keywords, 2)
    assign_token_codes(operators, len(token_codes))
    assign_token_codes(delimiters, len(token_codes) + len(operators))

def analyze_program(file_name):
    symbol_table = HashTable()
    pif = [] 
    lexical_errors = False
    
    with open(file_name, 'r') as program_file:
        line_number = 1
        for line in program_file:
            tokens = re.findall(r"[\w]+|[\(\)\;\{\}\[\]\t\n\s]|[=+-/\*%]+|\>\=|\<\=|\=\=|\!\=|\|\|", line)
            for token in tokens:
                if is_identifier(token) and not is_keyword(token):
                    symbol_table.put(token, "identifier")
                    pif.append((token, 0)) 
                elif is_keyword(token):
                    pif.append((token, token_codes.get(token)))
                elif is_operator(token):
                    pif.append((token, token_codes.get(token)))
                elif is_delimiter(token):
                    pif.append((token, token_codes.get(token)))
                elif is_constant(token):
                    pif.append((token, token_codes.get("constant")))
                else:
                    print(f"Lexical error at line {line_number}: Invalid token '{token}'")
                    lexical_errors = True
                line_number += 1

    if lexical_errors:
        return None, None
    return symbol_table, pif

def write_symbol_table_to_file(symbol_table, output_file_name):
    with open(output_file_name, 'w') as output_file:
        cnt=-1
        for entry in symbol_table.table:
            if entry is not None:
                cnt=cnt+1
                for key, value in entry:
                    if value == "identifier":
                        output_file.write(f"{cnt}   {key} -> {value}\n ")

def write_pif_to_file(pif, output_file_name):
    with open(output_file_name, 'w') as output_file:
        for entry in pif:
            token, code = entry
            if code!=52 and code != 54:
              output_file.write(f"{token} -> {code}\n")

keywords = ["invoc", "bool", "float", "string", "char", "for", "while", "ciki", "else", "scrie_pe_cer", "return"]
operators = ["++", "+", "-", "**", "*", "/", "%", "=", "==", "!=", "<", ">", "<=", ">=", "||", "!"]
delimiters = ["(", ")", ";", "{", "}", "[", "]", " ", "\t", "\n"]
token_codes = HashTable()

initialize_token_codes()

symbol_table, pif = analyze_program("p1.txt")

if symbol_table is not None:
    print("Lexically correct")
    write_symbol_table_to_file(symbol_table, "sym.out")
    write_pif_to_file(pif, "pif.out")
else:
    print("Lexical errors found")
