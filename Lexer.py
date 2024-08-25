def isWhiteSpace(char):
    return char in ' \t\n\r'


def isLetter(char):
    return ('a' <= char <= 'z') or ('A' <= char <= 'Z') or (char == '_') or '0' <= char <= '9'


def isPunctuation(char):
    return char in '(){}[],;'


def isLiteral(char):
    if char[0] == '$':  #using '$' for string definition
        return True
    if char == 'true' or char == 'false':  #boolean literal
        return True
    try:  #check for int literal
        float(char)
        return True
    except ValueError:
        return False


def isOperator(char):
    return char in '+/*-=!^><|&'


def keyWord(char):
    keyword = {'if', 'else', 'for', 'while'}
    return char in keyword


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

        if isLetter(char):
            current_token = char
            i += 1
            while i < len(string) and isLetter(string[i]):
                current_token += string[i]
                i += 1
            if keyWord(current_token):
                tokens.append(('KEYWORD', current_token))
            elif isFunction(current_token):
                tokens.append(('FUNCTION', current_token))
            elif isLiteral(current_token):
                tokens.append(('LITERAL', current_token))
            else:
                tokens.append(('IDENTIFIER', current_token))
            continue

        if i < len(string) - 1 and string[i:i + 2] in {'>=', '<=', '==', '!=', '||', '&&'}:  #two digits operators
            tokens.append(('OPERATOR', string[i:i + 2]))
            i += 2
            continue

        if isOperator(char):  #one digit operators
            tokens.append(('OPERATOR', char))
            i += 1
            continue

        if isPunctuation(char):
            i += 1
            tokens.append(('PUNC',char))
            continue

        raise ValueError(f"Unexpected character: {char}")
    return tokens
