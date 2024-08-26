# Lexer.py

def tokenize(string):
    tokens = []
    i = 0

    while i < len(string):
        char = string[i]

        if char.isspace():
            i += 1
            continue

        if char.isalpha() or char == '_':
            identifier = char
            i += 1
            while i < len(string) and (string[i].isalnum() or string[i] == '_'):
                identifier += string[i]
                i += 1
            if identifier in ['If', 'While']:
                tokens.append(('KEYWORD', identifier))
            elif identifier in ['Add', 'Sub', 'Mul', 'Div', 'Assign', 'Greater', 'Smaller', 'Concat']:
                tokens.append(('FUNCTION', identifier))
            else:
                tokens.append(('IDENTIFIER', identifier))
            continue

        if char.isdigit():
            number = char
            i += 1
            while i < len(string) and string[i].isdigit():
                number += string[i]
                i += 1
            tokens.append(('NUMBER', int(number)))
            continue

        if char == '$':
            string_literal = ''
            i += 1
            while i < len(string) and string[i] != '$':
                string_literal += string[i]
                i += 1
            if i < len(string) and string[i] == '$':
                tokens.append(('STRING', string_literal))
                i += 1
            else:
                raise ValueError("Unterminated string literal")
            continue

        if char in '(),':
            tokens.append(('PUNCTUATION', char))
            i += 1
            continue

        raise ValueError(f"Unexpected character: {char}")

    print("Lexer output:", tokens)  # Debug output
    return tokens