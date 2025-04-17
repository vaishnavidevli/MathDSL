
from mathdsl.ast_nodes import *
from mathdsl.lexer import tokenize

class Parser:
    def __init__(self, tokens):
        self.tokens = list(tokens)
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else (None, None)

    def eat(self, kind=None):
        token = self.peek()
        if kind and token[0] != kind:
            raise SyntaxError(f'Expected {kind}, got {token}')
        self.pos += 1
        return token

    def parse(self):
        tok, val = self.peek()
        if tok == 'IDENT':
            if self.tokens[self.pos + 1][1] == '=':
                return self.assignment()
            elif self.tokens[self.pos + 1][0] == 'LPAREN':
                return self.function_call()
        return self.expr()

    def assignment(self):
        name = self.eat('IDENT')[1]
        self.eat('OP')
        value = self.expr()
        return Assign(name, value)

    def function_call(self):
        name = self.eat('IDENT')[1]
        self.eat('LPAREN')
        args = []
        while self.peek()[0] != 'RPAREN':
            args.append(self.expr())
            if self.peek()[0] == 'COMMA':
                self.eat('COMMA')
        self.eat('RPAREN')
        return FuncCall(name, args)

    def expr(self):
        return self.additive()

    def additive(self):
        node = self.multiplicative()
        while self.peek()[1] in ('+', '-'):
            op = self.eat('OP')[1]
            right = self.multiplicative()
            node = BinOp(node, op, right)
        return node

    def multiplicative(self):
        node = self.exponent()
        while self.peek()[1] in ('*', '/'):
            op = self.eat('OP')[1]
            right = self.exponent()
            node = BinOp(node, op, right)
        return node

    def exponent(self):
        node = self.factor()
        while self.peek()[1] == '^':
            op = self.eat('OP')[1]
            right = self.factor()
            node = BinOp(node, op, right)
        return node

    def factor(self):
        tok, val = self.peek()
        if tok == 'NUMBER':
            return Number(self.eat()[1])
        elif tok == 'IDENT':
            return Var(self.eat()[1])
        elif tok == 'LPAREN':
            self.eat()
            expr = self.expr()
            self.eat('RPAREN')
            return expr
        raise SyntaxError('Invalid syntax')
