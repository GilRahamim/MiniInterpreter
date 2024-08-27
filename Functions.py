

def TypeCheck(value, expected_type):
    """Check if value is of expected_type, raise TypeError if not."""
    if not isinstance(value, expected_type):
        raise TypeError(f"Expected {expected_type.__name__}, got {type(value).__name__}")

def Add(x, y):
    """Add two numbers."""
    TypeCheck(x, (int, float))
    TypeCheck(y, (int, float))
    return x + y

def Sub(x, y):
    """Subtract y from x."""
    TypeCheck(x, (int, float))
    TypeCheck(y, (int, float))
    return x - y

def Mul(x, y):
    """Multiply two numbers."""
    TypeCheck(x, (int, float))
    TypeCheck(y, (int, float))
    return x * y

def Div(x, y):
    """Divide x by y. Raise ArithmeticError if y is zero."""
    TypeCheck(x, (int, float))
    TypeCheck(y, (int, float))
    if y == 0:
        raise ArithmeticError(f"Cannot divide {x} by zero!")
    return x / y

def Pow(x, y):
    """Raise x to the power of y."""
    TypeCheck(x, (int, float))
    TypeCheck(y, (int, float))
    return x ** y

def Sqrt(x):
    """Calculate square root of x. Raise ValueError if x is negative."""
    TypeCheck(x, (int, float))
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return x ** 0.5

def Min(x, y):
    """Return the minimum of two numbers."""
    TypeCheck(x, (int, float))
    TypeCheck(y, (int, float))
    return x if x < y else y

def Max(x, y):
    """Return the maximum of two numbers."""
    TypeCheck(x, (int, float))
    TypeCheck(y, (int, float))
    return x if x > y else y

def Assign(x, y):
    """Assign y to x."""
    return y

def Equal(x, y):
    """Check if x is equal to y."""
    return x == y

def NotEqual(x, y):
    """Check if x is not equal to y."""
    return x != y

def Greater(x, y):
    """Check if x is greater than y."""
    TypeCheck(x, (int, float, str))
    TypeCheck(y, (int, float, str))
    return x > y

def Smaller(x, y):
    """Check if x is smaller than y."""
    TypeCheck(x, (int, float, str))
    TypeCheck(y, (int, float, str))
    return x < y

def Or(x, y):
    """Perform logical OR operation."""
    TypeCheck(x, bool)
    TypeCheck(y, bool)
    return x or y

def And(x, y):
    """Perform logical AND operation."""
    TypeCheck(x, bool)
    TypeCheck(y, bool)
    return x and y

def Not(x):
    """Perform logical NOT operation."""
    TypeCheck(x, bool)
    return not x

def Array(*args):
    """Create an array (list) from the given arguments."""
    return list(args)

def Length(arr):
    """Get the length of an array, tuple, or string."""
    TypeCheck(arr, (list, tuple, str))
    return len(arr)

def Index(arr, val):
    """Find the index of a value in an array, tuple, or string."""
    TypeCheck(arr, (list, tuple, str))
    try:
        return arr.index(val)
    except ValueError:
        raise ValueError(f"Value {val} not found in {arr}")

def ArrayIndex(arr, idx):
    """Get the element at a specific index in an array or tuple."""
    TypeCheck(arr, (list, tuple))
    TypeCheck(idx, int)
    if 0 <= idx < len(arr):
        return arr[idx]
    raise IndexError(f"Index {idx} out of range for {arr}")

def AddIndex(arr, val):
    """Add a value to the end of an array."""
    TypeCheck(arr, list)
    arr.append(val)
    return arr

def RemoveIndex(arr, idx):
    """Remove and return the element at a specific index in an array."""
    TypeCheck(arr, list)
    TypeCheck(idx, int)
    if 0 <= idx < len(arr):
        return arr.pop(idx)
    raise IndexError(f"Index {idx} out of range for {arr}")

def Append(arr, val):
    """Append a value to the end of an array."""
    TypeCheck(arr, list)
    arr.append(val)
    return arr

def If(condition, action):
    """Execute an action if the condition is true."""
    TypeCheck(condition, bool)
    if condition:
        action()

def Else(action):
    """Execute an action unconditionally (used with If)."""
    action()

def Split(string, separator=' '):
    """Split a string into a list of substrings."""
    TypeCheck(string, str)
    TypeCheck(separator, str)
    return string.split(separator)

def Replace(string, old, new):
    """Replace occurrences of a substring in a string."""
    TypeCheck(string, str)
    TypeCheck(old, str)
    TypeCheck(new, str)
    return string.replace(old, new)

def IsUpper(string):
    """Check if all characters in a string are uppercase."""
    TypeCheck(string, str)
    return string.isupper()

def IsLower(string):
    """Check if all characters in a string are lowercase."""
    TypeCheck(string, str)
    return string.islower()

def Concat(*args):
    """Concatenate multiple strings or string representations of objects."""
    return ''.join(str(arg) for arg in args)

def While(condition, action):
    """Execute an action repeatedly while a condition is true."""
    while condition():
        action()

def For(iterable, action):
    """Execute an action for each item in an iterable."""
    for item in iterable:
        action(item)

def Tuple(*args):
    """Create a tuple from the given arguments."""
    return tuple(args)

def Sequence(iterable):
    """Create a sorted sequence from an iterable."""
    return sorted(iterable)

def TupleConcat(tuple1, tuple2):
    """Concatenate two tuples."""
    TypeCheck(tuple1, tuple)
    TypeCheck(tuple2, tuple)
    return tuple1 + tuple2

def GetItem(container, index):
    """Get an item from a container at a specific index."""
    TypeCheck(container, (list, tuple, str))
    TypeCheck(index, int)
    if 0 <= index < len(container):
        return container[index]
    raise IndexError(f"Index {index} out of range for {container}")

def IfElse(condition, if_action, else_action):
    """Execute one of two actions based on a condition."""
    TypeCheck(condition, bool)
    if condition:
        if_action()
    else:
        else_action()

def IsAlpha(char):
    """Check if a character is alphabetic."""
    TypeCheck(char, str)
    return char.isalpha()

def IsDigit(char):
    """Check if a character is a digit."""
    TypeCheck(char, str)
    return char.isdigit()

def IsAlnum(char):
    """Check if a character is alphanumeric."""
    TypeCheck(char, str)
    return char.isalnum()

def Print(*args, end="\n"):
    """Print the given arguments to the console."""
    print(*args, end=end)