

class ProgramNode:
    """
    Represents the root node of the Abstract Syntax Tree (AST).

    Attributes:
    statements (list): A list of statement nodes in the program.
    """
    def __init__(self, statements):
        self.statements = statements

    def __eq__(self, other):
        if isinstance(other, ProgramNode):
            return self.statements == other.statements
        return False

    def __repr__(self):
        return f"ProgramNode({self.statements})"

class AssignmentNode:
    """
    Represents an assignment statement in the AST.

    Attributes:
    var_name (str): The name of the variable being assigned.
    expression: The expression being assigned to the variable.
    """
    def __init__(self, var_name, expression):
        self.var_name = var_name
        self.expression = expression

    def __eq__(self, other):
        if isinstance(other, AssignmentNode):
            return self.var_name == other.var_name and self.expression == other.expression
        return False

    def __repr__(self):
        return f"AssignmentNode({self.var_name}, {self.expression})"

class ExpressionNode:
    """
    Represents an expression in the AST.

    Attributes:
    left: The left operand of the expression.
    operator (str): The operator of the expression.
    right: The right operand of the expression.
    """
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __eq__(self, other):
        if isinstance(other, ExpressionNode):
            return self.left == other.left and self.operator == other.operator and self.right == other.right
        return False

    def __repr__(self):
        return f"ExpressionNode({self.left}, {self.operator}, {self.right})"

class FactorNode:
    """
    Represents a factor (literal value or variable) in the AST.

    Attributes:
    value: The value of the factor.
    """
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, FactorNode):
            return self.value == other.value
        return False

    def __repr__(self):
        return f"FactorNode({self.value})"

class IfStatementNode:
    """
    Represents an if statement in the AST.

    Attributes:
    condition: The condition of the if statement.
    if_block: The block of code to execute if the condition is true.
    else_block: The block of code to execute if the condition is false (optional).
    """
    def __init__(self, condition, if_block, else_block=None):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block

    def __eq__(self, other):
        if isinstance(other, IfStatementNode):
            return (self.condition == other.condition and
                    self.if_block == other.if_block and
                    self.else_block == other.else_block)
        return False

    def __repr__(self):
        return f"IfStatementNode({self.condition}, {self.if_block}, {self.else_block})"

class WhileStatementNode:
    """
    Represents a while loop in the AST.

    Attributes:
    condition: The condition of the while loop.
    block: The block of code to execute while the condition is true.
    """
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

    def __eq__(self, other):
        if isinstance(other, WhileStatementNode):
            return self.condition == other.condition and self.block == other.block
        return False

    def __repr__(self):
        return f"WhileStatementNode({self.condition}, {self.block})"

class BlockNode:
    """
    Represents a block of statements in the AST.

    Attributes:
    statements (list): A list of statement nodes in the block.
    """
    def __init__(self, statements):
        self.statements = statements

    def __eq__(self, other):
        if isinstance(other, BlockNode):
            return self.statements == other.statements
        return False

    def __repr__(self):
        return f"BlockNode({self.statements})"