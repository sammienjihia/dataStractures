class Solution:
    """
    [5,6,7,0,1,2,3,4]
    [6,7,0,1,2,3,4,5]
    [2,3,4,5,6,7,0,1]
    [3,4,5,6,7,0,1,2]
    
    if mid greater than the first elem, then from mid to first elem is ordered
    if mid is smaller than the first element, then form mid to end is ordered
    
    Conclusion, if the mid elem is smaller than the first element, then the smallest number is
    to the right of the mid_elem
    
    Nb all the elements bofore the smallest element are ordered, and all elements after the 
    """

    # If answere is to return the true if found the recursion is a good strategy
    def search(self, nums, target):
        # find largest number 
        len_nums = len(nums)
        mid_index = len_nums//2
        
        # Get mid element and compare with first and last elements
        mid_elem = nums[mid_index]
        start_elem = nums[~(len_nums-1)]
        end_elem = nums[len_nums-1]
        
        if target == mid_elem:
            return True
        
        if start_elem < mid_elem and mid_elem < end_elem:
            # this means the list is already sorted
            
            if target > end_elem:
                # means target is not in the sorted list
                return -1
            elif target < start_elem:
                return -1
            else:
                if target > mid_elem:
                    # if target > mid elem then recursively call search with nums being the left portion
                    
                    return self.search(nums[mid_index+1:], target)
                    
                else:
                    return self.search(nums[:mid_index], target)
                    
        elif mid_elem > start_elem :
            # if mid elem is greater than the first elem, it means from elems from the first elem
            # to the mid elem is ordered
            # call search recurssivley
            if target > start_elem and target < mid_elem:
                return self.search(nums[:mid_index+1], target)
            else:
                return self.search(nums[mid_index+1:], target)
            
        elif mid_elem < start_elem:
            # if mid elem is less than start elem, then all the elems to the right of mid elem
            # are sorted
            if target > mid_elem and target < end_elem:
                return self.search(nums[mid_index:], target)
            else:
                return self.search(nums[:mid_index], target)

    def searchII(self, nums, target):

        len_nums = len(nums)

        start_index = 0
        end_index = len_nums-1
        mid_index = end_index//2

        start_elem = nums[start_index]
        mid_elem = nums[mid_index]
        end_elem = nums[end_index]

        iterate = True

        while iterate:
            if start_index == end_index:
                if target == start_elem:
                    iterate = False
                    ans = start_index
                else:
                    iterate = False
                    ans =  -1
            else:
                if mid_elem < start_elem:
                    # right portion is sorted
                    if target < mid_elem:
                        end_index = mid_index
                        end_elem = mid_elem
                        mid_index = (start_index + end_index)//2
                        mid_elem = nums[mid_index]
                    else:
                        
                else:
                    # left portion is sorted

        return ans

        

            
if __name__ == "__main__":
    sol = Solution()
    print(sol.search([4,5,6,7,0,1,2],0))
        
        