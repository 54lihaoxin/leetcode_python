# Search Insert Position
# 
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# 
# You may assume no duplicates in the array.
# 
# Here are few examples.
# [1,3,5,6], 5 -> 2
# [1,3,5,6], 2 -> 1
# [1,3,5,6], 7 -> 4
# [1,3,5,6], 0 -> 0


# import CommonClasses    # hxl: comment out this line for submission


debug = True
debug = False


class Solution:
    
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        
        if len(A) == 0:
            return 0
        
        r = len(A) / 2            
        low = 0
        high = len(A) - 1
        
        while low != r and high != r:
            if target == A[r]:
                return r    # hxl: base case: target found!
            elif target < A[r]:
                high = r
                r = low + (high - low) / 2
                if r == high: 
                    r -= 1  # hxl: index r is not allowed to stay the same
            else:   # A[r] < target
                low = r
                r = low + (high - low) / 2
                if r == low:
                    r += 1  # hxl: index r is not allowed to stay the same
        
        # hxl: if the flow reaches this point, then it means the target is not found
        if target < A[r]:
            if target <= A[low]:
                # hxl: this handles a case if len(A) is less than 2 and the WHILE loop above is escaped
                r = low
        elif A[r] < target:
            r += 1
            
        return r
        