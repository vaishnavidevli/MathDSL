# 📐 MathDSL

**MathDSL** is a Domain-Specific Language (DSL) for symbolic and numerical mathematical computation. It is designed to provide an intuitive syntax for performing complex mathematical operations like differentiation, integration, equation solving, and graphing. Under the hood, it leverages symbolic computation libraries like `SymPy` and compiles expressions to LLVM IR for efficient execution.

---

## 🚀 Features

- 📌 Simple and expressive DSL syntax
- 🧮 Symbolic computation (differentiation, integration, simplification)
- 🔎 Equation solving (linear, quadratic, etc.)
- 📊 Plotting mathematical functions and equations
- 🧠 Custom function definitions and variable assignments
- ⚡ LLVM IR generation and optimization for performance
- 🧾 Interactive REPL for experimentation

---

## 🧠 Example Syntax

```plaintext
x = 3
f(x) = x^2 + 2*x + 1
diff(f(x))         # Differentiate
integrate(f(x))    # Integrate
solve(f(x) = 0)    # Solve equation
plot(f(x))         # Plot function
