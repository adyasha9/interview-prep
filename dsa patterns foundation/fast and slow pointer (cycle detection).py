# 💡 Tip: Used in cycle detection, middle node finding, Floyd’s Algorithm.
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def has_cycle(head):
    """
    Detect if a linked list has a cycle using fast & slow pointers.
    """
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next  # Move 1 step
        fast = fast.next.next  # Move 2 steps
        if slow == fast:
            return True  # Cycle detected

    return False
