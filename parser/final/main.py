from Grammar import ContextFreeGrammar
from Parser import Parser
from PrintParser import PrintParser


def main():
    grammar = ContextFreeGrammar()
    grammar.load_grammar("g2.txt")
    parser = Parser(grammar, out_file="out2.txt", in_file="PIF.out")
    parser.parsingStrategy('')

    if parser.getState() == 'f':
        output = PrintParser(parser.getTree())
        output.printToFile('tree.txt')

if __name__ == "__main__":
    main()
