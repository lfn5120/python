def has_duplicate(a: list[int]) -> bool:
    """Determines if a list contains any duplicate observations; O(n) time, O(n) space."""

    assert isinstance(a, list) # ensures that the object is a list

    seen = set() # creates empty set to store observed numbers

    for n in a: # observes every number in original set individually

        if n in seen:
            return True # end operation if number is observed more than once

        seen.add(n) # add newly observed number until all are observed
    return False # if no flags are raised, then operation is complete


assert has_duplicate([]) == False
assert has_duplicate([1,2]) == False
assert has_duplicate([1,1]) == True
# ensures basic logic is followed

print(has_duplicate([1,2,3,4,12,5]))