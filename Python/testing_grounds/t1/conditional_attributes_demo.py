import inspect
import re

print("="*70)
print("SCENARIO: Conditional & Post-Init Attribute Assignment")
print("="*70)

class TestClass:
    def __init__(self, mode="production", enable_cache=True):
        self.name = "Alice"
        self.mode = mode
        
        # CONDITIONAL ASSIGNMENT - only some attributes get created
        if mode == "production":
            self.prod_server = "https://prod.com"
            self.prod_enabled = True
        elif mode == "development":
            self.dev_server = "https://dev.com"
            self.debug_mode = True
        
        # CONDITIONAL based on parameter
        if enable_cache:
            self.cache_size = 1000
            self.cache_enabled = True
        else:
            self.cache_disabled_reason = "User preference"
    
    def activate_feature(self):
        """This method is NOT called from __init__"""
        self.feature_activated = True
        self.activation_time = "2026-01-20"
    
    def process_data(self, data):
        """Conditionally assigns attributes based on runtime data"""
        if len(data) > 100:
            self.large_dataset = True
        else:
            self.small_dataset = True
        
        self.processed = True


def find_all_potential_assignments(obj):
    """
    Find ALL POSSIBLE attribute assignments (even conditional ones)
    """
    print("\n" + "="*70)
    print("STATIC ANALYSIS: Finding all POSSIBLE assignments")
    print("="*70)
    
    potential_assignments = {}
    
    # Get all methods in the class
    for method_name in dir(obj.__class__):
        if method_name.startswith('_') and method_name != '__init__':
            continue
        
        method = getattr(obj.__class__, method_name)
        if not callable(method):
            continue
        
        try:
            source = inspect.getsource(method)
            
            print(f"\n📄 Inspecting {method_name}():")
            print("-" * 70)
            
            # Find all self.attribute = assignments
            for line in source.split('\n'):
                match = re.search(r'self\.(\w+)\s*=\s*(.+)', line)
                if match:
                    attr_name = match.group(1)
                    assignment_value = match.group(2).strip()
                    
                    # Check if it's inside a conditional
                    is_conditional = 'if ' in line or line.strip().startswith('if ')
                    
                    if attr_name not in potential_assignments:
                        potential_assignments[attr_name] = []
                    
                    potential_assignments[attr_name].append({
                        'method': method_name,
                        'value': assignment_value,
                        'line': line.strip()
                    })
                    
                    print(f"  Found: self.{attr_name} = {assignment_value}")
        
        except (TypeError, OSError):
            # Built-in methods don't have source
            pass
    
    return potential_assignments


def compare_potential_vs_actual(obj):
    """
    Compare what COULD be assigned vs what ACTUALLY exists
    """
    print("\n" + "="*70)
    print("COMPARISON: Potential vs Actual Attributes")
    print("="*70)
    
    # Get potential assignments from source
    potential = find_all_potential_assignments(obj)
    
    # Get actual attributes on the object
    actual = [attr for attr in dir(obj) if not attr.startswith('_') and not callable(getattr(obj, attr))]
    
    print("\n" + "="*70)
    print("RESULTS:")
    print("="*70)
    
    print(f"\n{'Attribute':<25} {'Status':<15} {'Location':<30}")
    print("-"*70)
    
    all_attrs = set(potential.keys()) | set(actual)
    
    for attr in sorted(all_attrs):
        exists = attr in actual
        could_exist = attr in potential
        
        if exists and could_exist:
            location = potential[attr][0]['method']
            print(f"{attr:<25} {'✅ EXISTS':<15} {location:<30}")
        elif could_exist and not exists:
            location = potential[attr][0]['method']
            print(f"{attr:<25} {'⚠️  NOT CREATED':<15} {location + ' (conditional)':<30}")
        elif exists and not could_exist:
            print(f"{attr:<25} {'❓ UNKNOWN':<15} {'Not found in source':<30}")
    
    return potential, actual


# TEST 1: Production mode with cache
print("\n" + "="*70)
print("TEST 1: Production mode, cache enabled")
print("="*70)
obj1 = TestClass(mode="production", enable_cache=True)
potential1, actual1 = compare_potential_vs_actual(obj1)

# TEST 2: Development mode without cache
print("\n\n" + "="*70)
print("TEST 2: Development mode, cache disabled")
print("="*70)
obj2 = TestClass(mode="development", enable_cache=False)
potential2, actual2 = compare_potential_vs_actual(obj2)

# TEST 3: Call a method AFTER init
print("\n\n" + "="*70)
print("TEST 3: Calling activate_feature() AFTER __init__")
print("="*70)
obj3 = TestClass(mode="production", enable_cache=True)
print(f"\nBefore calling activate_feature():")
print(f"  Has 'feature_activated'? {hasattr(obj3, 'feature_activated')}")

obj3.activate_feature()
print(f"\nAfter calling activate_feature():")
print(f"  Has 'feature_activated'? {hasattr(obj3, 'feature_activated')}")
print(f"  Value: {obj3.feature_activated}")

print("\n" + "="*70)
print("SOLUTION SUMMARY:")
print("="*70)
print("""
STATIC ANALYSIS (Source Code Inspection):
------------------------------------------
✅ Can find: All POSSIBLE attributes in all methods
✅ Can detect: Which method could create each attribute
❌ Cannot predict: Which conditional branches will execute
❌ Cannot predict: Runtime-dependent conditions

RUNTIME INSPECTION (Object Inspection):
---------------------------------------
✅ Can find: Attributes that ACTUALLY exist on the object
✅ Can detect: Current state after __init__
❌ Cannot find: Attributes that COULD exist but weren't created
❌ Cannot find: Attributes from methods not yet called

COMBINED APPROACH:
------------------
1. Use SOURCE INSPECTION to find all POTENTIAL attributes
2. Use RUNTIME INSPECTION to see what ACTUALLY exists
3. Compare the two to identify:
   - Created attributes (in both)
   - Conditional attributes (in source but not runtime)
   - Dynamic attributes (in runtime but not source)
   - Post-init attributes (in methods not called from __init__)

RECOMMENDATION FOR YOUR LOG CLASS:
----------------------------------
For most logging purposes, focus on:
  → Attributes that ACTUALLY exist at logging time
  → Use source inspection as METADATA to show where they came from
  → Don't try to predict all possible conditional attributes
  
To track post-init changes:
  → Re-inspect the object when logging (not just at creation)
  → Compare snapshots to see what changed
""")
