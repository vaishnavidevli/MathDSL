# from sympy import symbols, Eq, solve
# from mathdsl.ast_nodes import Number, Var, BinOp, Assign  # Correctly import the necessary classes
# from mathdsl.interpreter import eval_node, env
#
#
# def solve_equation(expr):
#     # Prepare the symbol 'x' for solving equations
#     x = symbols('x')
#     eq_str = to_string(expr)
#
#     # Check if the equation already has an equal sign
#     if '=' not in eq_str:
#         eq_str = eq_str + " = 0"  # Append '= 0' if no equality symbol exists
#
#     # Split the equation into left and right sides
#     lhs, rhs = eq_str.split('=')
#
#     # Solve the equation using sympy's Eq class
#     equation = Eq(eval(lhs), eval(rhs))
#     return solve(equation, x)
#
#
# def to_string(node):
#     # Convert AST nodes into a string representation
#     if isinstance(node, Number):
#         return str(node.value)
#     elif isinstance(node, Var):
#         return node.name
#     elif isinstance(node, BinOp):
#         left = to_string(node.left)
#         right = to_string(node.right)
#         # Convert ^ to ** for SymPy compatibility
#         if node.op == '^':
#             return f"({left} ** {right})"
#         return f"({left} {node.op} {right})"
#     elif isinstance(node, Assign):
#         return f"{node.name} = {to_string(node.value)}"
#     else:
#         return ""

from sympy import symbols, Eq, solve, diff, integrate as sym_integrate, sympify
from mathdsl.ast_nodes import Number, Var, BinOp, Assign

x = symbols('x')  # Global symbol

def solve_equation(expr, eval_node):
    eq_str = to_string(expr)
    if '=' not in eq_str:
        eq_str += " = 0"
    lhs, rhs = eq_str.split('=')
    equation = Eq(sympify(lhs), sympify(rhs))
    return solve(equation, x)

def differentiate(expr, eval_node):
    expr_str = to_string(expr)
    sym_expr = sympify(expr_str)
    return diff(sym_expr, x)

def integrate(expr, eval_node):
    expr_str = to_string(expr)
    sym_expr = sympify(expr_str)
    return sym_integrate(sym_expr, x)

def to_string(node):
    if isinstance(node, Number):
        return str(node.value)
    elif isinstance(node, Var):
        return node.name
    elif isinstance(node, BinOp):
        left = to_string(node.left)
        right = to_string(node.right)
        if node.op == '^':
            return f"({left} ** {right})"  # Replace ^ with **
        return f"({left} {node.op} {right})"
    elif isinstance(node, Assign):
        return f"{node.name} = {to_string(node.value)}"
    else:
        return ""
