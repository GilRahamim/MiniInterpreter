# ASTNodes.py

class ProgramNode:
    def __init__(self, statements):
        self.statements = statements

class AssignmentNode:
    def __init__(self, var_name, expression):
        self.var_name = var_name
        self.expression = expression

class ExpressionNode:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class TermNode(ExpressionNode):
    pass

class FactorNode:
    def __init__(self, value):
        self.value = value

class IfStatementNode:
    def __init__(self, condition, if_block, else_block=None):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block

class WhileStatementNode:
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

class BlockNode:
    def __init__(self, statements):
        self.statements = statements
