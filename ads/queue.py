class Queue:
  class QueueNode:
    def __init__(self, data):
      self.data = data
      self.next = None
      
    def __str__(self) -> str:
      return self.data


  def __init__(self):
    self.first = None
    self.last = None    
    
  def push(self, item) -> None:
    node = self.QueueNode(item)
    if self.last:
      self.last.next = node
    self.last = node
    if not self.first:
      self.first = self.last
      
  def remove(self) -> None:
    if not self.first:
      return
    elif self.first.next:
      self.first = self.first.next
    elif self.first == self.last:
      self.first = self.last = None
      
  def is_empty(self) -> bool:
    return self.first is None
    
  def peek(self):
    return self.first.data if not self.is_empty() else 'Empty queue'


queue = Queue()
queue.push('a')
print(queue.peek())
queue.push('b')
print(queue.peek())
queue.push('c')
print(queue.peek())
queue.remove()
print(queue.peek())
queue.remove()
print(queue.peek())
queue.remove()
print(queue.peek())
queue.remove()
print(queue.is_empty())
queue.remove()
queue.push('c')
print(queue.is_empty())
print(queue.peek())
