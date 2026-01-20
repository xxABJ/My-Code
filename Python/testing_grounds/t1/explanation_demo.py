import inspect  # ← FROM 'inspect' MODULE
import re       # ← FROM 're' MODULE (regular expressions)

print("="*80)
print("DETAILED EXPLANATION: How Source Inspection Works")
print("="*80)

# Sample class for demonstration
class MyClass:
    def __init__(self):
        self.name = "Alice"
        self.result = self.calculate()
        self.func_ref = self.calculate
    
    def calculate(self):
        return 42


# ============================================================================
# PART 1: inspect.getsource() - Get Source Code as String
# ============================================================================
print("\n" + "="*80)
print("PART 1: inspect.getsource() - FROM 'inspect' MODULE")
print("="*80)

print("\nWhat it does: Gets the source code of a function/method as a string\n")

# Get source code of __init__
source_code = inspect.getsource(MyClass.__init__)

print("Source code of MyClass.__init__:")
print("-" * 80)
print(source_code)
print("-" * 80)

print("\nType:", type(source_code))
print("It's just a regular string! We can search through it.")


# ============================================================================
# PART 2: String Methods - split('\n') to Get Lines
# ============================================================================
print("\n\n" + "="*80)
print("PART 2: string.split('\\n') - Python BUILTIN String Method")
print("="*80)

print("\nWhat it does: Splits a string into a list of lines\n")

lines = source_code.split('\n')

print("Lines in __init__:")
print("-" * 80)
for i, line in enumerate(lines, 1):
    print(f"Line {i}: {line!r}")


# ============================================================================
# PART 3: re.search() - Find Patterns with Regular Expressions
# ============================================================================
print("\n\n" + "="*80)
print("PART 3: re.search() - FROM 're' MODULE (Regular Expressions)")
print("="*80)

print("\nWhat it does: Searches for a pattern in a string\n")

test_line = "        self.name = \"Alice\""
pattern = r'self\.(\w+)\s*=\s*(.+)'

print(f"Test line: {test_line!r}")
print(f"Pattern: {pattern!r}")
print("\nPattern breakdown:")
print("  self\\.        → Matches literal 'self.'")
print("  (\\w+)         → Captures word characters (attribute name)")
print("  \\s*           → Matches optional whitespace")
print("  =             → Matches literal '='")
print("  \\s*           → Matches optional whitespace")
print("  (.+)          → Captures everything after = (the value)")

match = re.search(pattern, test_line)

if match:
    print("\n✅ Pattern matched!")
    print(f"  Full match: {match.group(0)!r}")
    print(f"  Group 1 (attribute name): {match.group(1)!r}")
    print(f"  Group 2 (value): {match.group(2)!r}")
else:
    print("\n❌ Pattern did not match")


# ============================================================================
# PART 4: re.match() vs re.search()
# ============================================================================
print("\n\n" + "="*80)
print("PART 4: re.match() vs re.search() - FROM 're' MODULE")
print("="*80)

test_string = "prefix self.method"

print(f"\nTest string: {test_string!r}")
print(f"Pattern: r'^self\\.\\w+$'\n")

print("re.match() - FROM 're' MODULE:")
print("  → Checks if pattern matches at the START of string")
result = re.match(r'^self\.\w+$', test_string)
print(f"  Result: {result}  (None because 'prefix' is at start)\n")

print("re.search() - FROM 're' MODULE:")
print("  → Searches for pattern ANYWHERE in string")
result = re.search(r'self\.\w+', test_string)
print(f"  Result: {result}  (Found at position 7)")
if result:
    print(f"  Matched: {result.group(0)!r}")


# ============================================================================
# PART 5: re.findall() - Find All Matches
# ============================================================================
print("\n\n" + "="*80)
print("PART 5: re.findall() - FROM 're' MODULE")
print("="*80)

print("\nWhat it does: Finds ALL occurrences of a pattern\n")

test_code = """
self.method1()
self.method2()
self.method3()
"""

pattern = r'self\.(\w+)\('
matches = re.findall(pattern, test_code)

print(f"Code:\n{test_code}")
print(f"Pattern: {pattern!r}")
print(f"  → Finds: self.METHOD_NAME(")
print(f"\nAll matches: {matches}")


# ============================================================================
# PART 6: dir() and getattr() - Object Introspection
# ============================================================================
print("\n\n" + "="*80)
print("PART 6: dir() and getattr() - Python BUILTINS")
print("="*80)

obj = MyClass()

print("\ndir(obj) - Python BUILTIN:")
print("  → Returns list of all attribute/method names")
all_names = dir(obj)
print(f"  {all_names}\n")

print("getattr(obj, name) - Python BUILTIN:")
print("  → Gets the value of an attribute by name (string)")

