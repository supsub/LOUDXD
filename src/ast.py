class Number():
    def __init__(self, value):
        self.value = value
    def eval(self,context):
        return int(self.value)


class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Sum(BinaryOp):
    def eval(self,context):
        return self.left.eval(context)+self.right.eval(context)


class Sub(BinaryOp):
    def eval(self,context):
        return self.left.eval(context) - self.right.eval(context)

class Print():
    def __init__(self, value):
        self.value = value
    def eval(self,context):
        print(self.value.eval(context))

class Statement():
    def __init__(self, value):
        self.value = value
    def eval(self,context):
        return self.value.eval(context)

class Statements():
    def __init__(self,value, values):
        self.value = value
        self.values = [values]
    def eval(self,context):
        return [self.value.eval(context)]+[v.eval(context) for v in self.values]

class Assignment():
    def __init__(self,identifier,value):
        self.identifier = identifier
        self.value = value
    def eval(self,context):
        context[self.identifier.id] = self.value.eval(context)
class Identifier():
    def __init__(self,id):
        self.id = id
    def eval(self,context):
        return context[self.id]