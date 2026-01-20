import inspect
import types

print("="*60)
print("DEMONSTRATION: inspect and types modules")
print("="*60)

# Create a test class with different types of attributes
class TestClass:
    def __init__(self):
        # Regular values
        self.name = "Alice"
        self.age = 25
        self.scores = [90, 85, 95]
        
        # Called function (stores the return value)
        self.result_called = self.calculate()
        
        # Uncalled function (stores the function reference)
        self.func_uncalled = self.calculate
    
    def calculate(self):
        return 42

# Create an instance
obj = TestClass()

print("\n1. REGULAR VALUES (strings, ints, lists, etc.)")
print("-" * 60)

attr = "name"
value = getattr(obj, attr)
print(f"Attribute: {attr} = {value}")
print(f"  inspect.ismethod({value!r}) = {inspect.ismethod(value)}  ← from 'inspect' module")
print(f"  inspect.isfunction({value!r}) = {inspect.isfunction(value)}  ← from 'inspect' module")
print(f"  isinstance({value!r}, types.BuiltinFunctionType) = {isinstance(value, types.BuiltinFunctionType)}  ← from 'types' module")
print(f"  → This is a REGULAR VALUE (string)")

print("\n" + "-" * 60)
attr = "age"
value = getattr(obj, attr)
print(f"Attribute: {attr} = {value}")
print(f"  inspect.ismethod({value!r}) = {inspect.ismethod(value)}  ← from 'inspect' module")
print(f"  inspect.isfunction({value!r}) = {inspect.isfunction(value)}  ← from 'inspect' module")
print(f"  → This is a REGULAR VALUE (integer)")

print("\n" + "-" * 60)
attr = "scores"
value = getattr(obj, attr)
print(f"Attribute: {attr} = {value}")
print(f"  inspect.ismethod({value!r}) = {inspect.ismethod(value)}  ← from 'inspect' module")
print(f"  inspect.isfunction({value!r}) = {inspect.isfunction(value)}  ← from 'inspect' module")
print(f"  → This is a REGULAR VALUE (list)")

print("\n\n2. CALLED FUNCTION (stored return value)")
print("-" * 60)

attr = "result_called"
value = getattr(obj, attr)
print(f"Attribute: {attr} = {value}")
print(f"  (This was assigned with: self.result_called = self.calculate())")
print(f"  inspect.ismethod({value!r}) = {inspect.ismethod(value)}  ← from 'inspect' module")
print(f"  inspect.isfunction({value!r}) = {inspect.isfunction(value)}  ← from 'inspect' module")
print(f"  → This is a REGULAR VALUE (the function was CALLED, returned 42)")

print("\n\n3. UNCALLED FUNCTION (stored function reference)")
print("-" * 60)

attr = "func_uncalled"
value = getattr(obj, attr)
print(f"Attribute: {attr} = {value}")
print(f"  (This was assigned with: self.func_uncalled = self.calculate)")
print(f"  inspect.ismethod({value!r}) = {inspect.ismethod(value)}  ← from 'inspect' module")
print(f"  inspect.isfunction({value!r}) = {inspect.isfunction(value)}  ← from 'inspect' module")
print(f"  callable({value!r}) = {callable(value)}  ← Python builtin")
print(f"  → This is an UNCALLED FUNCTION (no parentheses, stored the method)")

print("\n\n4. BUILTIN FUNCTIONS")
print("-" * 60)

# Builtin function example
builtin_func = len
print(f"Variable: builtin_func = {builtin_func}")
print(f"  inspect.ismethod(len) = {inspect.ismethod(builtin_func)}  ← from 'inspect' module")
print(f"  inspect.isfunction(len) = {inspect.isfunction(builtin_func)}  ← from 'inspect' module")
print(f"  isinstance(len, types.BuiltinFunctionType) = {isinstance(builtin_func, types.BuiltinFunctionType)}  ← from 'types' module")
print(f"  → This is a BUILTIN FUNCTION (like len, print, etc.)")

print("\n\n5. BUILTIN METHODS")
print("-" * 60)

# Builtin method example
text = "hello"
builtin_method = text.upper
print(f"Variable: text.upper = {builtin_method}")
print(f"  inspect.ismethod(text.upper) = {inspect.ismethod(builtin_method)}  ← from 'inspect' module")
print(f"  isinstance(text.upper, types.BuiltinMethodType) = {isinstance(builtin_method, types.BuiltinMethodType)}  ← from 'types' module")
print(f"  → This is a BUILTIN METHOD (methods on built-in types)")

print("\n\n" + "="*60)
print("SUMMARY OF WHAT EACH FUNCTION CHECKS:")
print("="*60)
print("""
FROM THE 'inspect' MODULE:
--------------------------
inspect.ismethod(x):
  → Module: inspect
  → Returns True if x is a BOUND METHOD (a function attached to an object)
  → Example: obj.calculate (without parentheses)

inspect.isfunction(x):
  → Module: inspect
  → Returns True if x is a REGULAR FUNCTION (defined with def)
  → Example: def my_func(): pass


FROM THE 'types' MODULE:
------------------------
types.BuiltinFunctionType:
  → Module: types
  → Type for BUILTIN FUNCTIONS (len, print, max, etc.)
  → Use with isinstance(x, types.BuiltinFunctionType)

types.BuiltinMethodType:
  → Module: types
  → Type for BUILTIN METHODS (like str.upper, list.append)
  → Use with isinstance(x, types.BuiltinMethodType)
""")

print("\n" + "="*60)
print("HOW WE USE THIS IN YOUR LOG CLASS:")
print("="*60)
print("""
If inspect.ismethod(value) or inspect.isfunction(value):
    # It's a function that was NOT called (no parentheses)
    # Example: self.fanccall2 = self.tt1
    
elif isinstance(value, (types.BuiltinFunctionType, types.BuiltinMethodType)):
    # It's a builtin function/method that was NOT called
    # Example: self.func = len  or  self.method = text.upper
    
else:
    # It's a regular value (could be from calling a function)
    # Example: self.fanccall = self.tt() 
    #          self.name = "Alice"
    #          self.age = 25
""")
