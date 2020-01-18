"""
A Basic Calculator Program.
Supports 6 different operators for a single calculation.
"""

from math import pow

CurrentValue = 0.0

InitialText = "Please enter the starting number: "
NumberText = "Please enter a number: "
OperatorText = "Please enter an operator: "

ValidOperators = ['+', '-', '*', '/', '^', '%']
InvalidOperatorText = """
Invalid Operator. Valid Operators are:\n
+ _ Addition\n
- _ Subtraction\n
* _ Multiplication\n
/ _ Division\n
^ _ Exponent\n
% _ Modulo\n
"""


def numerical_input(Text):
    
    while True:
        try:
            UserInput = input(Text)
            return float(UserInput)
        except ValueError:
            print("%s is not a number." % UserInput)
            

def operator_input(Text):
    
    while True:
        Operator = input(Text)
        
        if Operator in ValidOperators:
            return Operator
        
        else:
            print(InvalidOperatorText)
            

def addition(FirstValue, SecondValue):
    return FirstValue + SecondValue

def subtraction(FirstValue, SecondValue):
    return FirstValue - SecondValue

def multiplication(FirstValue, SecondValue):
    return FirstValue * SecondValue

def division(FirstValue, SecondValue):
    return FirstValue / SecondValue

def exponent(FirstValue, SecondValue):
    return pow(FirstValue, SecondValue)
    
def modulo(FirstValue, SecondValue):
    return FirstValue % SecondValue

Operators = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division,
    '^': exponent,
    '%': modulo
    }
    
def calculation(Operator, Value):
    return Operators.get(Operator)(CurrentValue, SecondValue)

if __name__ == "__main__":        
    CurrentValue = numerical_input(InitialText)
    print (CurrentValue)
    
    Operator = operator_input(OperatorText)
    SecondValue = numerical_input(NumberText)
    
    Result = calculation(Operator, SecondValue)
    print(Result)
    
    print("%f %s %f = %f" % [CurrentValue, Operator, 
                              SecondValue, Result])
    