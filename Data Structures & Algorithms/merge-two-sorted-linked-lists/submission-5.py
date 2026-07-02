# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return None
        newList: Optional[ListNode] = ListNode()
        head = newList

        while list1 and list2:
            temp : Optional[ListNode] = ListNode()
            if list1.val <= list2.val:
                newList.val = list1.val
                list1 = list1.next
            elif list2.val <= list1.val:
                newList.val = list2.val
                list2 = list2.next
            newList.next = temp
            newList = newList.next

        if list1 != None and list2 == None:
            newList.val = list1.val
            newList.next = list1.next
        elif list2 != None and list1 == None:
            newList.val = list2.val
            newList.next = list2.next
        else:
            newList = None
        return head