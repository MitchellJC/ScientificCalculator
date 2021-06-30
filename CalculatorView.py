"""View classes for ScientificCalculator.py"""

__author__ = "Mitchell Clark"

import tkinter as tk
from CalculatorModel import *

class CalculatorApp(tk.Frame):
    """The main calculator UI application which contains an input screen and
    and buttons."""
    def __init__(self, master: tk.Tk, **kwargs) -> None:
        """Initialises a new calculator app."""
        super().__init__(master, **kwargs)
        self.pack()
        
        self._master = master

        # Input display.
        self._entered_operations = tk.StringVar()
        self._is_valid_command = self.register(self._is_valid)
        self._input_screen = tk.Entry(self, textvariable=self._entered_operations,\
                                      validate='key', \
                                      validatecommand=(self._is_valid_command,'%S'))
        self._input_screen.pack(fill=tk.X)

        # Output display.
        self._output_message = tk.StringVar()
        self._output_screen = tk.Label(self, justify=tk.RIGHT, textvariable=self._output_message, bg="white", anchor=tk.E)
        self._output_screen.pack(fill=tk.X)

        self._buttons_ui = ButtonsUI(self)
        self._buttons_ui.pack()

        self._calculation_processor = CalculationProcessor()
        self._last_answer = ""
        
        self._master.bind('<Return>', self.request_calculation)
        self._master.mainloop()
        
    def _is_valid(self, possible_string: str) -> bool:
        """Tests a given string and returns true if it contains only allowed
        characters and false otherwise."""
        valid = True
        for character in possible_string:
            character_valid = True
            if character.isdigit():
                continue
            elif character in ALLOWED_KEYBOARD_ENTERED_OPERATIONS:
                continue
            else:
                valid = False
                break

        return valid

    def add_to_display(self, input_to_add: str) -> None:
        """Adds given input to the input screen."""
        current_input = self._entered_operations.get()
        current_input += input_to_add
        self._entered_operations.set(current_input)
        self._input_screen.icursor(len(current_input))
        

    def all_clear(self) -> None:
        """Clear the input display."""
        self._entered_operations.set("")
        self._output_message.set("")

    def delete(self) -> None:
        """Deletes the character behind the cursor location or deletes the last character if cursor is not on input display."""
        cursor_position = self._input_screen.index(tk.INSERT)
        current_input = self._entered_operations.get()
        if cursor_position == 0:
            current_input = current_input[:-1]
        else:
            current_input = current_input[:cursor_position - 1] + current_input[cursor_position:]
            self._input_screen.icursor(cursor_position - 1)
            
        self._entered_operations.set(current_input)    
    
    def request_calculation(self, event: tk.Event = None) -> None:
        """Sends current input screen to the CalculationProcessor."""
        entered_operations = self._entered_operations.get()
        final_evaluation = self._calculation_processor.process_input(entered_operations)
        self._output_message.set(final_evaluation)
        

    
