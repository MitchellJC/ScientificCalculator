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
        expression = self._evaluate_basic_operators(expression, MULTIPLICATION_AND_DIVISION)
        expression = self._evaluate_basic_operators(expression, ADDITION_AND_SUBTRACTION)

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
        # Not implemented.
        return expression

    def _evaluate_basic_operators(self, expression: str, operator_pair: str) -> str:
        """Find all operators given in operator pair and evaluate them. The operator pair can contain multiplication and division, or addition and subtraction.
        Return partially evaluated expression."""
        # Need to fix for large numbers where scientific notation appears.
        operator_symbol1, operator_symbol2 = OPERATOR_SYMBOLS[operator_pair]
        while operator_symbol1 in expression[1:] or operator_symbol2 in expression[1:]: # expression[1:] takes into account (-)ve nums.
            left_number_indices = []
            right_number_indices = []
            finding_left_number = True
            operation1 = False
            operation2 = False
            
            for index in range(len(expression)):  
                character = expression[index]
                # Find nums on the left and right of the leftmost operator.
                if character in NUMBER_PARTS:
                    if finding_left_number:
                        left_number_indices.append(index)
                    else:
                        right_number_indices.append(index)
                elif operation1 or operation2:
                    break        
                elif character is operator_symbol1 and index != 0:
                    operation1 = True
                    finding_left_number = False
                elif character is operator_symbol2 and index != 0:
                    operation2 = True
                    finding_left_number = False
                else:
                    left_number_indices = []

            # Extract left and right nums from expression.
            left_number_start_index = left_number_indices[0]
            left_number_end_index = left_number_indices[-1]
            right_number_start_index = right_number_indices[0]
            right_number_end_index = right_number_indices[-1]
            left_number = expression[left_number_start_index:left_number_end_index + 1]
            right_number = expression[right_number_start_index:right_number_end_index + 1]
            left_number = float(left_number)
            right_number = float(right_number)
            
            if operation1:
                if operator_pair == MULTIPLICATION_AND_DIVISION:
                    calculated_number = left_number * right_number
                else:
                    calculated_number = left_number + right_number
            elif operation2:
                if operator_pair == MULTIPLICATION_AND_DIVISION:
                    calculated_number = left_number / right_number
                else:
                    calculated_number = left_number - right_number
                
            calculated_number = str(calculated_number)
            old_part_of_expression = expression[left_number_start_index:right_number_end_index + 1]
            expression = expression.replace(old_part_of_expression, calculated_number)
 
        return expression

    def _evaluate_factorial(self, expression: str) -> str:
        """With a given string evaluate and return its factorial."""
        raise NotImplementedError

if __name__ == "__main__":
    print(NOT_STANDALONE)
