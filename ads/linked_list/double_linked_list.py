from linked_list import LinkedList


class ListNode:
  def __init__(self, data) -> None:
    self.data = data
    self.next: ListNode | None = None
    self.prev: ListNode | None = None

  def __str__(self) -> str:
    return f'{self.data, self.next.data if self.next else None}'
  

class DoubleLinkedList(LinkedList):
  def append(self, data) -> None:
    new_node = ListNode(data)
    
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
    