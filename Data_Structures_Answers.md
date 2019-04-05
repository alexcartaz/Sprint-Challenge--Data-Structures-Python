Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

O(1)

2. What is the space complexity of your ring buffer's `append` function?

O(n) where n is capacity because the storage array will always have a length of capacity

3. What is the runtime complexity of your ring buffer's `get` method?

O(n) where n is capacity b/c it runs a function that iterates over the entire array to remove any values of None. It is worth noting that it is only O(n) when one or more None values are present. After which it is O(1). After n (capacity) items have been added it will never map over the length of the array b/c no more None values will be present.

4. What is the space complexity of your ring buffer's `get` method?

O(2n) while None values exist and O(1) when they don't

5. What is the runtime complexity of the provided code in `names.py`?

O(n^2) due to 2 nested for loops. for n names in names1 it will run another n times for each n given the number of names in names2

6. What is the space complexity of the provided code in `names.py`?

O(3n) because we have 2 arrays of 10,000 names (1 for each file) and a 3rd array for any duplicates (which could in theory be up to 10,000). 

7. What is the runtime complexity of your optimized code in `names.py`?

O(.5n^2) -> O(n^2). I'm not sure but I think the runtime complexity is still O(n^2), it's just that smarter, more efficient methods for value lookup are being used for each comparison. rather than iterating over each value in names_2 the built-in python method "x in array" optimizes the lookup, taking no more than 0.5n to find the value.

8. What is the space complexity of your optimized code in `names.py`?

O(3n) -- still 3 arrays up to 10,000 each