class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        left = 0
        right = len(s) - 1

        while left < right:
            #Python performs the assignment simultaneously.
            s[left], s[right] = s[right], s[left]

            # we need to create a temp variable, if want manually
            '''
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            '''

            left += 1
            right -= 1

            

