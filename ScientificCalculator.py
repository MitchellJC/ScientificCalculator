"""Scientific calculator application based on the CASIO fx-82AU PLUS II."""

from CalculatorView import *

def main():
    """Entry point to application."""
    root = tk.Tk()
    root.title(APP_TITLE)
    calculator = CalculatorApp(root)
    

if __name__ == "__main__":
    main()
