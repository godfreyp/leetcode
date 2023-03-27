# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# OPTIMAL
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head

        for i in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head
      
# Naive Recursion
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        newHead = self._recursiveRemoval(head, n)
        return newHead

    def _recursiveRemoval(self, head: Optional[ListNode], n: int, currentIndex: int = 1):
        print(currentIndex)
        if head.next == None:
            if currentIndex == n == 1:
                return None
            return currentIndex
        lastIndex = self._recursiveRemoval(head.next, n, currentIndex + 1)
        
        if n == (lastIndex - currentIndex):
            head.next = head.next.next
            lastIndex = -1
        elif (currentIndex == 1 and lastIndex != -1):
            head = head.next
            lastIndex = -1
        
        if (currentIndex == 1):
            return head
        return lastIndex
