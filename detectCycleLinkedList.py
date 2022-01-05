class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            while head.next != None:
                if type(head.val) == bool:
                    return True
                else:
                    head.val = True
                head = head.next
        return False