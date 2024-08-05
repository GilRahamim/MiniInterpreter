from _ast import keyword
def isWhiteSpace(char):
    return char in ' \t\n\r'

def isDigit(char):
    return '0' <= char <= '9'

def isLetter(char):
    return ('a' <= char <= 'z') or ('A' <= char <= 'Z') or (char == '_') or (char == ')') or (char == '(')

def isOperator(char):
    return char in '+/*-=!^><|&'

def keyWord(id):
    keyword = {'if' , 'else' ,'for' ,'while'}
    return id in keyword

def isFunction(identifier):
    functions = {
        'Min', 'Max',
        'Array', 'Length', 'Index', 'Add(i)', 'Remove(i)', 'Append',
        'Tuple', 'GetItem',
        'Split', 'Replace', 'isUpper', 'isLower', 'Concat'
    }
    return identifier in functions

def tokenize(string):
    tokens = []
    current_token = ''
    i = 0

    while i < len(string):
        char = string[i]
        if isWhiteSpace(char):
            i += 1
            continue

        if isDigit(char):
            current_token = char
            i += 1
            while i < len(string) and isDigit(string[i]):
                current_token += string[i]
                i += 1
                tokens.append('NUMBER' , current_token)
                continue

        if i < len(string) - 1 and string[i:i+2] in {'>=', '<=', '==', '!=', '||', '&&'}:
            tokens.append(('OPERATOR',string[i:i+2]))
            i += 2
            continue

        if isOperator(char):
            tokens.append(('OPERATOR', char))
            i += 1
            continue

        if isLetter(char):
            current_token = char
            i += 1
            while i < len(string) and isLetter(string[i]):
                current_token += string[i]
                i += 1
                if keyword(current_token):
                    tokens.append('KEYWORD' , current_token)
                elif isFunction(current_token):
                    tokens.append('FUNCTION' , current_token)
                else:
                    tokens.append('IDENTIFIER', current_token)
                continue

            raise ValueError(f"Unexpected character: {char}")
        return tokens





