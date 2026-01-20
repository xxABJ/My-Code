import inspect
import re
import ast

print("="*70)
print("DETECTING IF ATTRIBUTE WAS ASSIGNED FROM A FUNCTION CALL")
print("="*70)

class TestClass:
    def __init__(self):
        # Direct assignments (NO function call)
        self.name = "Alice"
        self.age = 25
        self.scores = [90, 85, 95]
        
        # Assigned FROM a function call (WITH parentheses)
        self.result_called = self.calculate()
        self.result_called2 = self.another_func()
        
        # Assigned to a function reference (WITHOUT parentheses)
        self.func_uncalled = self.calculate
    
    def calculate(self):
        return 42
    
    def another_func(self):
        return "Hello"


def analyze_attribute_assignment(obj, attr_name):
    """
    Analyze how an attribute was assigned by inspecting the source code
    """
    print(f"\n{'='*70}")
    print(f"ANALYZING: {attr_name}")
    print(f"{'='*70}")
    
    # Get the current value
    attr_value = getattr(obj, attr_name)
    print(f"Current value: {attr_value!r}")
    print(f"Type: {type(attr_value)}")
    
    # Get the source code of __init__
    try:
        source = inspect.getsource(obj.__class__.__init__)
        print(f"\nSearching in __init__ source code...")
        
        # Look for the assignment line
        # Pattern: self.attr_name = something
        pattern = rf'self\.{attr_name}\s*=\s*(.+)'
        match = re.search(pattern, source)
        
        if match:
            assignment_value = match.group(1).strip()
            print(f"Found assignment: self.{attr_name} = {assignment_value}")
            
            # Check if it's a function call (has parentheses)
            # Pattern: something() - but not inside quotes
            if '()' in assignment_value:
                # Check if it's calling a method
                if 'self.' in assignment_value and '()' in assignment_value:
                    func_name = re.search(r'self\.(\w+)\(\)', assignment_value)
                    if func_name:
                        print(f"✅ ASSIGNED FROM FUNCTION CALL: self.{func_name.group(1)}()")
                        return "function_call"
                else:
                    print(f"✅ ASSIGNED FROM FUNCTION CALL: {assignment_value}")
                    return "function_call"
            
            # Check if it's a function reference (no parentheses, but refers to self.method)
            elif re.match(r'self\.\w+$', assignment_value):
                # It's referring to self.something without ()
                method_name = assignment_value.replace('self.', '')
                if hasattr(obj, method_name) and callable(getattr(obj, method_name)):
                    print(f"✅ ASSIGNED AS FUNCTION REFERENCE (uncalled): {assignment_value}")
                    return "function_reference"
            
            # Direct value assignment
            print(f"✅ DIRECT VALUE ASSIGNMENT: {assignment_value}")
            return "direct_value"
        else:
            print(f"❌ Could not find assignment in __init__")
            return "unknown"
            
    except Exception as e:
        print(f"❌ Error analyzing: {e}")
        return "error"


# Create test object
obj = TestClass()

# Analyze each attribute
print("\n" + "="*70)
print("ANALYSIS RESULTS:")
print("="*70)

attributes = ['name', 'age', 'scores', 'result_called', 'result_called2', 'func_uncalled']

results = {}
for attr in attributes:
    result = analyze_attribute_assignment(obj, attr)
    results[attr] = result

# Summary
print("\n" + "="*70)
print("SUMMARY TABLE:")
print("="*70)
print(f"{'Attribute':<20} {'Type':<25} {'Assignment Method':<20}")
print("-"*70)
for attr in attributes:
    value = getattr(obj, attr)
    value_type = type(value).__name__
    assignment = results[attr]
    print(f"{attr:<20} {value_type:<25} {assignment:<20}")

print("\n" + "="*70)
print("EXPLANATION:")
print("="*70)
print("""
✅ FUNCTION_CALL:
   - Attribute was assigned by CALLING a function with ()
   - Example: self.result_called = self.calculate()
   - The value is the RETURN VALUE of the function

✅ FUNCTION_REFERENCE:
   - Attribute was assigned a function reference WITHOUT ()
   - Example: self.func_uncalled = self.calculate
   - The value IS the function itself (callable)

✅ DIRECT_VALUE:
   - Attribute was assigned a direct value
   - Example: self.name = "Alice"
   - No function involved in the assignment
""")
