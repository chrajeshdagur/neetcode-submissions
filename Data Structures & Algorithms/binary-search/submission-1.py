class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low_ind=0
        high_ind=len(nums)-1

        #print(low_ind +'and'+ high_ind)

        while low_ind <= high_ind:

            #
            # Both math equations yield the exact same index result. 
            # However, this specific syntax prevents a critical bug called ""Integer Overflow"".
            
            # If low_ind and high_ind are both very large numbers, 
            # adding them together (low_ind + high_ind) can exceed that limit. 
            #This causes the number to wrap around into a negative value, crashing your program.

            # basically due to integer data type overflow we use first to (high - low) // 2 = ? ; ? + low
            mid_ind= low_ind + (high_ind - low_ind) // 2
            # mindblowing if you explain  engineer love it 
            #print(mid_ind) 

            if nums[mid_ind] == target:
                return mid_ind

            elif nums[mid_ind] < target:
                low_ind = mid_ind + 1
            
            else:
                high_ind = mid_ind - 1

        return -1
