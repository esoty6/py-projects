from linked_list import LinkedList, ListNode


def remove_duplicates(head: ListNode) -> None:
  if not head or not head.next:
    return
  
  head = sort_list(head)

  current = head
  while current and current.next:
    if current.data == current.next.data:
      current.next = current.next.next
    else:
      current = current.next

def sort_list(head: ListNode) -> ListNode:
  if not head or not head.next:
    return head

  slow = fast = head
  prev = None
  while fast and fast.next:
    prev = slow
    slow = slow.next
    fast = fast.next.next
  prev.next = None

  left = sort_list(head)
  right = sort_list(slow)

  return merge(left, right)

def merge(left: ListNode, right: ListNode) -> ListNode:
  dummy = ListNode(None)
  current = dummy

  while left and right:
    if left.data < right.data:
      current.next = left
      left = left.next
    else:
      current.next = right
      right = right.next
    current = current.next

  if left:
    current.next = left
  if right:
    current.next = right

  return dummy.next
  

linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(2)
linked_list.append(2)

linked_list.print_list()

remove_duplicates(linked_list.head)

linked_list.print_list()
