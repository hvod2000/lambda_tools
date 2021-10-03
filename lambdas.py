class Application:
    def __init__(self, argument, funcion):
        self.argument, self.funcion = argument, funcion
    def __repr__(self):
        return f"funcion({repr(self.argument)}, {repr(self.funcion)})"
    def __str__(self):
        a = (str(self.argument) if isinstance(self.argument, Variable)
            else f"({self.argument})")
        return f"{a}!{self.funcion}"
    def reindex(self, min_index, delta):
        a = self.argument.reindex(min_index, delta)
        f = self.funcion.reindex(min_index, delta)
        return Application(a, f)
    def substitute(self, variable, value):
        a = self.argument.substitute(variable, value)
        f = self.funcion.substitute(variable, value)
        return Application(a, f)
class Function:
    def __init__(self, body):
        self.body = body
    def __repr__(self):
        return f"Function({repr(self.body)})"
    def __str__(self):
        return f"&{self.body}"
    def reindex(self, min_index, delta):
        return Function(self.body.reindex(min_index + 1, delta))
    def substitute(self, variable, value):
        return Function(self.body.substitute(variable + 1, value.reindex(1, 1)))
class Variable:
    def __init__(self, nesting_level):
        self.nesting_level = nesting_level
    def __repr__(self):
        return f"Variable({self.nesting_level})"
    def __str__(self):
        return f"{self.nesting_level}"
    def reindex(self, min_index, delta):
        return self if self.nesting_level < min_index else Variable(self.nesting_level + delta)
    def substitute(self, variable, value):
        return value if variable == self.nesting_level else self
