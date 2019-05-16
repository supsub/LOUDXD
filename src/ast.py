from rply.token import BaseBox

from src.exceptions import *
import more_itertools

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
        return self.left.eval(context)-self.right.eval(context)

class Bigger(BinaryOp):
    def eval(self,context):
        return (self.left.eval(context)) > (self.right.eval(context))
    
class Smaller(BinaryOp):
    def eval(self,context):
        return (self.left.eval(context)) < (self.right.eval(context))
    
class Equal(BinaryOp):
    def eval(self,context):
        return (self.left.eval(context)) == (self.right.eval(context))
    
class NtEqual(BinaryOp):
    def eval(self,context):
        return (self.left.eval(context)) != (self.right.eval(context))
    

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
        if self.id.value not in context.keys():
            raise ZlyKlucz(self.id)
        return context[self.id.value]

class Increment():
    def __init__(self,identifier,value):
        self.identifier = identifier
        self.value = value
    def eval(self,context):
        if self.identifier.value not in context.keys():
            raise ZlyKlucz(self.identifier)
        context[self.identifier.value] += self.value.eval(context)


class Decrement():
    def __init__(self,identifier,value):
        self.identifier = identifier
        self.value = value
    def eval(self,context):
        if self.identifier.value not in context.keys():
            raise ZlyKlucz(self.identifier)
        context[self.identifier.value] -= self.value.eval(context)
        
class IfStatement():
    def __init__(self, boolean, body):
        self.boolean = boolean
        self.body = body
    def eval(self, context):
        if self.boolean.eval(context):
            self.body.eval(context)

class String():
    def __init__(self,value, var=None):
        self.value = value[1:-1]
        self.var = var
    def eval(self,context):
        if self.var is not None:
            self.var =  list(more_itertools.collapse(self.var))
            self.var = [var.eval(context) for var in self.var]
            return self.value.replace("_","{}").format(*self.var)
        return self.value
