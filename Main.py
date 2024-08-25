from Lexer import tokenize
from Parser import parse
import Semantic
from AST import ProgramNode, AssignmentNode, ExpressionNode, FactorNode, IfStatementNode, WhileStatementNode, BlockNode


def run_tests():
    test_cases = [
        {
            "code": "x = 5",
            "expected_ast": ProgramNode([AssignmentNode(var_name="x", expression=FactorNode(5))])
        },
        {
            "code": "y = x + 2 * 3",
            "expected_ast": ProgramNode([
                AssignmentNode(
                    var_name="y",
                    expression=ExpressionNode(
                        left=FactorNode("x"),
                        operator="+",
                        right=ExpressionNode(
                            left=FactorNode(2),
                            operator="*",
                            right=FactorNode(3)
                        )
                    )
                )
            ])
        },
        {
            "code": "if x > 5 { y = x - 1 } else { y = x + 1 }",
            "expected_ast": ProgramNode([
                IfStatementNode(
                    condition=ExpressionNode(
                        left=FactorNode("x"),
                        operator=">",
                        right=FactorNode(5)
                    ),
                    if_block=BlockNode([
                        AssignmentNode(var_name="y", expression=ExpressionNode(
                            left=FactorNode("x"),
                            operator="-",
                            right=FactorNode(1)
                        ))
                    ]),
                    else_block=BlockNode([
                        AssignmentNode(var_name="y", expression=ExpressionNode(
                            left=FactorNode("x"),
                            operator="+",
                            right=FactorNode(1)
                        ))
                    ])
                )
            ])
        },
        {
            "code": "while y < 10 { y = y + 1 }",
            "expected_ast": ProgramNode([
                WhileStatementNode(
                    condition=ExpressionNode(
                        left=FactorNode("y"),
                        operator="<",
                        right=FactorNode(10)
                    ),
                    block=BlockNode([
                        AssignmentNode(var_name="y", expression=ExpressionNode(
                            left=FactorNode("y"),
                            operator="+",
                            right=FactorNode(1)
                        ))
                    ])
                )
            ])
        },
        {
            "code": "result = (a + b) * (c - d) / e",
            "expected_ast": ProgramNode([
                AssignmentNode(
                    var_name="result",
                    expression=ExpressionNode(
                        left=ExpressionNode(
                            left=ExpressionNode(
                                left=FactorNode("a"),
                                operator="+",
                                right=FactorNode("b")
                            ),
                            operator="*",
                            right=ExpressionNode(
                                left=FactorNode("c"),
                                operator="-",
                                right=FactorNode("d")
                            )
                        ),
                        operator="/",
                        right=FactorNode("e")
                    )
                )
            ])
        }
    ]

    for i, test in enumerate(test_cases):
        print(f"Running Test {i + 1}: {test['code']}")
        tokens = tokenize(test["code"])  # Directly call the tokenize function
        parser = Parser(tokens)
        ast = parser.parse()

        if ast == test["expected_ast"]:
            print(f"Test {i + 1} Passed!\n")
        else:
            print(f"Test {i + 1} Failed.\nExpected: {test['expected_ast']}\nGot: {ast}\n")


def main():
    run_tests()

if __name__ == "__main__":
    main()