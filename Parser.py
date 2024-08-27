

from AST import *
from Functions import *

class Token:
    """
    Represents a token in the input stream.

    Attributes:
    type (str): The type of the token.
    value: The value of the token.
    """
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

class Parser:
    """
    Parses a list of tokens into an Abstract Syntax Tree (AST).
    """
    def __init__(self, tokens):
        """
        Initialize the Parser with a list of tokens.

        Args:
        tokens (list): A list of token tuples.
        """
        TypeCheck(tokens, list)
        self.tokens = [Token(t[0], t[1]) for t in tokens]
        self.current_token = None
        self.pos = Sub(0, 1)
        self.advance()

    def advance(self):
        """
        Move to the next token in the token list.
        """
        self.pos = Add(self.pos, 1)
        if Smaller(self.pos, Length(self.tokens)):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = None

    @staticmethod
    def parse(tokens):
        """
        Parse a list of tokens into an AST.

        Args:
        tokens (list): A list of token tuples.

        Returns:
        ProgramNode: The root node of the AST.
        """
        TypeCheck(tokens, list)
        parser = Parser(tokens)
        ast = parser.parse_program()
        return ast

    def parse_program(self):
        """
        Parse the entire program.

        Returns:
        ProgramNode: The root node of the AST.
        """
        statements = []
        while self.current_token is not None:
            Append(statements, self.statement())
        return ProgramNode(statements)

    def statement(self):
        """
        Parse a single statement.

        Returns:
        Node: An AST node representing the statement.
        """
        if self.current_token and Equal(self.current_token.type, 'KEYWORD'):
            if Equal(self.current_token.value, 'If'):
                return self.if_statement()
            elif Equal(self.current_token.value, 'While'):
                return self.while_statement()
        return self.expression()

    def expression(self):
        """
        Parse an expression.

        Returns:
        Node: An AST node representing the expression.
        """
        return self.function_call()

    def function_call(self):
        """
        Parse a function call.

        Returns:
        Node: An AST node representing the function call.
        """
        if self.current_token is None or (
                NotEqual(self.current_token.type, 'IDENTIFIER') and NotEqual(self.current_token.type, 'FUNCTION')):
            return self.factor()

        function_name = self.current_token.value
        self.advance()  # Consume function name
        if self.current_token is None or NotEqual(self.current_token.value, '('):
            return FactorNode(function_name)

        self.advance()  # Consume '('
        arguments = []
        while self.current_token is not None and NotEqual(self.current_token.value, ')'):
            Append(arguments, self.expression())
            if self.current_token is not None and Equal(self.current_token.value, ','):
                self.advance()  # Consume ','

        if self.current_token is None or NotEqual(self.current_token.value, ')'):
            raise SyntaxError("Expected ')' to close function call")
        self.advance()  # Consume ')'

        return ExpressionNode(FactorNode(function_name), "FUNCTION_CALL", arguments)

    def factor(self):
        """
        Parse a factor (number, string, or identifier).

        Returns:
        FactorNode: An AST node representing the factor.

        Raises:
        SyntaxError: If an unexpected token is encountered.
        """
        if self.current_token is None:
            raise SyntaxError("Unexpected end of input")

        token_type, token_value = self.current_token.type, self.current_token.value
        if Equal(token_type, 'NUMBER'):
            self.advance()
            return FactorNode(token_value)
        elif Equal(token_type, 'STRING'):
            self.advance()
            return FactorNode(token_value)
        elif Equal(token_type, 'IDENTIFIER'):
            self.advance()
            return FactorNode(token_value)
        else:
            raise SyntaxError(Concat("Unexpected token: ", token_value))

    def if_statement(self):
        """
        Parse an if statement.

        Returns:
        IfStatementNode: An AST node representing the if statement.

        Raises:
        SyntaxError: If the if statement syntax is incorrect.
        """
        self.advance()  # Skip 'If'
        if NotEqual(self.current_token.value, '('):
            raise SyntaxError("Expected '(' after 'If'")
        self.advance()  # Consume '('
        condition = self.expression()
        if NotEqual(self.current_token.value, ','):
            raise SyntaxError("Expected ',' after condition in If statement")
        self.advance()  # Consume ','
        if_block = self.statement()
        else_block = None
        if Equal(self.current_token.value, ','):
            self.advance()  # Consume ','
            else_block = self.statement()
        if NotEqual(self.current_token.value, ')'):
            raise SyntaxError("Expected ')' at the end of If statement")
        self.advance()  # Consume ')'
        return IfStatementNode(condition, BlockNode([if_block]), BlockNode([else_block]) if else_block else None)

    def while_statement(self):
        """
        Parse a while statement.

        Returns:
        WhileStatementNode: An AST node representing the while statement.

        Raises:
        SyntaxError: If the while statement syntax is incorrect.
        """
        self.advance()  # Skip 'While'
        if NotEqual(self.current_token.value, '('):
            raise SyntaxError("Expected '(' after 'While'")
        self.advance()  # Consume '('
        condition = self.expression()
        if NotEqual(self.current_token.value, ','):
            raise SyntaxError("Expected ',' after condition in While statement")
        self.advance()  # Consume ','
        block = self.statement()
        if NotEqual(self.current_token.value, ')'):
            raise SyntaxError("Expected ')' at the end of While statement")
        self.advance()  # Consume ')'
        return WhileStatementNode(condition, BlockNode([block]))