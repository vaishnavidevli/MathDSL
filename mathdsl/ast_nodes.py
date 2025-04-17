
class Number:
    def __init__(self, value): self.value = float(value)

class BinOp:
    def __init__(self, left, op, right):
        self.left, self.op, self.right = left, op, right

class Var:
    def __init__(self, name): self.name = name

class Assign:
    def __init__(self, name, value): self.name, self.value = name, value

class FuncCall:
    def __init__(self, name, args): self.name, self.args = name, args
