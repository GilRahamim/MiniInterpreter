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




