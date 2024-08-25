from AST import *
def __init__(self, tokens):
    self.tokens = tokens
    self.current_token = None
    self.pos = -1
    self.advance()


def advance(self):
    self.pos += 1
    if self.pos < len(self.tokens):
        self.current_token = self.tokens[self.pos]
    else:
        self.current_token = None


def parse(self):
    statements = []
    while self.current_token is not None:
        statements.append(self.statement())
    return ProgramNode(statements)


def statement(self):
    if self.current_token[0] == 'IDENTIFIER' and self.peek_next() == '=':
        return self.assignment()
    elif self.current_token[0] == 'KEYWORD' and self.current_token[1] == 'if':
        return self.if_statement()
    elif self.current_token[0] == 'KEYWORD' and self.current_token[1] == 'while':
        return self.while_statement()
    else:
        return self.expression()


def assignment(self):
    var_name = self.current_token[1]
    self.advance()  # skip identifier
    self.advance()  # skip '='
    expr = self.expression()
    return AssignmentNode(var_name, expr)


def expression(self):
    left = self.term()
    while self.current_token is not None and self.current_token[1] in ('+', '-'):
        operator = self.current_token[1]
        self.advance()
        right = self.term()
        left = ExpressionNode(left, operator, right)
    return left


def term(self):
    left = self.factor()
    while self.current_token is not None and self.current_token[1] in ('*', '/'):
        operator = self.current_token[1]
        self.advance()
        right = self.factor()
        left = TermNode(left, operator, right)
    return left


def factor(self):
    token_type, token_value = self.current_token
    if token_type == 'INTEGER':
        self.advance()
        return FactorNode(int(token_value))
    elif token_type == 'IDENTIFIER':
        self.advance()
        return FactorNode(token_value)
    elif token_value == '(':
        self.advance()
        expr = self.expression()
        if self.current_token[1] == ')':
            self.advance()
            return expr
        else:
            raise SyntaxError("Expected ')'")
    else:
        raise SyntaxError(f"Unexpected token: {token_value}")


def if_statement(self):
    self.advance()  # Skip 'if'
    condition = self.expression()
    if_block = self.block()
    else_block = None
    if self.current_token is not None and self.current_token[1] == 'else':
        self.advance()  # Skip 'else'
        else_block = self.block()
    return IfStatementNode(condition, if_block, else_block)


def while_statement(self):
    self.advance()  # Skip 'while'
    condition = self.expression()
    block = self.block()
    return WhileStatementNode(condition, block)


def block(self):
    if self.current_token[1] != '{':
        raise SyntaxError("Expected '{'")
    self.advance()  # Skip '{'
    statements = []
    while self.current_token is not None and self.current_token[1] != '}':
        statements.append(self.statement())
    if self.current_token[1] == '}':
        self.advance()  # Skip '}'
    else:
        raise SyntaxError("Expected '}'")
    return BlockNode(statements)


def peek_next(self):
    if self.pos + 1 < len(self.tokens):
        return self.tokens[self.pos + 1][1]
    return None
