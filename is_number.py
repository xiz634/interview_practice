import sys
import unittest

# automata implementation

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
    current_state = 1;
    for c in s:
        if c in ['d', 's', 'b']:
            return False
        elif '0' <= c and c <= '9':
            c = 'd'
        elif c == ' ':
            c = 'b'
        elif c in ['+', '-']:
            c = 's'
        if c not in state[current_state].keys():
            return False
        current_state = state[current_state][c]
    if current_state not in [3, 5, 8, 9]:
        return False
    return True

class TestStringMethods(unittest.TestCase):

    def test_valid_number(self):
        self.assertTrue(isNumber('1234'))
        self.assertTrue(isNumber('.235'))
        self.assertTrue(isNumber('1e15'))
        self.assertTrue(isNumber('+5'))
        self.assertTrue(isNumber('    123   '))
        self.assertTrue(isNumber('1.5e-5'))
        self.assertTrue(isNumber('+.52e12'))

    def test_invalid_number(self):
        self.assertFalse(isNumber('..123'))
        self.assertFalse(isNumber('ddd'))
        self.assertFalse(isNumber('1 23'))
        self.assertFalse(isNumber('5.e5'))
        self.assertFalse(isNumber('52d'))
        self.assertFalse(isNumber('+-5'))
        self.assertFalse(isNumber('1.5e+-5'))
        self.assertFalse(isNumber('..5'))

if __name__ == '__main__':
#    while True:
#        try:
#            print(isNumber(input('--> ')))
#        except (EOFError, KeyboardInterrupt):
#            sys.exit(0)
    unittest.main()

