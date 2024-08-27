
from Lexer import *
from Parser import *
from Semantic import *
from Functions import *

def print_ast_tree(node, prefix="", is_last=True):
    """
    Print the AST tree in a hierarchical format.

    Args:
    node: The current node in the AST.
    prefix (str): The prefix to use for the current line.
    is_last (bool): Whether the current node is the last child of its parent.
    """
    if node is None:
        return

    Print(Concat(prefix, "`- " if is_last else "|- "), end="")
    new_prefix = Concat(prefix, "   " if is_last else "|  ")

    if isinstance(node, ProgramNode):
        Print("Program")
        for i, statement in enumerate(node.statements):
            print_ast_tree(statement, new_prefix, Equal(i, Sub(Length(node.statements), 1)))
    elif isinstance(node, ExpressionNode):
        Print(Concat("Expression (", node.operator, ")"))
        print_ast_tree(node.left, new_prefix, False)
        if isinstance(node.right, list):
            for i, arg in enumerate(node.right):
                print_ast_tree(arg, new_prefix, Equal(i, Sub(Length(node.right), 1)))
        else:
            print_ast_tree(node.right, new_prefix, True)
    elif isinstance(node, FactorNode):
        Print(Concat("Factor: ", str(node.value)))
    elif isinstance(node, IfStatementNode):
        Print("If Statement")
        print_ast_tree(node.condition, new_prefix, False)
        print_ast_tree(node.if_block, new_prefix, node.else_block is None)
        if node.else_block:
            print_ast_tree(node.else_block, new_prefix, True)
    elif isinstance(node, WhileStatementNode):
        Print("While Statement")
        print_ast_tree(node.condition, new_prefix, False)
        print_ast_tree(node.block, new_prefix, True)
    elif isinstance(node, BlockNode):
        Print("Block")
        for i, statement in enumerate(node.statements):
            print_ast_tree(statement, new_prefix, Equal(i, Sub(Length(node.statements), 1)))
    else:
        Print(Concat("Unknown Node Type: ", str(type(node))))

def run_tests():
    """
    Run a series of test cases to verify the functionality of the interpreter.
    """
    test_cases = [
        "Assign(x, 5)",
        "Assign(x, 10) Assign(y, Add(x, Mul(2, 3)))",
        "Assign(x, 7) If(Greater(x, 5), Assign(y, Sub(x, 1)), Assign(y, Add(x, 1)))",
        "Assign(y, 1) While(Smaller(y, 5), Assign(y, Add(y, 1)))",
        "Assign(a, 1) Assign(b, 2) Assign(result, Add(a, b))",
        "Assign(name, $John$) Assign(greeting, Concat($Hello, $, name))",
        "Assign(x, 5) Assign(y, 3) Assign(result, Greater(x, y))"
    ]

    for i, test_code in enumerate(test_cases):
        Print(Concat("\nRunning Test ", str(Add(i, 1)), ":"))
        Print(Concat("Code: ", test_code))

        tokens = tokenize(test_code)
        ast = Parser.parse(tokens)
        Print("\nGenerated AST Tree:")
        print_ast_tree(ast)

        Print("\nPerforming Semantic Analysis:")
        semantic_analyzer = SemanticAnalyzer()
        try:
            semantic_analyzer.analyze(ast)
            Print(semantic_analyzer.get_summary())
        except ValueError as e:
            Print(Concat("Semantic Analysis: Failed - ", str(e)))

def main():
    """
    The main entry point of the program. Runs the test suite.
    """
    run_tests()

if __name__ == "__main__":
    main()