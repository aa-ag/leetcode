from typing import List

def mergeTwoLists(list1, list2):
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    ### dummy node to store result
    dummy = ListNode(0)

    ### tail store last node
    tail = dummy

    while True:
        ### check if either list is empty
        ### if so, join all elements from non-empty  list
        if list1 is None:
            tail.next = list2
            break
        if list2 is None:
            tail.next = list1