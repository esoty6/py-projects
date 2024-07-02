from linked_list import LinkedList, ListNode


def sum_lists_backward(x: ListNode, y: ListNode) -> LinkedList:
  dummy = ListNode(None)
  current = dummy
  carry = 0
  
  while x or y or carry:
    val_x = x.data if x else 0
    val_y = y.data if y else 0
    
    total = val_x + val_y + carry
    carry = total // 10
    digit = total % 10
    
    current.next = ListNode(digit)
    current = current.next
    
    if x:
      x = x.next
    if y:
      y = y.next
  
  result_list = LinkedList()
  result_list.head = dummy.next
    
  return result_list


def sum_lists_forward(x: ListNode, y: ListNode) -> LinkedList:
  result_list = LinkedList()
  
  def get_length(head: ListNode) -> int:
    length = 0
    
    while head:
      length += 1
      head = head.next
      
    return length
  
  
  def pad_list(head: ListNode, pad: int) -> ListNode:
    dummy = ListNode(None)
    current = dummy
    
    for _ in range(pad):
      current.next = ListNode(0)
      current = current.next
    
    current.next = head
    
    return dummy.next
    
  
  def pad_zeros(x: ListNode, y: ListNode) -> tuple:
    len_x = get_length(x)
    len_y = get_length(y)
    
    if len_x == len_y:
      return x, y
    
    pad = abs(len_x - len_y)
    
    if len_x < len_y:
      x = pad_list(x, pad)
      
    else:
      y = pad_list(y, pad)
      
    return x, y

  
  def calculate_carry(x, y):
    if not x and not y:
      return 0
    
    carry = calculate_carry(x.next, y.next)
    
    if x:
      carry += x.data
    if y:
      carry += y.data

    result_list.insert(ListNode(carry % 10))

    return carry // 10
  
  
  pad_x, pad_y = pad_zeros(x, y)

  calculate_carry(pad_x, pad_y)
  
  return result_list


# backward
linked_list1 = LinkedList()
linked_list2 = LinkedList()

linked_list1.append(7)
linked_list1.append(1)
linked_list1.append(6)
linked_list2.append(5)
linked_list2.append(9)
linked_list2.append(2)

print('Backward lists')
linked_list1.print_list()
linked_list2.print_list()

backward = sum_lists_backward(linked_list1.head, linked_list2.head)

print('Result')
backward.print_list()

print('----------')

# forward
linked_list1 = LinkedList()
linked_list2 = LinkedList()

linked_list1.append(6)
linked_list1.append(1)
linked_list1.append(7)
linked_list2.append(2)
linked_list2.append(9)
linked_list2.append(5)

print('Forward lists')
linked_list1.print_list()
linked_list2.print_list()

forward = sum_lists_forward(linked_list1.head, linked_list2.head)

print('Result')
forward.print_list()
