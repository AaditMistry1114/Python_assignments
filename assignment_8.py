# Define a custom exception class for accessing private members
class PrivateAccessError(Exception):
    def __init__(self, message):
        super().__init__(message)

class A:
    def __init__(self, a, b, c):
        self.__a = a # private member
        self._b = b # protected member
        self.c = c # public member

    def display(self):
        print("Values of a, b and c in class A are:")
        try:
            print(self.__a) # try to access the private member
        except AttributeError as e:
            # raise a custom exception with a personalized message
            raise PrivateAccessError("You cannot access the private member a of class A") from e
        print(self._b)
        print(self.c)

class B(A):
    def display(self):
        print("Values of a, b and c in class B are:")
        try:
            print(self.__a) 
        except AttributeError as e:
            raise PrivateAccessError("You cannot access the private member a of class A") from e
        print(self._b)
        print(self.c)

obj_a = A(10, 20, 30)

obj_b = B(40, 50, 60)

try:
    obj_a.display()
except PrivateAccessError as e:
    print(e)

try:
    obj_b.display()
except PrivateAccessError as e:
    print(e)
