

from Functions import *

def tokenize(string):
    """
    Tokenize the input string into a list of tokens.

    Args:
    string (str): The input string to be tokenized.

    Returns:
    list: A list of tuples, where each tuple contains a token type and its value.

    Raises:
    ValueError: If an unexpected character is encountered.
    """
    TypeCheck(string, str)
    tokens = []
    i = 0

    while Smaller(i, Length(string)):
        char = GetItem(string, i)

        if char.isspace():
            i = Add(i, 1)
            continue

        if Or(IsAlpha(char), Equal(char, '_')):
            # Handle identifiers, keywords, and function names
            identifier = char
            i = Add(i, 1)
            while Smaller(i, Length(string)):
                next_char = GetItem(string, i)
                if Or(IsAlnum(next_char), Equal(next_char, '_')):
                    identifier = Concat(identifier, next_char)
                    i = Add(i, 1)
                else:
                    break
            if Or(Equal(identifier, 'If'), Equal(identifier, 'While')):
                Append(tokens, ('KEYWORD', identifier))
            elif Or(Or(Or(Or(Or(Or(Or(Equal(identifier, 'Add'), Equal(identifier, 'Sub')), Equal(identifier, 'Mul')), Equal(identifier, 'Div')), Equal(identifier, 'Assign')), Equal(identifier, 'Greater')), Equal(identifier, 'Smaller')), Equal(identifier, 'Concat')):
                Append(tokens, ('FUNCTION', identifier))
            else:
                Append(tokens, ('IDENTIFIER', identifier))
            continue

        if IsDigit(char):
            # Handle numeric literals
            number = char
            i = Add(i, 1)
            while Smaller(i, Length(string)):
                if IsDigit(GetItem(string, i)):
                    number = Concat(number, GetItem(string, i))
                    i = Add(i, 1)
                else:
                    break
            Append(tokens, ('NUMBER', int(number)))
            continue

        if Equal(char, '$'):
            # Handle string literals
            string_literal = ''
            i = Add(i, 1)
            while Smaller(i, Length(string)):
                if NotEqual(GetItem(string, i), '$'):
                    string_literal = Concat(string_literal, GetItem(string, i))
                    i = Add(i, 1)
                else:
                    break
            if And(Smaller(i, Length(string)), Equal(GetItem(string, i), '$')):
                Append(tokens, ('STRING', string_literal))
                i = Add(i, 1)
            else:
                raise ValueError("Unterminated string literal")
            continue

        if Or(Or(Equal(char, '('), Equal(char, ')')), Equal(char, ',')):
            # Handle punctuation
            Append(tokens, ('PUNCTUATION', char))
            i = Add(i, 1)
            continue

        raise ValueError(Concat("Unexpected character: ", char))

    Print(Concat("Lexer output: ", str(tokens)))  # Debug output
    return tokens