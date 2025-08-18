# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
             return False

        kaplumbaga=head
        tavsan=head

        while tavsan and tavsan.next:
          kaplumbaga=kaplumbaga.next
          tavsan=tavsan.next.next
          if kaplumbaga==tavsan:
              return True
        return False    
