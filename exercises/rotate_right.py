def rotate_right(nums: list[int], k: int) -> list[int]: # accepts a list and a value, and returns a list (all integers)
    """Rotates list to the right by the desired number k; O(n) time, O(n) space."""
    if bool(nums) != True: # in case the list is empty, return an empty list
        return []
    if len(nums) == k: # returns original set if rotation is equal to the number of observations
        return nums
    k %= len(nums) # calculates remainder in case k is larger than the set 
    return nums[-k:] + nums[:-k] # rotates by desired number and returns final list

assert rotate_right([], 3) == [] # ensures it is not ignoring empty values
assert rotate_right([1,2,3,4,5], 2) == [4,5,1,2,3] # simulates an example and ensures it is calculating as intended
assert rotate_right([10,20,30], 5) == [20,30,10] # simulates if it is calculating the remainder correctly

print(rotate_right([1,2,3,4,5,6,7,8,9,10,12], 25))
