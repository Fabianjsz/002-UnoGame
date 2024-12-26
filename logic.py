import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def shuffle_linked_list(head):
    # Step 1: Convert linked list to array
    current = head
    values = []
    
    while current:
        values.append(current.val)
        current = current.next
    
    # Step 2: Shuffle the array
    random.shuffle(values)
    
    # Step 3: Rebuild the shuffled linked list
    dummy_head = ListNode()  # Temporary dummy node
    current = dummy_head
    
    for value in values:
        current.next = ListNode(value)
        current = current.next
    
    return dummy_head.next  # Return the shuffled list (dummy's next node)

# Helper functions for testing
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original list:")
print_linked_list(head)

shuffled_head = shuffle_linked_list(head)

print("Shuffled list:")
print_linked_list(shuffled_head)