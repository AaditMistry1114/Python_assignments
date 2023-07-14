
class Add(Exception):
    def add(a,b):
        def __init__(self,*args: object):
         super().__init__(*args)
        try:
            if a == None or b == None:
                raise Add('insufficient arguments')
            print(a + b)
        except Add as a:
           print(a.args[0])

class Sub(Exception):
    def sub(a,b):
        def __init__(self,*args: object):
         super().__init__(*args)
        try:
            if a == None or b == None:
                pass 
            elif a == None and b == None:
                raise Sub('insufficient arguments')
            print(a - b)
        except Sub as b:
           print(b.args[0])

class Mul(Exception):
    def mul(a,b):
        def __init__(self,*args: object):
         super().__init__(*args)
        try:
            if a == None or b == None:
                pass 
            elif a == None and b == None:
                raise Mul('insufficient arguments')
            print(a * b)
        except Mul as m:
           print(m.args[0])

class Div(Exception):
    def div(a,b):
        def __init__(self,*args: object):
         super().__init__(*args)
        try:
            if a == None or b == None:
                pass 
            elif a == None and b == None:
                raise Div('insufficient arguments')
            print(a / b)
        except Div as d:
           print(d.args[0])

class FloorDiv(Exception):
    def floordiv(a,b):
        def __init__(self,*args: object):
         super().__init__(*args)
        try:
            if a == None or b == None:
                pass 
            elif a == None and b == None:
                raise FloorDiv('insufficient arguments')
            print(a // b)
        except FloorDiv as fd:
           print(fd.args[0])


class Exponent(Exception):
    def expo(a,b):
        def __init__(self,*args: object):
         super().__init__(*args)
        try:
            if a == None or b == None:
                pass 
            elif a == None and b == None:
                raise Exponent('insufficient arguments')
            print(a ** b)
        except Exponent as e:
           print(e.args[0])

class Mod(Exception):
    def mod(a,b):
        def __init__(self,*args: object):
         super().__init__(*args)
        try:
            if a == None or b == None:
                pass 
            elif a == None and b == None:
                raise Mod('insufficient arguments')
            print(a ** b)
        except Mod as m:
           print(m.args[0])











