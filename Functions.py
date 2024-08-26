def Add(x, y):
    return x + y

def Sub(x, y):
    return x - y

def Mul(x, y):
    return x * y

def Div(x, y):
    if y == 0:
        ArithmeticError(f"Cannot divide {x} by zero!")
    return x / y

def Pow(x, y):
    return x ** y

def Sqrt(x):
    return x ** 0.5

def Min(x, y):
    return x if x < y else y

def Max(x, y):
    return x if x > y else y

def Assign(x, y):
    x = y
    return x

def Eqaual(x, y):
    return x == y

def NotEqual(x, y):
    return x != y

def Greater(x, y):
    return x > y

def Smaller(x, y):
    return x < y

def Or(x, y):
    return x or y

def And(x, y):
    return x and y

def Array(*args):
    return list(args)

def Length(arr):
    if isinstance(arr, list):
        return len(arr)
    raise TypeError(f"that is {arr} is not a list!")

def Index(arr, val):
    if isinstance(arr, list):
        return arr.index(val)
    raise TypeError(f"that is {arr} is not a list!")

def ArrayIndex(arr, val):
    if isinstance(arr, list):
        if 0 <= val < len(arr):
            return arr[val]
        else:
            raise TypeError(f"index of {arr} is not valid!")
    raise TypeError(f"that is {arr} is not a list!")

def AddIndex(arr, val):
    if not isinstance(arr, list):
        raise TypeError(f"{arr} is not a list!")
    arr.append(val)
    return arr

def RemoveIndex(arr, val):
    if not isinstance(arr, list):
        raise TypeError(f"{arr} is not a list!")
    try:
        arr.remove(val)
        return arr
    except ValueError:
        return TypeError(f"value {val} is not found in the list!")

def append(arr, val):
    if not isinstance(arr, list):
        raise TypeError(f"{arr} is not a list!")
    arr += [val]
    return arr

def If(condition, action):
    if condition:
        action()

def Else(action):
    action()

def Concat(a, b):
    if isinstance(a, str) and isinstance(b, str):
        return a + b
    elif isinstance(a, list) and isinstance(b, list):
        return a + b
    else:
        raise TypeError('Concat function only supports concatenation of two strings or two lists.')

    def Tuple(*args):
        return tuple(args)

    def SequenceSort(sequence):
        return sorted(sequence)

    def ConcatTuples(tuple1, tuple2):
        if isinstance(tuple1, tuple) and isinstance(tuple2, tuple):
            return tuple1 + tuple2
        else:
            raise TypeError('ConcatTuples function only supports tuple concatenation.')

    def GetItem(sequence, index):
        return sequence[index]

    def Index(sequence, item):
        return sequence.index(item)

    def Length(sequence):
        return len(sequence)

    def Split(string, delimiter=None):
        return string.split(delimiter)

    def Replace(string, old, new):
        return string.replace(old, new)

    def isUpper(string):
        return string.isupper()

    def isLower(string):
        return string.islower()

