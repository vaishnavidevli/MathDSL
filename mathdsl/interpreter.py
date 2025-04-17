# from mathdsl.ast_nodes import *
# import math
#
# env = {}
#
# def eval_node(node):
#     if isinstance(node, Number):
#         return node.value
#     elif isinstance(node, Var):
#         return env.get(node.name, 0)
#     elif isinstance(node, BinOp):
#         l, r = eval_node(node.left), eval_node(node.right)
#         return eval_op(node.op, l, r)
#     elif isinstance(node, Assign):
#         val = eval_node(node.value)
#         env[node.name] = val
#         return val
#     elif isinstance(node, FuncCall):
#         if node.name == 'plot':
#             from mathdsl.plotter import plot
#             return plot(node.args)
#         elif node.name == 'solve':
#             from mathdsl.symmath import solve_equation
#             return solve_equation(node.args[0])
#
# def eval_op(op, a, b):
#     if op == '^':  # Exponentiation is handled here
#         return a ** b
#     return {
#         '+': a + b,
#         '-': a - b,
#         '*': a * b,
#         '/': a / b
#     }[op]

from mathdsl.ast_nodes import *
import math
from mathdsl.symmath import solve_equation, differentiate, integrate  # Import the updated functions

env = {}

def eval_node(node):
    if isinstance(node, Number):
        return node.value
    elif isinstance(node, Var):
        return env.get(node.name, 0)
    elif isinstance(node, BinOp):
        l, r = eval_node(node.left), eval_node(node.right)
        return eval_op(node.op, l, r)
    elif isinstance(node, Assign):
        val = eval_node(node.value)
        env[node.name] = val
        return val
    elif isinstance(node, FuncCall):
        if node.name == 'plot':
            from mathdsl.plotter import plot
            return plot(node.args)
        elif node.name == 'solve':
            return solve_equation(node.args[0], eval_node)  # Pass eval_node here
        elif node.name == 'differentiate':
            return differentiate(node.args[0], eval_node)  # Pass eval_node here
        elif node.name == 'integrate':
            return integrate(node.args[0], eval_node)  # Pass eval_node here

def eval_op(op, a, b):
    return {'+': a+b, '-': a-b, '*': a*b, '/': a/b, '^': a**b}[op]
