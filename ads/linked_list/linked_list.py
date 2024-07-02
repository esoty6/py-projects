class ListNode:
  def __init__(self, data) -> None:
    self.data = data
    self.next: ListNode | None = None

  def __str__(self) -> str:
    return f'{self.data, self.next.data if self.next else None}'
 
class LinkedList:
  def __init__(self) -> None:
    self.head: ListNode | None = None
  
  def append(self, data) -> None:
    new_node = ListNode(data)
    
    if not self.head:
      self.head = new_node
      return
    
    last = self.head
    
    while last.next:
      last = last.next
      
    last.next = new_node
    
    
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
  
  
  def insert(self, node: ListNode) -> None:
    node.next = self.head
    self.head = node
  
    
  def print_list(self) -> None:
    print(' -> '.join(self._get_list()))
  
  
  def __str__(self) -> str:
    return f'{self.head.data}'
