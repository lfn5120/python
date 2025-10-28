def count_even_num(nums: list[int]) -> int:
    """counts how many even numbers in a given list; O(n) time, O(1) space."""
    counter = 0 # keeps track of the count
    for n in nums: # for every number in the list
        if n % 2 == 0: counter += 1 # if the number is even, add one to counter
    return counter # returns the number of observations in which the boolean was true

def count_odd_num(nums: list[int]) -> int:
    """counts how many odd numbers in a given list; O(n) time, O(1) space."""
    counter = 0 # keeps track of the count
    for n in nums: # for every number in the list
        if n % 2 != 0: counter += 1 # if the number is odd, add one to counter
    return counter # returns the number of observations in which the boolean was true

assert count_even_num([0,2,3]) == 2
assert count_even_num([]) == 0
assert count_even_num([2,2,4,5]) == 3
assert count_odd_num([0,2,3]) == 1
assert count_odd_num([]) == 0
assert count_odd_num([1,3,4,5]) == 3
# checks for basic logic, reports any issues

print(count_even_num([2,2,2,3]), "even number(s).")
print(count_odd_num([2,2,2,3]), "odd number(s).")