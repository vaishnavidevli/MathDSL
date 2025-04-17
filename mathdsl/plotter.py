
import matplotlib.pyplot as plt
import numpy as np
from mathdsl.interpreter import env, eval_node

def plot(args):
    expr = args[0]
    x_vals = np.linspace(-10, 10, 100)
    y_vals = []

    for x in x_vals:
        env['x'] = x
        y = eval_node(expr)
        y_vals.append(y)

    plt.plot(x_vals, y_vals)
    plt.grid()
    plt.show()
