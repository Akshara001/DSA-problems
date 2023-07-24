# Definition for singly-linked list:
#class LinkedNode:
#     def_init_(self,x):
#        self.val = x
#         self.next = None

class  Solution:
   def hasCycle(self, head: ListNode) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

            return False