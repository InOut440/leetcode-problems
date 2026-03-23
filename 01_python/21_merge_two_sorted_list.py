from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
        # Append the remaining nodes of the non-empty list
        current.next = list1 if list1 else list2
        
        return dummy.next

def create_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def run_test(arr1: List[int], arr2: List[int]) -> None:
    list1 = create_linked_list(arr1)
    list2 = create_linked_list(arr2)
    merged_head = Solution().mergeTwoLists(list1, list2)
    result = linked_list_to_list(merged_head)
    print(f"list1={arr1}, list2={arr2} --> result={result}")

if __name__ == "__main__":
    run_test([1, 2, 4], [1, 3, 4])
    run_test([], [])
    run_test([], [0])