class StockPrice:

    def __init__(self):
        self.records={}
        self.latest=0
        self.Max_heap=[]
        self.Min_heap=[]

    def update(self, timestamp: int, price: int) -> None:
        
        self.records[timestamp]=price
        self.latest=max(self.latest,timestamp)
        
        heapq.heappush(self.Max_heap,(-price,timestamp))
        heapq.heappush(self.Min_heap,(price,timestamp))
        
            
        
        

    def current(self) -> int:
        return self.records[self.latest]
        

    def maximum(self) -> int:
        p, t = heapq.heappop(self.Max_heap)
        
        while -p != self.records[t]:
            p,t=heapq.heappop(self.Max_heap)
        heapq.heappush(self.Max_heap,(p,t))    
    
        
        return -p
            
        

    def minimum(self) -> int:
        p, t = heapq.heappop(self.Min_heap)
        
        while p != self.records[t]:
            p,t=heapq.heappop(self.Min_heap)
        heapq.heappush(self.Min_heap,(p,t))
    
        
        return p
        
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()