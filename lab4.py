class FiniteAutomaton:
    def __init__(self, filename):
        self.states, self.alphabet, self.transition = [], [], {}
        self.initial_state, self.final_states = "", []
        self.read_configuration(filename)

    def read_configuration(self, filename):
        with open(filename) as file:
            self.states = self.parse_line(file.readline())
            self.alphabet = self.parse_line(file.readline())
            self.initial_state = file.readline().strip()
            self.final_states = self.parse_line(file.readline())
            self.transition = {tuple(pair): [result] for pair, result in (self.parse_transition_line(line) for line in file)}

    @staticmethod
    def parse_line(line):
        return [elem.strip() for elem in line.strip().replace(" ", "").split(",")] if line.strip() else []

    @staticmethod
    def parse_transition_line(line):
        pair, result = (elem.strip() for elem in line.strip().replace(" ", "").split("="))
        if not (pair and result):
            raise RuntimeError("Error while parsing transition functions")
        return tuple(pair.split(",")), result

    def is_deterministic(self):
        return not any(len(values) > 1 for values in self.transition.values())

    def check_sequence(self, sequence):
        if self.is_deterministic():
            state = self.initial_state
            transitions = self.transition.get
            return all((state := transitions((state, str(path)), [None])[0]) is not None for path in sequence) and state in self.final_states
        return False

    


def user_menu(automaton):
    while True:
        print_menu()
        choice = input("Enter your choice (0-7): ")
        if choice == "0":
            break
        elif choice == "6":
            print(check_sequence(automaton))
        elif choice in MENU_OPTIONS:
            print(getattr(automaton, MENU_OPTIONS[choice]))
        else:
            print("Invalid action!")


def check_sequence(automaton):
    sequence = input("Please enter the sequence (comma-separated): ").strip().replace(" ", "").split(",")
    return automaton.check_sequence(sequence)


def print_menu():
    print("\n".join(MENU_OPTIONS.values()))


MENU_OPTIONS = {
    "1": "states",
    "2": "alphabet",
    "3": "transition",
    "4": "initial_state",
    "5": "final_states",
    "6": "check_sequence",
    "0": "exit"
}


def start():
    automaton = FiniteAutomaton("fa.in")
    user_menu(automaton)
    print(f"Finite automaton is deterministic: {automaton.is_deterministic()}")


start()