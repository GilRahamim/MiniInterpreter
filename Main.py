# Main.py

from Lexer import tokenize
from Parser import Parser
from AST import ProgramNode, AssignmentNode, ExpressionNode, FactorNode, IfStatementNode, WhileStatementNode, BlockNode
from Semantic import SemanticAnalyzer

def print_ast_tree(node, prefix="", is_last=True):
    if node is None:
        return

    print(prefix, end="")
    if is_last:
        print("`- ", end="")
        prefix += "   "
    else:
        print("|- ", end="")
        prefix += "|  "

    if isinstance(node, ProgramNode):
        print("Program")
        for i, statement in enumerate(node.statements):
            print_ast_tree(statement, prefix, i == len(node.statements) - 1)
    elif isinstance(node, ExpressionNode):
        print(f"Expression ({node.operator})")
        print_ast_tree(node.left, prefix, False)
        if isinstance(node.right, list):
            for i, arg in enumerate(node.right):
                print_ast_tree(arg, prefix, i == len(node.right) - 1)
        else:
            print_ast_tree(node.right, prefix, True)
    elif isinstance(node, FactorNode):
        print(f"Factor: {node.value}")
    elif isinstance(node, IfStatementNode):
        print("If Statement")
        print_ast_tree(node.condition, prefix, False)
        print_ast_tree(node.if_block, prefix, node.else_block is None)
        if node.else_block:
            print_ast_tree(node.else_block, prefix, True)
    elif isinstance(node, WhileStatementNode):
        print("While Statement")
        print_ast_tree(node.condition, prefix, False)
        print_ast_tree(node.block, prefix, True)
    elif isinstance(node, BlockNode):
        print("Block")
        for i, statement in enumerate(node.statements):
            print_ast_tree(statement, prefix, i == len(node.statements) - 1)
    else:
        print(f"Unknown Node Type: {type(node)}")

def run_tests():
    test_cases = [
        {
            "code": "Assign(x, 5)",
        },
        {
            "code": "Assign(x, 10) Assign(y, Add(x, Mul(2, 3)))",
        },
        {
            "code": "Assign(x, 7) If(Greater(x, 5), Assign(y, Sub(x, 1)), Assign(y, Add(x, 1)))",
        },
        {
            "code": "Assign(y, 1) While(Smaller(y, 10), Assign(y, Add(y, 1)))",
        },
        {
            "code": "Assign(a, 1) Assign(b, 2) Assign(c, 3) Assign(d, 4) Assign(e, 5) Assign(result, Div(Mul(Add(a, b), Sub(c, d)), e))",
        },
        {
            "code": "Assign(x, 5) Assign(y, Add(x, 3))",
        },
        {
            "code": "Assign(name, $John Doe$) Assign(greeting, Concat($Hello, $, name))",
        }
    ]

    for i, test in enumerate(test_cases):
        print(f"\nRunning Test {i + 1}: {test['code']}")
        tokens = tokenize(test["code"])
        print(f"Tokens: {tokens}")
        ast = Parser.parse(tokens)

        print("\nGenerated AST Tree:")
        print_ast_tree(ast)

        # Semantic Analysis
        print("\nPerforming Semantic Analysis:")
        semantic_analyzer = SemanticAnalyzer()
        try:
            semantic_analyzer.analyze(ast)
            print(semantic_analyzer.get_summary())
        except ValueError as e:
            print(f"Semantic Analysis: Failed - {str(e)}")

def main():
    run_tests()

if __name__ == "__main__":
    main()