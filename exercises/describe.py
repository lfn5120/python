def describe(value):
    """Evaluates if input is true or false"""
    return "true" if value else "false" # analyses the boolean and provide findings
    
assert describe(12) == "true" # any non-empty values must return as true
assert describe(0) == "false" # empty values are always false
assert describe('') == "false" # empty strings are always false

print(describe.__doc__)
print(describe(154))