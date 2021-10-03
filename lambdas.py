class Application:
    def __init__(self, argument, funcion):
        self.argument, self.funcion = argument, funcion
class Function:
    def __init__(self, body):
        self.body = body
class Variable:
    def __init__(self, nesting_level):
        self.nesting_level = nesting_level
