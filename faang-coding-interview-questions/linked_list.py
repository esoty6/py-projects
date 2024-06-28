class Node:
  def __init__(self, data) -> None:
    self.data = data
    self.next: Node | None = None
    self.prev: Node | None = None

  def __str__(self) -> str:
    return f'{self.data, self.next.data if self.next else None}'
  
  
def sort_list(head: Node) -> Node:
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

def merge(left: Node, right: Node) -> Node:
  dummy = Node(None)
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
  
  
class LinkedList:
  def __init__(self) -> None:
    self.head: Node | None = None
  
  def append(self, data) -> None:
    new_node = Node(data)
    
    if not self.head:
      self.head = new_node
      return
    
    last = self.head
    
    while last.next:
      last = last.next
      
    last.next = new_node
    
    
  def kth_to_last(self, k: int) -> int | None:
    if not self.head and k < 1 :
      return None
    
    slow = fast = self.head
    
    for _ in range(k):
      if not fast:
        return None
      
      fast = fast.next
    
    while fast:
      fast = fast.next
      slow = slow.next
      
    return slow.data
    
    
  def _get_list(self) -> list:
    if not self.head:
      return 'LinkedList is empty'
    
    last = self.head
    array = [str(last.data)]
    
    while last.next:
      last = last.next
      array.append(str(last.data))
      
    return array
  
  
  def find_by_value(self, value) -> bool:
    if not self.head:
      return False
    
    last = self.head
    
    if (last.data == value):
      return True
    
    while last.next:
      last = last.next
      if (last.data == value):
        return True
      
    return False
  
  
  def delete_value(self, value) -> bool:
    if not self.head:
      return False
 
    if self.head.data == value:
      self.head = self.head.next
      return True
    
    current = self.head
    
    while current.next:
      if current.data == value:
        current.next = current.next.next
        return True
        
      current = current.next
      
    return True
    
    
  def remove_duplicates(self) -> None:
    if not self.head or not self.head.next:
      return
    
    self.head = sort_list(self.head)

    current = self.head
    while current and current.next:
      if current.data == current.next.data:
        current.next = current.next.next
      else:
        current = current.next
    
    
  def print_list(self) -> None:
    print(' -> '.join(self._get_list()))
  
  
  def __str__(self) -> str:
    return f'{self.head.data}'
 
  
class DoubleLinkedList(LinkedList):
  def append(self, data) -> None:
    new_node = Node(data)
    
    if not self.head:
      self.head = new_node
      return
    
    last = self.head
    
    while last.next:
      last = last.next
      
    last.next = new_node
    last.next.prev = last
    

  def print_list(self) -> None:
    print(' <-> '.join(self._get_list()))


linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

linked_list.print_list()

# Remove duplicates
linked_list.append(2)
linked_list.append(2)
linked_list.print_list()
linked_list.remove_duplicates()
linked_list.print_list()

# kth to last element
# print(linked_list.kth_to_last(1))

# linked_list.append(9)
# linked_list.print_list()

# print(linked_list.kth_to_last(3))
# print(linked_list.kth_to_last(5))
# print(linked_list.kth_to_last(4))

# Find by value
# print(linked_list.find_by_value(1))
# print(linked_list.find_by_value(2))
# print(linked_list.find_by_value(6))
# print(linked_list.find_by_value(0))
# print(linked_list.find_by_value(90))

# Deletion
# print(linked_list.delete_value(1))

# linked_list.print_list()

# linked_list.append(2)

# print(linked_list.delete_value(2))

# linked_list.print_list()

# linked_list.append(4)
# linked_list.append(7)
# linked_list.append(8)

# linked_list.print_list()

# print(linked_list.delete_value(4))

# linked_list.print_list()

# print(linked_list.delete_value(8))
# print(linked_list.delete_value(123))

# linked_list.print_list()
