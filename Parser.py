# Parser.py

from AST import ProgramNode, ExpressionNode, FactorNode, IfStatementNode, WhileStatementNode, BlockNode

class Parser:
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

    @staticmethod
    def parse(tokens):
        parser = Parser(tokens)
        ast = parser.parse_program()
        print("Parser output:", ast)  # Debug output
        return ast

    def parse_program(self):
        statements = []
        while self.current_token is not None:
            statements.append(self.statement())
        return ProgramNode(statements)

    def statement(self):
        if self.current_token[0] == 'KEYWORD':
            if self.current_token[1] == 'If':
                return self.if_statement()
            elif self.current_token[1] == 'While':
                return self.while_statement()
        return self.expression()

    def expression(self):
        return self.function_call()

    def function_call(self):
        if self.current_token[0] not in ['IDENTIFIER', 'FUNCTION']:
            return self.factor()

        function_name = self.current_token[1]
        self.advance()  # Consume function name
        if self.current_token is None or self.current_token[1] != '(':
            return FactorNode(function_name)

        self.advance()  # Consume '('
        arguments = []
        while self.current_token is not None and self.current_token[1] != ')':
            arguments.append(self.expression())
            if self.current_token is not None and self.current_token[1] == ',':
                self.advance()  # Consume ','

        if self.current_token is None or self.current_token[1] != ')':
            raise SyntaxError("Expected ')' to close function call")
        self.advance()  # Consume ')'

        return ExpressionNode(FactorNode(function_name), "FUNCTION_CALL", arguments)

    def factor(self):
        if self.current_token is None:
            raise SyntaxError("Unexpected end of input")

        token_type, token_value = self.current_token
        if token_type == 'NUMBER':
            self.advance()
            return FactorNode(token_value)
        elif token_type == 'STRING':
            self.advance()
            return FactorNode(token_value)
        elif token_type == 'IDENTIFIER':
            self.advance()
            return FactorNode(token_value)
        else:
            raise SyntaxError(f"Unexpected token: {token_value}")

    def if_statement(self):
        self.advance()  # Skip 'If'
        if self.current_token[1] != '(':
            raise SyntaxError("Expected '(' after 'If'")
        self.advance()  # Consume '('
        condition = self.expression()
        if self.current_token[1] != ',':
            raise SyntaxError("Expected ',' after condition in If statement")
        self.advance()  # Consume ','
        if_block = self.statement()
        else_block = None
        if self.current_token[1] == ',':
            self.advance()  # Consume ','
            else_block = self.statement()
        if self.current_token[1] != ')':
            raise SyntaxError("Expected ')' at the end of If statement")
        self.advance()  # Consume ')'
        return IfStatementNode(condition, BlockNode([if_block]), BlockNode([else_block]) if else_block else None)

    def while_statement(self):
        self.advance()  # Skip 'While'
        if self.current_token[1] != '(':
            raise SyntaxError("Expected '(' after 'While'")
        self.advance()  # Consume '('
        condition = self.expression()
        if self.current_token[1] != ',':
            raise SyntaxError("Expected ',' after condition in While statement")
        self.advance()  # Consume ','
        block = self.statement()
        if self.current_token[1] != ')':
            raise SyntaxError("Expected ')' at the end of While statement")
        self.advance()  # Consume ')'
        return WhileStatementNode(condition, BlockNode([block]))