class ButtonsUI(tk.Frame):
    """Interface for all buttons on the calculator."""
    def __init__(self, master: tk.Tk, **kwargs) -> None:
        """Initialises new ButtonsUI."""
        super().__init__(master)

        # First row.
        self._row_one = tk.Frame(self)
        self._row_one.pack()

        self._abs_button = tk.Button(self._row_one, text=ABSOLUTE_VALUE, \
                                     width=BUTTON_WIDTH)
        self._abs_button.pack(side=tk.LEFT)
        self._cubed_button = tk.Button(self._row_one, text=X_CUBED, \
                                     width=BUTTON_WIDTH)
        self._cubed_button.pack(side=tk.LEFT)
        self._inverse_button = tk.Button(self._row_one, text=X_INVERSE, \
                                     width=BUTTON_WIDTH)
        self._inverse_button.pack(side=tk.LEFT)
        self._factorial_button = tk.Button(self._row_one, text=X_FACTORIAL, \
                                     width=BUTTON_WIDTH)
        self._factorial_button.pack(side=tk.LEFT)

        # Second row.
        self._row_two = tk.Frame(self)
        self._row_two.pack()

        self._fraction_button = tk.Button(self._row_two, text=FRACTION, \
                                     width=BUTTON_WIDTH)
        self._fraction_button.pack(side=tk.LEFT)
        self._square_root_button = tk.Button(self._row_two, text=X_ROOTED, \
                                     width=BUTTON_WIDTH)
        self._square_root_button.pack(side=tk.LEFT)
        self._squared_button = tk.Button(self._row_two, text=X_SQUARED, \
                                     width=BUTTON_WIDTH)
        self._squared_button.pack(side=tk.LEFT)
        self._powered_button = tk.Button(self._row_two, text=X_POWERED, \
                                     width=BUTTON_WIDTH)
        self._powered_button.pack(side=tk.LEFT)
        self._log_button = tk.Button(self._row_two, text=LOG, \
                                     width=BUTTON_WIDTH)
        self._log_button.pack(side=tk.LEFT)
        self._ln_button = tk.Button(self._row_two, text=LN, \
                                     width=BUTTON_WIDTH)
        self._ln_button.pack(side=tk.LEFT)

        # Third row.
        self._row_three = tk.Frame(self)
        self._row_three.pack()

        self._negative_sign_button = tk.Button(self._row_three, text=NEGATIVE_SIGN, \
                                     width=BUTTON_WIDTH)
        self._negative_sign_button.pack(side=tk.LEFT)
        self._timecalc_button = tk.Button(self._row_three, text=TIME_CALCULATIONS, \
                                     width=BUTTON_WIDTH)
        self._timecalc_button.pack(side=tk.LEFT)
        self._hyperbolic_button = tk.Button(self._row_three, text=HYPERBOLIC, \
                                     width=BUTTON_WIDTH)
        self._hyperbolic_button.pack(side=tk.LEFT)
        self._sin_button = tk.Button(self._row_three, text=SIN, \
                                     width=BUTTON_WIDTH)
        self._sin_button.pack(side=tk.LEFT)

        self._cos_button = tk.Button(self._row_three, text=COS, \
                                     width=BUTTON_WIDTH)
        self._cos_button.pack(side=tk.LEFT)
        self._tan_button = tk.Button(self._row_three, text=TAN, \
                                     width=BUTTON_WIDTH)
        self._tan_button.pack(side=tk.LEFT)

        # Fourth row.
        self._row_four = tk.Frame(self)
        self._row_four.pack()

        self._RCL_button = tk.Button(self._row_four, text=RCL, \
                                     width=BUTTON_WIDTH)
        self._RCL_button.pack(side=tk.LEFT)
        self._ENG_button = tk.Button(self._row_four, text=ENG, \
                                     width=BUTTON_WIDTH)
        self._ENG_button.pack(side=tk.LEFT)
        self._left_bracket_button = tk.Button(self._row_four, text=LEFT_BRACKET, \
                                     width=BUTTON_WIDTH, command=lambda: master.add_to_display(LEFT_BRACKET))
        self._left_bracket_button.pack(side=tk.LEFT)
        self._right_bracket_button = tk.Button(self._row_four, text=RIGHT_BRACKET, \
                                     width=BUTTON_WIDTH, command=lambda: master.add_to_display(RIGHT_BRACKET))
        self._right_bracket_button.pack(side=tk.LEFT)
        self._standard_and_decimal_button = tk.Button(self._row_four, text=STANDARD_AND_DECIMAL, \
                                     width=BUTTON_WIDTH)
        self._standard_and_decimal_button.pack(side=tk.LEFT)
        self._mplus_button = tk.Button(self._row_four, text=M_PLUS, \
                                     width=BUTTON_WIDTH)
        self._mplus_button.pack(side=tk.LEFT)

        # Fifth row.
        self._row_five = tk.Frame(self)
        self._row_five.pack()

        self._seven_button = tk.Button(self._row_five, text=SEVEN, \
                                     width=BUTTON_WIDTH, command=lambda: master.add_to_display(SEVEN))
        self._seven_button.pack(side=tk.LEFT)
        self._eight_button = tk.Button(self._row_five, text=EIGHT, \
                                     width=BUTTON_WIDTH, command=lambda: master.add_to_display(EIGHT))
        self._eight_button.pack(side=tk.LEFT)
        self._nine_button = tk.Button(self._row_five, text=NINE, \
                                     width=BUTTON_WIDTH, command=lambda: master.add_to_display(NINE))
        self._nine_button.pack(side=tk.LEFT)
        self._delete_button = tk.Button(self._row_five, text=DELETE, \
                                     width=BUTTON_WIDTH, command=master.delete)
        self._delete_button.pack(side=tk.LEFT)
        self._all_clear_button = tk.Button(self._row_five, text=ALL_CLEAR, \
                                     width=BUTTON_WIDTH, command=master.all_clear)
        self._all_clear_button.pack(side=tk.LEFT)

        # Sixth row.
        self._row_six = tk.Frame(self)
        self._row_six.pack()

        self._four_button = tk.Button(self._row_six, text=FOUR, \
                                     width=BUTTON_WIDTH, command=lambda: master.add_to_display(FOUR))
        self._four_button.pack(side=tk.LEFT)
        self._five_button = tk.Button(self._row_six, text=FIVE, \
                                     width=BUTTON_WIDTH, command=lambda: master.add_to_display(FIVE))
        self._five_button.pack(side=tk.LEFT)
        self._six_button = tk.Button(self._row_six, text=SIX, \
                                     width=BUTTON_WIDTH, command=lambda: master.add_to_display(SIX))
        self._six_button.pack(side=tk.LEFT)
        self._multiply_button = tk.Button(self._row_six, text=MULTIPLY, \
                                     width=BUTTON_WIDTH, command=lambda: master.add_to_display(MULTIPLY))
        self._multiply_button.pack(side=tk.LEFT)
        self._divide_button = tk.Button(self._row_six, text=DIVIDE, \
                                     width=BUTTON_WIDTH, command=lambda: master.add_to_display(DIVIDE))
        self._divide_button.pack(side=tk.LEFT)

        # Seventh row.
        self._row_seven = tk.Frame(self)
        self._row_seven.pack()

        self._one_button = tk.Button(self._row_seven, text=ONE, \
                                     width=BUTTON_WIDTH, command=lambda: master.add_to_display(ONE))
        self._one_button.pack(side=tk.LEFT)
        self._two_button = tk.Button(self._row_seven, text=TWO, \
                                     width=BUTTON_WIDTH, command=lambda: master.add_to_display(TWO))
        self._two_button.pack(side=tk.LEFT)
        self._three_button = tk.Button(self._row_seven, text=THREE, \
                                     width=BUTTON_WIDTH, command=lambda: master.add_to_display(THREE))
        self._three_button.pack(side=tk.LEFT)
        self._plus_button = tk.Button(self._row_seven, text=PLUS, \
                                     width=BUTTON_WIDTH, command=lambda: master.add_to_display(PLUS))
        self._plus_button.pack(side=tk.LEFT)
        self._minus_button = tk.Button(self._row_seven, text=MINUS, \
                                     width=BUTTON_WIDTH, command=lambda: master.add_to_display(MINUS))
        self._minus_button.pack(side=tk.LEFT)

        # Eighth row.
        self._row_eight = tk.Frame(self)
        self._row_eight.pack()

        self._zero_button = tk.Button(self._row_eight, text=ZERO, \
                                     width=BUTTON_WIDTH, command=lambda: master.add_to_display(ZERO))
        self._zero_button.pack(side=tk.LEFT)
        self._dot_button = tk.Button(self._row_eight, text=DOT, \
                                     width=BUTTON_WIDTH, command=lambda: master.add_to_display(DOT))
        self._dot_button.pack(side=tk.LEFT)
        self._scientific_notation_button = tk.Button(self._row_eight, text=SCIENTIFIC_NOTATION, \
                                     width=BUTTON_WIDTH)
        self._scientific_notation_button.pack(side=tk.LEFT)
        self._answer_button = tk.Button(self._row_eight, text=ANSWER, \
                                     width=BUTTON_WIDTH, command=lambda: master.add_to_display(ANSWER))
        self._answer_button.pack(side=tk.LEFT)
        self._equals_button = tk.Button(self._row_eight, text=EQUALS, \
                                     width=BUTTON_WIDTH, command=master.request_calculation)
        self._equals_button.pack(side=tk.LEFT)
        
if __name__ == "__main__":
    print(NOT_STANDALONE)
