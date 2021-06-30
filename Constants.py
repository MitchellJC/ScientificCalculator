APP_TITLE = "ScientificCalculator"
NOT_STANDALONE = "This is not a standalone module. Please run ScientificCalculator.py."

BUTTON_WIDTH = 8
INPUT_DISPLAY_WIDTH = BUTTON_WIDTH*8

# Button names.
# Row one.
ABSOLUTE_VALUE = "Abs"
X_CUBED = "x^3"
X_INVERSE = "x^(-1)"
X_FACTORIAL = "x!"

# Row two.
FRACTION = "□/■"
X_ROOTED = "√(□)"
X_SQUARED = "x^2"
X_POWERED = "x^□"
LOG = "log"
LN = "ln"

# Row three.
NEGATIVE_SIGN = "(-)"
TIME_CALCULATIONS  = "° ' ''"
HYPERBOLIC = "hyp"
SIN = "sin"
COS = "cos"
TAN = "tan"

# Row four.
RCL = "RCL"
ENG = "ENG"
LEFT_BRACKET = "("
RIGHT_BRACKET = ")"
STANDARD_AND_DECIMAL = "S<->D"
M_PLUS = "M+"

# Row five.
SEVEN = "7"
EIGHT = "8"
NINE = "9"
DELETE = "DEL"
ALL_CLEAR = "AC"

# Row six.
FOUR = "4"
FIVE = "5"
SIX  = "6"
MULTIPLY = "×"
DIVIDE = "÷"

# Row seven.
ONE = "1"
TWO = "2"
THREE = "3"
PLUS = "+"
MINUS = "-"

# Row eight.
ZERO = "0"
DOT = "."
SCIENTIFIC_NOTATION = "×10^x"
ANSWER = "Ans"
EQUALS = "="

BRACKETS = (LEFT_BRACKET, RIGHT_BRACKET)
ALLOWED_KEYBOARD_ENTERED_OPERATIONS = ('+', '-', '×', '/', '!', '(', ')', '.')
OPERATIONS = ('+', '-', '×', '/', '!', '(', ')')
ADVANCED_OPERATIONS = ('^', '√', '!', '|', 'log', 'ln', 'sin', 'cos', 'tan')
NUMBER_PARTS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.')
MATH_ERROR = "Math ERROR"
SYNTAX_ERROR = "Syntax ERROR"

BLANK = ""

if __name__ == "__main__":
    print(NOT_STANDALONE)
