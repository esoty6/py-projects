from linked_list import LinkedList, ListNode

  
def palindrome(head: ListNode) -> bool:
  if not head or not head.next:
    return True
  
  slow = fast = head
  while fast.next and fast.next.next:
    slow = slow.next
    fast = fast.next.next
  
  second_half = reverse_list(slow.next)
  
  first_half = head
  while second_half:
    if first_half.data != second_half.data:
      return False
    
    first_half = first_half.next
    second_half = second_half.next
  
  return True

def reverse_list(head: ListNode) -> ListNode:
  prev = None
  current = head
  
  while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node
    
  return prev
  

linked_list = LinkedList() 

linked_list.append('a') 
linked_list.append('b') 
linked_list.append('b')
linked_list.append('a') 

print(palindrome(linked_list.head))

linked_list.append('c')

print(palindrome(linked_list.head)) 
