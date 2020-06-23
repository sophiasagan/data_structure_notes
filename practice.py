# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements that appear twice in this array.
# Could you do it without extra space and in O(n) runtime?
#leetcode 442 finding all duplicates

input = [4, 3, 2, 7, 8, 2, 3, 1]
output = [2, 3]

class Solution(object):

     def findDuplicates(self, nums):
        if not nums: #if list is empty
            return [] # return empty array
        
        result = [] #empty array for results
        for _, num in enumerate(nums): #regardless of position for each number, iterate through the list and create a tuple for numbers in the list
            index = abs(num)-1 #gives us the index -1 e.g. 4 -1 = 7 (in index 3)
            if nums[index] < 0: # if number matches a previously negative index ...
                result.append(index+1) # append to results
            nums[index]*=-1 # makes number in that index negative
        return result
     

# def test():
#     solution = Solution()

#     assert sorted(solution.findDuplicates([])) == []
#     assert sorted(solution.findDuplicates([1])) == []
#     assert sorted(solution.findDuplicates([3, 3, 1])) == [3]
#     assert sorted(solution.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])) == [2, 3]
#     print("self test passed")

# if __name__ == '__main__':
    # test()