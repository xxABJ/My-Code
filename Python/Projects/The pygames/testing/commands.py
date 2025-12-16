#abs()
abs_a = 10.165
abs_a2 = 2
# returns the absolute value of a number | x |
abs_b = abs(abs_a2 - abs_a)
no_abs_b = abs_a2 - abs_a
print(f"abs_b: {abs_b} , no_abs_b: {no_abs_b}")
print()

#aiter()

#all()

#__repr__()
class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   # this is intended for representing the class for developers
   def __repr__(self):
      return f"__repr__ Person is (self.name: '{self.name}', self.age: {self.age})" 
print(Person("ali", 27))
print()

#ascii()
ascii_s = 'cafe'
ascii_s2 = 'café'
print(f"ascii_s('cafe'): {ascii(ascii_s)} , ascii_s2('café'): {ascii(ascii_s2)}")
print()

#bin()
bin_a = 20
bin_a2 = 7
print(f"bin_a(20): {bin(bin_a)} , bin_a2(7): {bin(bin_a2)}")
print()

#bool()
class bool_test1():
    def __init__(self, obj):
        self.obj = obj
    
    def __bool__(self):
        return False
    
class bool_test2():
    def __init__(self, obj):
        self.obj = obj
    
    #def __bool__(self):
    #   return False

class bool_test3():
    def __init__(self, obj):
        self.obj = obj
        self.list = []
        for ind, value in enumerate(str(self.obj)):
            self.list.append(value)
        self.length = len(self.list)
        #print(self.list, self.length)
    
    def __len__(self):
        if self.length == 5:
            return 0
        return self.length
    

print("explicitly returning False at __bool__() even though @bool_test1.__init__(obj) is True due to it not being zero in lenght or a NoneType:\t", bool(bool_test1(10)))
print("commenting on what was done in the previous calling which in boolean context defaults to True for it being not a NoneType or having more than zero length:\t", bool(bool_test2(10)))
print(F"adding specific (return 0 if length is 5) conditions where __len__() would return False even though the length is not zero:\t obj=123456:len=6 ({bool(bool_test3(123456))}), obj=1234:len=4 ({bool(bool_test3(1234))}), obj=12345:len=5 ({bool(bool_test3(12345))})")
print()

#breakpoint()
def double(x):
   breakpoint()
   return x * 2
val = 3
# This built-in function takes in args and pauses right after it is called and makes you able contniue in the debugger
#print(f"{val} * 2 is {double(val)}")