for name in ['name', 'result', 'func_ref']:
    value = getattr(obj, name)
    print(f"  getattr(obj, '{name}') = {value!r}")


# ============================================================================
# PART 7: callable() - Check if Something Can Be Called
# ============================================================================
print("\n\n" + "="*80)
print("PART 7: callable() - Python BUILTIN")
print("="*80)

print("\nWhat it does: Checks if an object can be called like a function\n")

examples = [
    ('obj.name', obj.name),
    ('obj.result', obj.result),
    ('obj.func_ref', obj.func_ref),
    ('obj.calculate', obj.calculate),
]

for name, value in examples:
    is_callable = callable(value)
    print(f"callable({name:<20}) = {is_callable:<5}  (value: {value!r})")


# ============================================================================
# PART 8: Putting It All Together - The Complete Logic
# ============================================================================
print("\n\n" + "="*80)
print("PART 8: THE COMPLETE LOGIC - How It All Works Together")
print("="*80)

print("""
STEP-BY-STEP PROCESS:
---------------------

1. inspect.getsource(Class.__init__)  ← FROM 'inspect' MODULE
   → Get source code as a string

2. source.split('\\n')  ← Python BUILTIN string method
   → Split into individual lines

3. FOR EACH LINE:
   re.search(r'self\\.(\\w+)\\s*=\\s*(.+)', line)  ← FROM 're' MODULE
   → Search for pattern: self.ATTRIBUTE = VALUE
   
   IF MATCH FOUND:
     - match.group(1) = attribute name
     - match.group(2) = assignment expression
     
4. CATEGORIZE THE ASSIGNMENT:
   
   a) Check if expression has '()':
      re.search(r'\\w+\\(.*?\\)', expression)  ← FROM 're' MODULE
      → If found: FUNCTION CALL (with parentheses)
   
   b) Check if expression is 'self.method' pattern:
      re.match(r'^self\\.\\w+$', expression)  ← FROM 're' MODULE
      → If matches: FUNCTION REFERENCE (without parentheses)
   
   c) Otherwise:
      → DIRECT VALUE (literal assignment)

5. VERIFY WHAT ACTUALLY EXISTS:
   
   dir(obj)  ← Python BUILTIN
   → Get all attribute names on the object
   
   getattr(obj, attr_name)  ← Python BUILTIN
   → Get the actual value
   
   attr_name in actual_attrs  ← Python BUILTIN
   → Check if attribute exists

""")


# ============================================================================
# COMPLETE EXAMPLE WITH ANNOTATIONS
# ============================================================================
print("\n" + "="*80)
print("COMPLETE ANNOTATED EXAMPLE:")
print("="*80)

def analyze_with_annotations(cls):
    print("\n1️⃣ Get source code:")
    source = inspect.getsource(cls.__init__)  # ← FROM 'inspect' MODULE
    print(f"   inspect.getsource(cls.__init__) → Got {len(source)} characters\n")
    
    print("2️⃣ Split into lines:")
    lines = source.split('\n')  # ← Python BUILTIN string method
    print(f"   source.split('\\n') → Got {len(lines)} lines\n")
    
    print("3️⃣ Search each line for assignments:")
    for line in lines:
        match = re.search(r'self\.(\w+)\s*=\s*(.+)', line)  # ← FROM 're' MODULE
        
        if match:
            attr = match.group(1)  # ← Python BUILTIN (match object method)
            expr = match.group(2).strip()  # ← Python BUILTIN (string method)
            
            print(f"   Found: self.{attr} = {expr}")
            
            # Categorize
            if '()' in expr:  # ← Python BUILTIN (string 'in' operator)
                print(f"      → Type: FUNCTION CALL (has parentheses)")
            elif re.match(r'^self\.\w+$', expr):  # ← FROM 're' MODULE
                print(f"      → Type: FUNCTION REFERENCE (no parentheses)")
            else:
                print(f"      → Type: DIRECT VALUE\n")

analyze_with_annotations(MyClass)


# ============================================================================
# SUMMARY TABLE
# ============================================================================
print("\n" + "="*80)
print("QUICK REFERENCE: Module/Builtin Lookup")
print("="*80)
print("""
FROM 'inspect' MODULE:
----------------------
inspect.getsource(func)     → Get source code of a function/class

FROM 're' MODULE (Regular Expressions):
----------------------------------------
re.search(pattern, string)  → Find pattern anywhere in string
re.match(pattern, string)   → Check if pattern matches at start
re.findall(pattern, string) → Find all occurrences of pattern

PYTHON BUILTINS (no import needed):
------------------------------------
dir(obj)                    → List all attributes/methods
getattr(obj, name)          → Get attribute value by name
callable(obj)               → Check if object can be called
string.split(separator)     → Split string into list
string.strip()              → Remove whitespace
'substring' in string       → Check if substring exists
""")
