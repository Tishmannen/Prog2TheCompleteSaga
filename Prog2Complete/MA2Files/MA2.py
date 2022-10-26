"""
Solutions to module 2 - A calculator
Student: Thor Lindberg
Mail: thor.ronnegard@gmail.com
Reviewed by: Adam Pehrson/Oliver Groth
Reviewed date: 19/09-2022
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from queue import Empty
from statistics import mean
from tokenize import TokenError
from types import NoneType  
from MA2tokenizer import TokenizeWrapper


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class EvaluationError(Exception):
    def __init__(self,function,message):
        self.function = function
        self.message = message
        super(EvaluationError, self).__init__(function,message)


def statement(wtok, variables):
    """ See syntax chart for statement"""
    result = assignment(wtok, variables)

    if wtok.is_at_end():
        return result
    else:
        raise SyntaxError("Expected end of expression")


def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)

    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            variables[wtok.get_current()] = result
        else:
            raise SyntaxError("Expected variable after '=")
        wtok.next()

    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)

    while wtok.get_current() == '+' or wtok.get_current() == '-':
        wtok.next()
        if wtok.get_previous() == '+':
            result = result + term(wtok, variables)
        else:
            result = result - term(wtok,variables)

    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)

    while wtok.get_current() == '*' or wtok.get_current() == '/': 
        wtok.next()
        if wtok.get_previous() == '*':
            result = result * factor(wtok, variables)
        else:
            fact = factor(wtok,variables)
            if fact == 0:
                raise EvaluationError("term","Division by 0")
            result = result / fact
            
    return result

def factor(wtok, variables):
    """ See syntax chart for factor"""
    function_1 = {'sin': math.sin,'cos': math.cos,'exp': math.exp,'log': log,'fib': fib,'fac': factorial}
    function_n = {'min': min,'max': max,'sum': sum,'mean': mean}
    if wtok.get_current() in variables:
        result = variables[wtok.get_current()]
        wtok.next()

    elif wtok.get_current() in function_1:
        func = wtok.get_current()
        wtok.next()
        if wtok.get_current() != '(':
            raise SyntaxError("Expected '('")

        result = function_1[func](factor(wtok,variables))

    elif wtok.get_current() in function_n:
        wtok.next()
        result = function_n[wtok.get_previous()](arglist(wtok, variables))

    elif wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()
            
    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()

    elif wtok.get_current() == '-':
        wtok.next()
        result = -1*factor(wtok, variables)

    elif wtok.is_name():
        raise EvaluationError("factor","Unknown variable")

    else:
        raise SyntaxError(
            "Expected number or '('")  
    return result

def log(n):
    if n > 0:
        return math.log(n)
    else:
        raise EvaluationError("log","Expected number > 0")

def factorial(x):
    if (x).is_integer() and x >= 0:
        return math.factorial(int(x))
    else:
        raise EvaluationError("fac","Expected whole number >= 0")

def fib(n):
    if (n).is_integer() and n >= 0:
        return _fib(n,computed = {0: 0, 1: 1})
    else:
        raise EvaluationError("fib", "Expected whole number >= 0")

def _fib(n,computed = {0: 0, 1: 1}):
    if (n).is_integer() and n >= 0:
        if n not in computed:
            computed[n] = _fib(n-1, computed) + _fib(n-2, computed)
    return computed[n]

def arglist(wtok, variables):
    if wtok.get_current() != '(':
        raise SyntaxError("Expected '('")

    result = []
    while wtok.get_current() != ')':
        wtok.next()
        result = result + [assignment(wtok,variables)]
        if wtok.get_current() != ',':
            if wtok.get_current() == ')':
                pass
            else:
                raise SyntaxError("Expected ','")
    wtok.next()
    return result

         
def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """
    
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    # Note: The unit test file initiate variables in this way. If your implementation 
    # requires another initiation you have to update the test file accordingly.
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        else:
            try:
                if wtok.get_current() == 'vars':
                    for key,value in variables.items():
                        print(key+' : ',value)
                else:
                    result = statement(wtok, variables)
                    variables['ans'] = result
                    print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')
 


if __name__ == "__main__":
    main()
