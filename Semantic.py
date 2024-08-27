
from AST import *
from Functions import *

class Variable:
    """
    Represents a variable in the symbol table.

    Attributes:
    name (str): The name of the variable.
    type: The type of the variable.
    value: The value of the variable.
    """
    def __init__(self, name, var_type, value=None):
        self.name = name
        self.type = var_type
        self.value = value

class SemanticAnalyzer:
    """
    Performs semantic analysis on the Abstract Syntax Tree (AST).
    """

    def __init__(self):
        """
        Initialize the SemanticAnalyzer with an empty symbol table and function call set.
        """
        self.symbol_table = []
        self.functions_called = set()

    def declare(self, name, var_type, value=None):
        """
        Declare a new variable in the symbol table.

        Args:
        name (str): The name of the variable.
        var_type: The type of the variable.
        value: The initial value of the variable (optional).

        Raises:
        ValueError: If the variable is already declared.
        """
        TypeCheck(name, str)
        for var in self.symbol_table:
            if Equal(var.name, name):
                raise ValueError(Concat("Variable '", name, "' is already declared."))
        self.symbol_table.append(Variable(name, var_type, value))

    def lookup(self, name):
        """
        Look up a variable in the symbol table.

        Args:
        name (str): The name of the variable to look up.

        Returns:
        The value of the variable.

        Raises:
        ValueError: If the variable is not declared.
        """
        TypeCheck(name, str)
        for var in self.symbol_table:
            if Equal(var.name, name):
                return var.value
        raise ValueError(Concat("Variable '", name, "' is not declared."))

    def update(self, name, value):
        """
        Update the value of a variable in the symbol table.

        Args:
        name (str): The name of the variable to update.
        value: The new value of the variable.

        Raises:
        ValueError: If the variable is not declared.
        """
        TypeCheck(name, str)
        for var in self.symbol_table:
            if Equal(var.name, name):
                var.value = value
                var.type = type(value).__name__
                return
        raise ValueError(Concat("Variable '", name, "' is not declared."))

    def evaluate_function(self, function_name, args):
        """
        Evaluate a function call.

        Args:
        function_name (str): The name of the function to evaluate.
        args (list): The arguments to pass to the function.

        Returns:
        The result of the function call.

        Raises:
        ValueError: If the function is unknown.
        """
        TypeCheck(function_name, str)
        TypeCheck(args, list)
        self.functions_called.add(function_name)
        if Equal(function_name, 'Add'):
            return Add(args[0], args[1])
        elif Equal(function_name, 'Sub'):
            return Sub(args[0], args[1])
        elif Equal(function_name, 'Mul'):
            return Mul(args[0], args[1])
        elif Equal(function_name, 'Div'):
            return Div(args[0], args[1])
        elif Equal(function_name, 'Greater'):
            return Greater(args[0], args[1])
        elif Equal(function_name, 'Smaller'):
            return Smaller(args[0], args[1])
        elif Equal(function_name, 'Concat'):
            return Concat(*args)
        else:
            raise ValueError(Concat("Unknown function: ", function_name))

    def analyze(self, ast):
        """
        Analyze the Abstract Syntax Tree (AST) and perform semantic checks.

        Args:
        ast: The root node of the AST.

        Returns:
        The result of the analysis, if applicable.

        Raises:
        ValueError: If a semantic error is encountered.
        """
        if isinstance(ast, ProgramNode):
            for statement in ast.statements:
                self.analyze(statement)
        elif isinstance(ast, ExpressionNode):
            if Equal(ast.operator, "FUNCTION_CALL"):
                function_name = ast.left.value
                if Equal(function_name, "Assign"):
                    var_name = ast.right[0].value
                    value = self.analyze(ast.right[1])
                    try:
                        self.lookup(var_name)
                        self.update(var_name, value)
                    except ValueError:
                        self.declare(var_name, type(value).__name__, value)
                else:
                    args = [self.analyze(arg) for arg in ast.right]
                    return self.evaluate_function(function_name, args)
            else:
                left = self.analyze(ast.left)
                right = self.analyze(ast.right)
                return self.evaluate_function(ast.operator, [left, right])
        elif isinstance(ast, FactorNode):
            if isinstance(ast.value, str):
                try:
                    return self.lookup(ast.value)
                except ValueError:
                    if ast.value.startswith('$') and ast.value.endswith('$'):
                        return ast.value[1:-1]  # Remove the $ signs for string literals
                    else:
                        return ast.value  # Return identifiers as is
            return ast.value
        elif isinstance(ast, IfStatementNode):
            condition = self.analyze(ast.condition)
            if condition:
                self.analyze(ast.if_block)
            elif ast.else_block:
                self.analyze(ast.else_block)
        elif isinstance(ast, WhileStatementNode):
            while self.analyze(ast.condition):
                self.analyze(ast.block)
        elif isinstance(ast, BlockNode):
            for statement in ast.statements:
                self.analyze(statement)

        return None

    def get_summary(self):
        """
        Get a summary of the semantic analysis.

        Returns:
        str: A string containing the list of functions called and variables in the symbol table.
        """
        functions = ', '.join(sorted(self.functions_called))
        variables = ', '.join(Concat(var.name, ": ", str(var.value)) for var in self.symbol_table)
        return Concat("Functions called: ", functions, "\nVariables: ", variables)