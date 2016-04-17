import sys

def isNumber(s):
    state = [{},
             {'b': 1, 's': 2, 'd': 3, '.': 4},
             {'d': 3, '.': 4},
             {'d': 3, '.': 4, 'e': 6, 'b': 9},
             {'d': 5},
             {'d': 5, 'e': 6, 'b': 9},
             {'s': 7, 'd': 8},
             {'d': 8},
             {'d': 8, 'b': 9},
             {'b': 9}]
    currentState = 1;
    for c in s:
        if c in ['d', 's', 'b']:
            return False
        elif '0' <= c and c <= '9':
            c = 'd'
        elif c == ' ':
            c = 'b'
        elif c in ['+', '-']:
            c = 's'
        elif c not in state[currentState].keys():
            return False
        currentState = state[currentState][c]
    if currentState not in [3, 5, 8, 9]:
        return False
    return True

if __name__ == '__main__':
    while True:
        try:
            print(isNumber(input('--> ')))
        except (EOFError, KeyboardInterrupt):
            sys.exit(0)

