from tabulate import tabulate


class PrintParser:
    def __init__(self, tree):
        self._tree = tree

    def _generate_rows(self):
        headers = ['Index', 'Value', 'Parent', 'Left Sibling']
        rows = []
        for index, item in enumerate(self._tree):
            rows.append([index, item.value, item.father, item.sibling])
        return headers, rows

    def printToFile(self, filename):
        headers, rows = self._generate_rows()
        with open(filename, 'w') as writer:
            writer.write('\n')
            writer.write(tabulate(rows, headers, tablefmt='orgtbl'))
