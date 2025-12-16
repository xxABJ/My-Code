# reset system
import random
a = 0

dynamic_global_dicts = globals()
#current_dicts = dict(dynamic_global_dicts)
for i in range(10):
    exec(f"variable_{i} = random.randint(1,2)")
global_dicts = dict(dynamic_global_dicts)

print(variable_5)
#variable_5 = "hi"

dynamic_global_dicts["variable_5"] = "hi"
print(variable_5)

#print(new_global_dicts)
print(f"dynamic_global_dicts['variable_5']: {dynamic_global_dicts['variable_5']}")
print(f"global_dicts['variable_5']: {global_dicts['variable_5']}")


print(dynamic_global_dicts)
print(global_dicts)