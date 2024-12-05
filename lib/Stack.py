class Stack:
    
    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def push(self,item):
        if self.size() >= self.limit:
            return None
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        if self.size() >= self.limit:
            return True
        else:
            return False
        
    def search(self,target):
        if target not in self.items:
            return -1
        
        target_index = self.items.index(target)
        distance_from_top = len(self.items)-1 - target_index
        return distance_from_top