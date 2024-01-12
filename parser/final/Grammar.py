class ContextFreeGrammar:
    def __init__(self):
        self.non_terminals = []
        self.terminals = []
        self.rules = {}
        self.start_symbol = None

    def terminals_list(self):
        """
        :return: List of terminal symbols.
        """
        return self.terminals

    def non_terminals_list(self):
        """
        :return: List of non-terminal symbols.
        """
        return self.non_terminals

    def start_sym(self):
        """
        :return: The start symbol.
        """
        return self.start_symbol

    def productions_for(self, non_terminal):
        """
        :param non_terminal: Non-terminal symbol to get productions for.
        :return: List of production rules for the given non-terminal.
        """
        return self.rules.get(non_terminal, [])

    def has_additional_production(self, non_terminal, production_number):
        """
        Checks if there is an additional production rule for a given non-terminal symbol.
        :param non_terminal: Non-terminal symbol to check.
        :param production_number: Current production number.
        :return: True if there is another production, False otherwise.
        """
        return self.rules[non_terminal][-1][1] != production_number

    def specific_production(self, non_terminal, production_number):
        """
        :param non_terminal: Non-terminal symbol to get the production for.
        :param production_number: The production number to retrieve.
        :return: Specific production rule if found, None otherwise.
        """
        for production in self.rules[non_terminal]:
            if production[1] == production_number:
                return production

    def load_grammar(self, file_path):
        """
        :param file_path: Path to the file containing the grammar.
        :raises ValueError: If the grammar is not a valid context-free grammar.
        """
        with open(file_path, 'r') as file:
            self.non_terminals = self._parse_line(file.readline())
            self.terminals = self._parse_line(file.readline())
            self.start_symbol = file.readline().split('=')[1].strip()
            file.readline()
            prod_rules = [line.strip() for line in file]
            self.rules = self._interpret_rules(prod_rules)

            if not self._is_valid_cfg(prod_rules):
                raise ValueError('The provided grammar is not a valid CFG')

    def display_non_terminals(self):
        """
        :return: String of non-terminal symbols.
        """
        return str(self.non_terminals)

    def display_terminals(self):
        """
        :return: String of terminal symbols.
        """
        return str(self.terminals)

    def display_start_symbol(self):
        """
        :return: String of the start symbol.
        """
        return str(self.start_symbol)

    def display_productions(self):
        """
        :return: String of production rules.
        """
        return str(self.rules)

    @staticmethod
    def _parse_line(line):
        """
        :param line: Line from the grammar file.
        :return: List of symbols extracted from the line.
        """
        parts = line.strip().split('=', 1)[1]
        if parts.strip()[-1] == ',':
            parts = [',']
        return [item.strip() for item in parts.split(',')]

    @staticmethod
    def _interpret_rules(rule_lines):
        """
        :param rule_lines: Lines from the grammar file representing the rules.
        :return: Dictionary of interpreted production rules.
        """
        productions = {}
        index = 1

        for rule in rule_lines:
            left_side, right_side = rule.split('->')
            left_side = left_side.strip()
            right_side = [val.strip() for val in right_side.split('|')]

            for production in right_side:
                if left_side in productions:
                    productions[left_side].append((production, index))
                else:
                    productions[left_side] = [(production, index)]
                index += 1
        return productions

    @staticmethod
    def _is_valid_cfg(rules):
        """
        Checks if the parsed grammar is a valid context-free grammar (CFG).
        Ensures that each production rule adheres to the format required for CFGs.
        check if the lhs of each production rule contains only a single non-terminal symbol
        :param rules: List of rules to be checked.
        :return: True if valid CFG, False otherwise.
        """
        for rule in rules:
            lhs, _ = rule.split('->')
            lhs = lhs.strip()
            if sum(element.strip() in lhs for element in lhs.split('|')) > 1:
                return False
        return True
