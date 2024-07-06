from linked_list import ListNode


def get_length(head: ListNode) -> int:
  if not head:
    return 0
  
  if head and not head.next:
    return 1
  
  length = 0
    
  while head:
    length += 1
    head = head.next
      
  return length
