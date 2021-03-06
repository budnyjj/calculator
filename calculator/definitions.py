import math
from collections import namedtuple

# abstract data structure
Identifier = namedtuple('Identifier', ['type', 'val'])

Operator = namedtuple('Operator', ['leftAssoc', 'priority', 'argCount', 'alg'])
Function = namedtuple('Function', ['argCount', 'alg'])
Number = namedtuple('Number', ['regex'])
Constant = namedtuple('Constant', ['value'])

_number = Number(regex='\d*[\.]?\d+')
_operators = {
    '!'  : Operator(leftAssoc = False, priority = 4, argCount = 1, alg = lambda args: not args[0]),
    '^'  : Operator(leftAssoc = True, priority = 4, argCount = 2, alg = lambda args: args[0] ** args[1]),
    '*'  : Operator(leftAssoc = True, priority = 3, argCount = 2, alg = lambda args: args[0] * args[1]),
    '/'  : Operator(leftAssoc = True, priority = 3, argCount = 2, alg = lambda args: args[0] / args[1]),
    '//' : Operator(leftAssoc = True, priority = 3, argCount = 2, alg = lambda args: int(args[0]) // int(args[1])),
    '%'  : Operator(leftAssoc = True, priority = 3, argCount = 2, alg = lambda args: int(args[0]) % int(args[1])),
    '+'  : Operator(leftAssoc = True, priority = 2, argCount = 2, alg = lambda args: args[0] + args[1]),
    '-'  : Operator(leftAssoc = True, priority = 2, argCount = 2, alg = lambda args: args[0] - args[1]),
    '='  : Operator(leftAssoc = True, priority = 1, argCount = 2, alg = lambda args: args[0] == args[1]),
}
_functions = {
    'abs'   : Function(argCount = 1, alg = lambda args: math.fabs(args[0])),
    'acosh' : Function(argCount = 1, alg = lambda args: math.acosh(args[0])),
    'acos'  : Function(argCount = 1, alg = lambda args: math.acos(args[0])),
    'asinh' : Function(argCount = 1, alg = lambda args: math.asinh(args[0])),
    'asin'  : Function(argCount = 1, alg = lambda args: math.asin(args[0])),
    'atan2' : Function(argCount = 1, alg = lambda args: math.atan2(args[0])),
    'atanh' : Function(argCount = 1, alg = lambda args: math.atanh(args[0])),
    'atan'  : Function(argCount = 1, alg = lambda args: math.atan(args[0])),
    'cos'   : Function(argCount = 1, alg = lambda args: math.cos(args[0])),
    'exp'   : Function(argCount = 1, alg = lambda args: math.exp(args[0])),
    'log10' : Function(argCount = 1, alg = lambda args: math.log10(args[0])),
    'log'   : Function(argCount = 1, alg = lambda args: math.log(args[0])),
    'sin'   : Function(argCount = 1, alg = lambda args: math.sin(args[0])),
    'sqrt'  : Function(argCount = 1, alg = lambda args: math.sqrt(args[0])),
    'tanh'  : Function(argCount = 1, alg = lambda args: math.tanh(args[0])),
    'tan'   : Function(argCount = 1, alg = lambda args: math.tan(args[0])),
}
_constants = {
    'e'     : Constant(value = 2.71828182846),
    'pi'    : Constant(value = 3.14159265359),
}

