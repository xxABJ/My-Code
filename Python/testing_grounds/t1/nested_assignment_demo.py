import inspect
import re

print("="*70)
print("SCENARIO: Attributes assigned in OTHER methods called from __init__")
print("="*70)

class TestClass:
    def __init__(self):
        # Direct assignments
        self.name = "Alice"
        
        # Call a method that ALSO assigns attributes
        self.result = self.setup_data()
        
        # Call another method
        self.configure()
    
    def setup_data(self):
        # This method assigns NEW attributes not in __init__!
        self.data_value = 100
        self.data_list = [1, 2, 3]
        return 42
    
    def configure(self):
        # This method also assigns attributes
        self.config_name = "Production"
        self.config_enabled = True


def find_all_assignments(obj):
    """
    Find ALL attribute assignments by inspecting __init__ AND any methods it calls
    """
    print("\n" + "="*70)
    print("DEEP INSPECTION: Finding all assignments")
    print("="*70)
    
    assignments = {}
    
    # Step 1: Get __init__ source
    init_source = inspect.getsource(obj.__class__.__init__)
    print(f"\n📄 Inspecting __init__ source code:")
    print("-" * 70)
    
    # Find direct assignments in __init__
    for line in init_source.split('\n'):
        match = re.search(r'self\.(\w+)\s*=\s*(.+)', line)
        if match:
            attr_name = match.group(1)
            assignment_value = match.group(2).strip()
            print(f"  Found: self.{attr_name} = {assignment_value}")
            
            # Check if it's a function call
            if '()' in assignment_value:
                assignments[attr_name] = {
                    'type': 'function_call',
                    'value': assignment_value,
                    'location': '__init__'
                }
            else:
                assignments[attr_name] = {
                    'type': 'direct_value',
                    'value': assignment_value,
                    'location': '__init__'
                }
    
    # Step 2: Find method calls in __init__
    print(f"\n🔍 Looking for method calls in __init__:")
    print("-" * 70)
    method_calls = re.findall(r'self\.(\w+)\(', init_source)
    
    called_methods = []
    for method_name in method_calls:
        if hasattr(obj, method_name) and callable(getattr(obj, method_name)):
            called_methods.append(method_name)
            print(f"  Found method call: self.{method_name}()")
    
    # Step 3: Inspect each called method for assignments
    for method_name in called_methods:
        print(f"\n📄 Inspecting {method_name}() source code:")
        print("-" * 70)
        
        method = getattr(obj.__class__, method_name)
        method_source = inspect.getsource(method)
        
        for line in method_source.split('\n'):
            match = re.search(r'self\.(\w+)\s*=\s*(.+)', line)
            if match:
                attr_name = match.group(1)
                assignment_value = match.group(2).strip()
                print(f"  Found: self.{attr_name} = {assignment_value}")
                
                assignments[attr_name] = {
                    'type': 'indirect_assignment',
                    'value': assignment_value,
                    'location': f'{method_name}() method'
                }
    
    return assignments


# Create object
obj = TestClass()

# Get all assignments
assignments = find_all_assignments(obj)

# Display results
print("\n" + "="*70)
print("COMPLETE ASSIGNMENT TRACKING:")
print("="*70)
print(f"{'Attribute':<20} {'Assignment Type':<25} {'Location':<25}")
print("-"*70)

for attr_name, info in assignments.items():
    print(f"{attr_name:<20} {info['type']:<25} {info['location']:<25}")

# Verify against actual attributes
print("\n" + "="*70)
print("VERIFICATION: Actual object attributes")
print("="*70)
actual_attrs = [attr for attr in dir(obj) if not attr.startswith('_') and not callable(getattr(obj, attr))]
print(f"Actual attributes: {actual_attrs}")

tracked_attrs = list(assignments.keys())
print(f"Tracked attributes: {tracked_attrs}")

# Check if we found everything
missing = set(actual_attrs) - set(tracked_attrs)
if missing:
    print(f"\n⚠️  Missed attributes: {missing}")
else:
    print(f"\n✅ All attributes tracked successfully!")

print("\n" + "="*70)
print("EXPLANATION:")
print("="*70)
print("""
The solution uses RECURSIVE SOURCE INSPECTION:

1. Inspect __init__ source code
2. Find all method calls: self.method_name()
3. For each called method, inspect ITS source code
4. Track assignments in those methods too

RESULT:
- self.name = "Alice"              → Found in __init__
- self.result = self.setup_data()  → Found in __init__
- self.data_value = 100            → Found in setup_data()
- self.data_list = [1, 2, 3]       → Found in setup_data()
- self.config_name = "Production"  → Found in configure()
- self.config_enabled = True       → Found in configure()

✅ This catches attributes assigned in OTHER methods!

LIMITATIONS:
- Only works if source code is available
- Won't catch dynamically created attributes (setattr, exec, etc.)
- Won't catch assignments in methods called AFTER __init__
- Requires recursive inspection for nested method calls
""")
