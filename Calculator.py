"""
Scientific calculator application based on the CASIO fx-82AU PLUS II.
"""

__author__ = "Mitchell Clark"

import tkinter as tk

APP_TITLE = "ScientificCalculator"

ALLOWED_KEYBOARD_ENTERED_OPERATIONS = ('+', '-', '*', '/', '!', '(', ')')
OPERATIONS = ('+', '-', '*', '/', '!', '(', ')')

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

        self._input_screen.pack()

        # Output display.
        self._output_message = tk.StringVar()

        self._output_screen = tk.Label(self, justify=tk.RIGHT, textvariable=self._output_message)
        self._output_screen.pack()

        #
        self.calculation_processor = CalculationProcessor()
        self._master.bind('<Return>', lambda x: self._request_calculation(self._entered_operations.get()))
        self._master.mainloop()
        
    def _is_valid(self, possible_string: str) -> bool:
        """Tests a given string and returns true if it contains only allowed
        characters and false otherwise.

        Parameters:
            possible_string(str): String to be tested E.g. "2+2m".

        Allowed Characters:
            All digits 0-9 aswell as all basic operation symbols i.e. '+','-'"""
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

    def _request_calculation(self, entered_operations: str):
        self.calculation_processor.process_input(entered_operations)
        
class CalculationProcessor:
    """Handles calculating expressions given by the UI."""
    def process_input(self, entered_operations: str) -> str:
        """Process the operations in the given string."""
        for character in entered_operations:
            print('hello') 
    
class InputScreen(tk.Canvas):
    """The input screen for the calculator. Displays numbers and operations
    entered by the user."""
    def __init__(self, master: tk.Tk, **kwargs) -> None:
        """Initialises new input screen."""
        super().__init__(master)
        self.master = master
        
def main():
    """Entry point to application."""
    root = tk.Tk()
    root.title(APP_TITLE)
    calculator = CalculatorApp(root)
    

if __name__ == "__main__":
    main()
