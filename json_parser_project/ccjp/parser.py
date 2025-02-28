"""Module for lexing and parsing a JSON-encoded string."""
from typing import List, Optional, Tuple, Union

JSON_WHITESPACE = " "
JSON_QUOTE = '"'
JSON_SYNTAX = "{}[]:,"

def lex_string(input: str) -> Tuple[Optional[str], str]:

    json_string = ""

    if input[0] != JSON_QUOTE:
        return None, input

    input = input[1:] 
    for char in input:
        if char == JSON_QUOTE:
            break
            
        json_string += char

    return json_string, input[len(json_string)+1:]


def lex_number(input: str) -> Tuple[Optional[Union[int, float]], str]:

    json_number = ""
    
    valid_number_chars = [str(n) for n in range(0, 10)] + ['.', '-']

    for char in input:
        if char in valid_number_chars:
            json_number += char
            continue

        break

    if len(json_number):
        input = input[len(json_number):]
        if '.' in json_number:
            return float(json_number), input
        else:
            return int(json_number), input

    return None, input


def lex(input: str) -> List:

    tokens = []

    # input will be changing dynamically
    while len(input):
        print(f"Current input: {input}")
        print(f"Current tokens: {tokens}")
        json_string, input = lex_string(input)
        if json_string is not None:
            tokens.append(json_string)
            continue

        json_number, input = lex_number(input)
        if json_number is not None:
            tokens.append(json_number)
            continue


        if input[0] in JSON_WHITESPACE:
            input = input[1:]
        elif input[0] in JSON_SYNTAX:
            tokens.append(input[0])
            input = input[1:]
        else:
            raise Exception("Invalid Char {}".format(input[0]))

    print(tokens)
        
    return tokens

# print([f for f in '{"foo": 1}'])
