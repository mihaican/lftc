class Symbol:
    def __init__(self, value):
        self.father = -1
        self.sibling = -1
        self.value = value
        self.production = -1

    def __str__(self):
        return f"Value= {self.value}; Sibling= {self.sibling}; Father= {self.father}; Prod= {self.production}"
