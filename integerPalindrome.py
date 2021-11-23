class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_x = str(x)
        num_stack = []
        for i in range(len(num_x)):
            num_stack.append(num_x[i])
        i = 0
        while len(num_stack) > 0:
            if num_stack.pop() != num_x[i]:
                return False
            else:
                i += 1
        return True
