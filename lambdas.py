class Application:
    def __init__(self, argument, funcion):
        self.argument, self.funcion = argument, funcion
    def __repr__(self):
        return f"funcion({repr(self.argument)}, {repr(self.funcion)})"
    def __str__(self):
        a = (str(self.argument) if isinstance(self.argument, Variable)
            else f"({self.argument})")
        return f"{a}!{self.funcion}"
class Function:
    def __init__(self, body):
        self.body = body
    def __repr__(self):
        return f"Function({repr(self.body)})"
    def __str__(self):
        return f"&{self.body}"
class Variable:
    def __init__(self, nesting_level):
        self.nesting_level = nesting_level
    def __repr__(self):
        return f"Variable({self.nesting_level})"
    def __str__(self):
        return f"{self.nesting_level}"
