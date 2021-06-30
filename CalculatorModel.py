"""Model classes for Calculator.py"""

__author__= "Mitchell Clark"

from Constants import *
import math

class CalculationProcessor:
    """Handles calculating expressions given by the UI."""
    def process_input(self, expression: str) -> str:
        """Process the operations in the given string."""
        expression = self._evaluate_brackets(expression)
        expression = self._evaluate_operations(expression)
        
        basic_operator_split = self._split_operators(expression)
        self._evaluate_basic_operators(basic_operator_split, (MULTIPLY, DIVIDE))
        self._evaluate_basic_operators(basic_operator_split, (PLUS, MINUS))
        expression = BLANK.join(basic_operator_split)
        return expression

    def _evaluate_brackets(self, expression: str) -> str:
        """Find all brackets and evaluate expression within appropriately."""
        while LEFT_BRACKET in expression:
            for index in range(len(expression)):
                character = expression[index]
                if character is LEFT_BRACKET:
                    left_bracket_position = index
                elif character is RIGHT_BRACKET:
                    right_bracket_position = index
                    break

            bracketed_expression = expression[left_bracket_position + 1:right_bracket_position]
            evaluated_bracketed_expression = self.process_input(bracketed_expression)
            old_part_of_expression = expression[left_bracket_position:right_bracket_position + 1]
            expression = expression.replace(old_part_of_expression, evaluated_bracketed_expression)
        
        return expression

    def _evaluate_operations(self, expression: str) -> str:
        """Find operations such as sin, x^2 and log. Evaluate all operations and return partially evaluated expresson."""
        return expression

    def _split_operators(self, expression: str) -> list:
        """Split an expression into a list containing elements seperated by operators. E.g. _split_basic_operators("302.2+3×6")
        returns ['302.2', '+', '3', '×', '6']"""
        operation_splits = []
        element = BLANK
        for index in range(len(expression)):
            character = expression[index]
            if index == 0 or character in NUMBER_PARTS:
                element += character
                
                last_index = len(expression) - 1
                if index == last_index:
                    operation_splits.append(element)
                    
            else:
                operation_splits.append(element)
                operation_splits.append(character)
                element = BLANK
                
        return operation_splits

    def _split_brackets(self, expression: str) -> list:
        """Split expression into a list seperated by brackets that are not attached to a function.
        E.g. _split_brackets("(32+4)×(3+sin(30))") returns ['(', '32+4', ')', '×', '(', '3+sin(30)', ')']"""
        bracket_splits = []
        function_right_bracket = False
        element = BLANK
        for index in range(len(expression)):
            character = expression[index]
            if character not in BRACKETS:
                element += character
            elif character is LEFT_BRACKET:
                if element is BLANK:
                    bracket_splits.append(character)
                elif element[-1].isalpha() and element[-1].islower():
                    element += character
                    function_right_bracket = True
                else:
                    bracket_splits.append(element)
                    bracket_splits.append(character)
                    element = BLANK
            elif character is RIGHT_BRACKET:
                if function_right_bracket == False:
                    bracket_splits.append(element)
                    bracket_splits.append(character)
                    element = BLANK
                else:
                    element += character
                    function_right_bracket = False

        return bracket_splits
                    
    def _evaluate_basic_operators(self, expression: list, operator_pair: tuple) -> list:
        """Find all operators given in operator pair and evaluate them. The operator pair can contain multiplication and division, or addition and subtraction.
        Return partially evaluated expression."""
        basic_operations = {MULTIPLY:lambda x, y: x * y, DIVIDE:lambda x, y: x / y, \
                            PLUS:lambda x, y: x + y, MINUS:lambda x, y: x - y}
        operation1, operation2 = operator_pair 
        
        while operation1 in expression or operation2 in expression:
            try: operation1_position = expression.index(operation1)
            except: operation1_position = len(expression)
            try: operation2_position = expression.index(operation2)
            except: operation2_position = len(expression)
                
            leftmost_operation_position = min(operation1_position, operation2_position)
            operation_undertaken = expression[leftmost_operation_position]
            left_number = float(expression[leftmost_operation_position - 1])
            right_number = float(expression[leftmost_operation_position + 1])

            evaluated_number = basic_operations[operation_undertaken](left_number, right_number)

            for count in range(3):
                expression.pop(leftmost_operation_position - 1)
            expression.insert(leftmost_operation_position - 1, str(evaluated_number))
 
        return expression

    def _evaluate_factorial(self, expression: str) -> str:
        """With a given string evaluate and return its factorial."""
        raise NotImplementedError

if __name__ == "__main__":
    print(NOT_STANDALONE)
