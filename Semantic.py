# Semantic.py

from AST import ProgramNode, ExpressionNode, FactorNode, IfStatementNode, WhileStatementNode, BlockNode

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}
        self.functions_called = set()

    def declare(self, name, var_type, value=None):
        if name in self.symbol_table:
            raise ValueError(f"Variable '{name}' is already declared.")
        self.symbol_table[name] = {'type': var_type, 'value': value}

    def lookup(self, name):
        if name not in self.symbol_table:
            raise ValueError(f"Variable '{name}' is not declared.")
        return self.symbol_table[name]['value']

    def update(self, name, value):
        if name not in self.symbol_table:
            raise ValueError(f"Variable '{name}' is not declared.")
        self.symbol_table[name]['value'] = value
        self.symbol_table[name]['type'] = type(value).__name__

    def evaluate_function(self, function_name, args):
        self.functions_called.add(function_name)
        if function_name == 'Add':
            return args[0] + args[1]
        elif function_name == 'Sub':
            return args[0] - args[1]
        elif function_name == 'Mul':
            return args[0] * args[1]
        elif function_name == 'Div':
            if args[1] == 0:
                raise ValueError("Division by zero")
            return args[0] / args[1]
        elif function_name == 'Greater':
            return args[0] > args[1]
        elif function_name == 'Smaller':
            return args[0] < args[1]
        elif function_name == 'Concat':
            return ''.join(str(arg) for arg in args)
        else:
            raise ValueError(f"Unknown function: {function_name}")

    def analyze(self, ast):
        if isinstance(ast, ProgramNode):
            for statement in ast.statements:
                self.analyze(statement)
        elif isinstance(ast, ExpressionNode):
            if ast.operator == "FUNCTION_CALL":
                function_name = ast.left.value
                if function_name == "Assign":
                    var_name = ast.right[0].value
                    value = self.analyze(ast.right[1])
                    if var_name not in self.symbol_table:
                        self.declare(var_name, type(value).__name__, value)
                    else:
                        self.update(var_name, value)
                else:
                    args = [self.analyze(arg) for arg in ast.right]
                    return self.evaluate_function(function_name, args)
            else:
                left = self.analyze(ast.left)
                right = self.analyze(ast.right)
                return self.evaluate_function(ast.operator, [left, right])
        elif isinstance(ast, FactorNode):
            if isinstance(ast.value, str):
                if ast.value in self.symbol_table:
                    return self.lookup(ast.value)
                elif ast.value.startswith('$') and ast.value.endswith('$'):
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
        functions = ', '.join(sorted(self.functions_called))
        variables = ', '.join(f"{name}: {value['value']}" for name, value in self.symbol_table.items())
        return f"Functions called: {functions}\nVariables: {variables}"