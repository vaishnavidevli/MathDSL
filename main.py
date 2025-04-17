
from mathdsl.lexer import tokenize
from mathdsl.parser import Parser
from mathdsl.interpreter import eval_node

print("🔢 Math DSL REPL (type 'exit' to quit)")

while True:
    try:
        code = input('> ')
        if code in ('exit', 'quit'): break
        tokens = tokenize(code)
        parser = Parser(tokens)
        ast = parser.parse()
        result = eval_node(ast)
        if result is not None:
            print(result)
    except Exception as e:
        print(f"❌ Error: {e}")
