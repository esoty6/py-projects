import math 
  
  
MAX_SIZE = 10000001


class DoubleHash: 
    def __init__(self, n: int): 
        self.TABLE_SIZE = n 
        self.PRIME = self.__get_largest_prime(n - 1) 
        self.keysPresent = 0
        self.hashTable = [-1] * n 
  
    def __get_largest_prime(self, limit: int) -> int: 
        is_prime = [True] * (limit + 1) 
        is_prime[0], is_prime[1] = False, False
        for i in range(2, int(math.sqrt(limit)) + 1): 
            if is_prime[i]: 
                for j in range(i * i, limit + 1, i): 
                    is_prime[j] = False
        for i in range(limit, -1, -1): 
            if is_prime[i]: 
                return i 
  
    def __hash1(self, value: int) -> int:
        return value % self.TABLE_SIZE 
  
    def __hash2(self, value: int) -> int: 
        return self.PRIME - (value % self.PRIME) 
  
    def is_full(self) -> bool: 
        return self.TABLE_SIZE == self.keysPresent 
  
    def insert(self, value: list) -> None: 
        if value == -1 or value == -2: 
            print("ERROR : -1 and -2 can't be inserted in the table") 
            return
        if self.is_full(): 
            print("ERROR : Hash Table Full") 
            return
        probe, offset = self.__hash1(value[0]), self.__hash2(value[0]) 
        while self.hashTable[probe] != -1: 
            if -2 == self.hashTable[probe]: 
                break
            probe = (probe + offset) % self.TABLE_SIZE 
        self.hashTable[probe] = value 
        self.keysPresent += 1
  
    def erase(self, value: int) -> None: 
        if not self.search(value): 
            return
        probe, offset = self.__hash1(value), self.__hash2(value) 
        while self.hashTable[probe] != -1: 
            if type(self.hashTable[probe]) is list and self.hashTable[probe][0] == value: 
                self.hashTable[probe] = -2
                self.keysPresent -= 1
                return
            else: 
                probe = (probe + offset) % self.TABLE_SIZE 
  
    def search(self, value: int) -> bool: 
        probe, offset, initialPos, firstItr = self.__hash1(value), self.__hash2(value), self.__hash1(value), True
        while True: 
            if self.hashTable[probe] == -1: 
                break
            elif type(self.hashTable[probe]) is list and self.hashTable[probe][0] == value:
                return True
            elif probe == initialPos and not firstItr: 
                return False
            else: 
                probe = (probe + offset) % self.TABLE_SIZE 
            firstItr = False
        return False
  
    def to_string(self) -> str: 
        return ", ".join(map(str, self.hashTable))
  
  
if __name__ == '__main__': 
    myHash = DoubleHash(13) 

    insertions = [[115, 'mango'], [123, "apple"], [123, "apricot"],[163, "cherry"],[93, "pear"],[323, "banana"], [-1, 'strawberry'], [-2, 'blueberry']] 
    for insertion in insertions: 
        myHash.insert(insertion) 
    print(f"Status of hash table after initial insertions: {myHash.to_string()}") 
  
    queries = [1, 123, 2, 115, -1] 
    n2 = len(queries) 
    print("Search operation after insertion: ") 
      
    for i in range(n2): 
        if myHash.search(queries[i]): 
            print(queries[i], "present") 
              
    deletions = [123, 87, 115, -2] 
    n3 = len(deletions) 
      
    for i in range(n3): 
        myHash.erase(deletions[i]) 
          
    print(f"Status of hash table after deleting elements: {myHash.to_string()}") 
  
    myHash.erase(123) 

    print(f"Status of hash table after deleting elements: {myHash.to_string()}") 
    