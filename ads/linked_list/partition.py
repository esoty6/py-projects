from linked_list import LinkedList, ListNode


def partition(head: ListNode, pivot: int) -> ListNode:
  smaller_head = smaller_last = None
  greater_last = greater_head = None
  equal_head = equal_last = None

  while head:
    if head.data == pivot: 
      if not equal_head: 
        equal_head = equal_last = head 
      else:
        equal_last.next = head 
        equal_last = equal_last.next
        
    elif head.data < pivot: 
      if not smaller_head: 
        smaller_last = smaller_head = head 
      else:
        smaller_last.next = head 
        smaller_last = head 
    
    else:
      if not greater_head:
        greater_last = greater_head = head 
      else:
        greater_last.next = head 
        greater_last = head 
        
    head = head.next
  
  if greater_last:
    greater_last.next = None

  if not smaller_head:
    if not equal_head:

      return greater_head 
    
    equal_last.next = greater_head 

    return equal_head 
  
  if not equal_head:
    smaller_last.next = greater_head

    return smaller_head 

  smaller_last.next = equal_head 
  equal_last.next = greater_head 
  
  return smaller_head


linked_list = LinkedList()

linked_list.append(3)
linked_list.append(5)
linked_list.append(8)
linked_list.append(5)
linked_list.append(10)
linked_list.append(2)
linked_list.append(1)
linked_list.print_list()

partition(linked_list.head, 5)

linked_list.print_list()

