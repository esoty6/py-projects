from linked_list import LinkedList, ListNode


def kth_to_last(head: ListNode, k: int) -> int | None:
  if not head and k < 1 :
    return None
  
  slow = fast = head
  
  for _ in range(k):
    if not fast:
      return None
    
    fast = fast.next
  
  while fast:
    fast = fast.next
    slow = slow.next
    
  return slow.data


linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

print(kth_to_last(linked_list.head, 1))

linked_list.append(9)
linked_list.print_list()

print(kth_to_last(linked_list.head, 3))
print(kth_to_last(linked_list.head, 5))
print(kth_to_last(linked_list.head, 4))
