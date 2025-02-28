from ccjp import parser
import sys

def main(input: str):
    parser.lex(input)

if __name__ == "__main__": 

    input = sys.argv[1]
    
    main(input)
