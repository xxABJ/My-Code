import inspect
import re

print("="*80)
print("COMPLETE SOLUTION: Source Inspection + Assignment Type Detection")
print("="*80)

class TestClass:
    def __init__(self, mode="production"):
        # Direct value assignments
        self.name = "Alice"
        self.age = 25
        self.scores = [90, 85, 95]
        
        # Function call assignments (WITH parentheses)
        self.result = self.calculate()
        self.message = self.get_message()
        
        # Function reference assignments (WITHOUT parentheses)
        self.func_ref = self.calculate
        self.method_ref = self.get_message
        
        # Conditional assignments
        if mode == "production":
            self.prod_value = self.setup_prod()
            self.prod_name = "Production Server"
        else:
            self.dev_func = self.setup_dev
        
        # Call other methods
        self.configure()
    
    def calculate(self):
        return 42
    
    def get_message(self):
        return "Hello World"
    
    def setup_prod(self):
        return "prod_config"
    
    def setup_dev(self):
        return "dev_config"
    
    def configure(self):
        # More assignments in called method
        self.config_value = self.load_config()
        self.config_ref = self.load_config
        self.config_name = "Main Config"
    
    def load_config(self):
        return {"setting": "value"}
    
    def activate(self):
        # This is NOT called from __init__
        self.activated = True
        self.activation_func = self.calculate


def analyze_all_assignments(cls):
    """
    Analyze ALL potential attribute assignments in a class
    """
    print("\n" + "="*80)
    print("ANALYZING ALL METHODS FOR ATTRIBUTE ASSIGNMENTS")
    print("="*80)
    
    all_assignments = {}
    
    # Get all methods
    for method_name in dir(cls):
        if method_name.startswith('_') and method_name != '__init__':
            continue
        
        method = getattr(cls, method_name)
        if not callable(method):
            continue
        
        try:
            source = inspect.getsource(method)
            
            print(f"\n📄 Method: {method_name}()")
            print("-" * 80)
            
            # Find all self.attribute = value assignments
            for line_num, line in enumerate(source.split('\n'), 1):
                match = re.search(r'self\.(\w+)\s*=\s*(.+)', line)
                if match:
                    attr_name = match.group(1)
                    assignment_expr = match.group(2).strip()
                    
                    # Determine assignment type
                    assignment_type = categorize_assignment(assignment_expr)
                    
                    # Check if it's in a conditional
                    is_conditional = bool(re.search(r'^\s*if\s+', line))
                    
                    if attr_name not in all_assignments:
                        all_assignments[attr_name] = []
                    
                    all_assignments[attr_name].append({
                        'method': method_name,
                        'expression': assignment_expr,
                        'type': assignment_type,
                        'conditional': is_conditional,
                        'line': line.strip()
                    })
                    
                    # Print with color coding
                    type_icon = {
                        'direct_value': '📦',
                        'function_call': '🔧',
                        'function_reference': '🔗',
                        'external_call': '🌐'
                    }.get(assignment_type, '❓')
                    
                    cond_marker = ' [CONDITIONAL]' if is_conditional else ''
                    print(f"  {type_icon} self.{attr_name} = {assignment_expr:<40} → {assignment_type}{cond_marker}")
        
        except (TypeError, OSError):
            pass
    
    return all_assignments


def categorize_assignment(expression):
    """
    Determine the type of assignment based on the expression
    """
    # Check if it's a function call (has parentheses)
    if re.search(r'\w+\(.*?\)', expression):
        # Check if it's calling self.method()
        if expression.startswith('self.') and '()' in expression:
            return 'function_call'
        else:
            return 'external_call'
    
    # Check if it's a function reference (self.method without parentheses)
    elif re.match(r'^self\.\w+$', expression):
        return 'function_reference'
    
    # Otherwise it's a direct value
    else:
        return 'direct_value'


def create_summary_table(cls, obj):
    """
    Create a comprehensive summary table
    """
    all_assignments = analyze_all_assignments(cls)
    
    # Get actual attributes on the object
    actual_attrs = {attr: getattr(obj, attr) 
                   for attr in dir(obj) 
                   if not attr.startswith('_') and not callable(getattr(obj, attr))}
    
    print("\n" + "="*80)
    print("COMPREHENSIVE SUMMARY TABLE")
    print("="*80)
    print(f"{'Attribute':<20} {'Type':<20} {'Method':<15} {'Exists':<10} {'Value':<20}")
    print("-"*80)
    
    # Show all potential attributes
    for attr_name in sorted(all_assignments.keys()):
        info = all_assignments[attr_name][0]  # First occurrence
        exists = attr_name in actual_attrs
        value = repr(actual_attrs[attr_name])[:18] if exists else 'N/A'
        exists_marker = '✅' if exists else '⚠️'
        
        type_display = {
            'direct_value': 'Direct Value',
            'function_call': 'Function Call',
            'function_reference': 'Function Ref',
            'external_call': 'External Call'
        }.get(info['type'], 'Unknown')
        
        print(f"{attr_name:<20} {type_display:<20} {info['method']:<15} {exists_marker:<10} {value:<20}")
    
    # Show categorized groups
    print("\n" + "="*80)
    print("CATEGORIZED BY ASSIGNMENT TYPE")
    print("="*80)
    
    categories = {}
    for attr_name, infos in all_assignments.items():
        info = infos[0]
        cat = info['type']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append((attr_name, info, attr_name in actual_attrs))
    
    for cat, items in sorted(categories.items()):
        type_display = {
            'direct_value': '📦 DIRECT VALUE ASSIGNMENTS',
            'function_call': '🔧 FUNCTION CALL ASSIGNMENTS (with ())',
            'function_reference': '🔗 FUNCTION REFERENCE ASSIGNMENTS (without ())',
            'external_call': '🌐 EXTERNAL FUNCTION CALLS'
        }.get(cat, cat)
        
        print(f"\n{type_display}:")
        print("-" * 80)
        for attr_name, info, exists in items:
            exists_marker = '✅' if exists else '⚠️'
            print(f"  {exists_marker} self.{attr_name:<18} = {info['expression']:<35} [{info['method']}]")


# Run the analysis
print("\n" + "="*80)
print("TEST: Creating object in PRODUCTION mode")
print("="*80)
obj = TestClass(mode="production")
create_summary_table(TestClass, obj)

print("\n\n" + "="*80)
print("EXPLANATION OF EACH TYPE:")
print("="*80)
print("""
📦 DIRECT VALUE ASSIGNMENTS:
   - Direct assignment of literal values
   - Examples: self.name = "Alice"
              self.age = 25
              self.scores = [90, 85, 95]

🔧 FUNCTION CALL ASSIGNMENTS (with parentheses):
   - Assigns the RETURN VALUE of a function call
   - Examples: self.result = self.calculate()
              self.message = self.get_message()
   - The function IS EXECUTED, stores the result

🔗 FUNCTION REFERENCE ASSIGNMENTS (without parentheses):
   - Assigns the FUNCTION ITSELF (not called)
   - Examples: self.func_ref = self.calculate
              self.method_ref = self.get_message
   - The function is NOT executed, stores the callable

🌐 EXTERNAL FUNCTION CALLS:
   - Calls to functions not defined in the class
   - Examples: self.data = json.loads(text)
              self.time = datetime.now()
""")
