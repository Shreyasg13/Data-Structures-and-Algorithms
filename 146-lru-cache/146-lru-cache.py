class LRUCache:

    def __init__(self, capacity: int):
        self.Map={None:None}
        self.capacity=capacity
        self.stack=[]
        

    def get(self, key: int) -> int:
        if key in self.Map:
            self.stack.remove(key)
            self.stack.append(key)
            return self.Map[key]
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.Map:
            self.stack.remove(key)
            self.stack.append(key)
            self.Map[key]=value
        else:
            if len(self.stack)==self.capacity:
                LRU=self.stack[0]
                self.stack.remove(LRU)
                self.Map.pop(LRU)
                
            self.Map[key]=value
            self.stack.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)