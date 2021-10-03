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

def reduce_lambda_to_head_beta_normal_form(lambda_expression):
    args, f = [], lambda_expression
    while not isinstance(f, Variable):
        if isinstance(f, Application):
            a, f = f.argument, f.funcion
            args.append(a)
        elif args:
            f = f.body.substitute(1, args.pop().reindex(1, 1)).reindex(2, -1)
        else:
            break
    while args:
        f = Application(args.pop(), f)
    return f

def string_to_lambda_expression(source):
    IGNORED_CHARACTERS = ' \t\n'
    def skipl(i):
        while i < len(source) and source[i] in IGNORED_CHARACTERS:
            i += 1
        return i
    def str_to_expression(start):
        start = skipl(start)
        if source[start] in "&":
            body, end = str_to_expression(start + 1)
            return Function(body), end
        v, i = str_to_simple_expression(start)
        if i < len(source) and source[i] in "!":
            f, end = str_to_expression(i + 1)
            return Application(v, f), end
        return v, i
    def str_to_simple_expression(start):
        start = skipl(start)
        if source[start] in "(":
            e, i = str_to_expression(start + 1)
            return e, skipl(i + 1)
        i = start
        while i < len(source) and source[i] in "0123456789":
            i += 1
        return Variable(int(source[start:i])), skipl(i)
    return str_to_expression(0)[0]
