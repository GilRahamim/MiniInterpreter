def __init__(self):
    self.table = {}

def declare(self, name, var_type, value=None):
    if name in self.table:
        raise ValueError(f"Variable '{name}' is already declared.")
    self.table[name] = {'type': var_type, 'value': value}

def lookup(self, name):
    if name not in self.table:
        raise ValueError(f"Variable '{name}' is not declared.")
    return self.table[name]

def update(self, name, value):
    if name not in self.table:
        raise ValueError(f"Variable '{name}' is not declared.")
    self.table[name]['value'] = value


