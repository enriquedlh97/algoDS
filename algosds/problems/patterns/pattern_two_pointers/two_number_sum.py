'''
Problem:

Given an non-empty array of different integers and a target sum integer,
find any pair that sums up to the target and return them.

When there is no pair summing up to the target return an empty array.

Single integers cannot be summed to themselves. The pair must be comprised
of different integers from the array.

There is at most one pair summing up to the target.

Input:
    array: [3, 5, -4, 8, 11, 1, -1, 6]
    target sum: 10

Output:
    [-1,11]
'''


# Time O(n^2)
# Space O(1)
def twoNumberSum_forLoop(array, targetSum):
    for index, n_1 in enumerate(array):
        for n_2 in array[index + 1:]:
            if n_1 + n_2 == targetSum:
                return [n_1, n_2]

    return []

# Time O(n)
# Space O(n)
def twoNumberSum_hashTable(array, targetSum):
    sumComplement = {}
    for num in array:
		valueComplement = targetSum - num
		if valueComplement in sumComplement:
			return [valueComplement, num]
		else:
			sumComplement[num] = True

    return []

# Time O(nlg(n))
# Space O(1)
def twoNumberSum_pointers(array, targetSum):
    array.sort()
    rightPointer = len(array) - 1
    leftPointer = 0

    for idx in array:
        sum = array[leftPointer] + array[rightPointer]
        if sum == targetSum:
            return [array[leftPointer], array[rightPointer]]
        else:
            if sum < targetSum:
                leftPointer += 1
            else:
                rightPointer -= 1

    return []
