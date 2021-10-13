arr = list()
head = 0
tail = 0

gr = {
    "A":["B","C","D"],
    "B":["A","C","E"],
    "C":["A","B"],
    "D":["A","E","F"],
    "E":["B","D"],
    "F":["D","A"]
}


class graph:
    def __init__(self):
        self.arr = list()
        self.head = 0
        self.tail = 0
        self.start = None
        self.visited = list() 
    
    def en(self,el):
        self.arr.append(el)
        self.tail += 1   

    
    def deq(self):
        if self.empty():
            return("Finished Graph")
            self.visited.append(self.arr[self.head])
        else:
            self.head += 1

    def full(self):
        if self.tail - self.head == 1:
            return True
        else:
            return False
            
    def empty(self):
        if self.tail == self.head:
            return True
        else:
            return False
    
    def check(self, el):
        if el in self.visited:
            return True
        else:
            return False
        
    def breath(self):
        self.en(self.start)
        self.visited.append(self.start)
        while self.head < len(gr) - 1:
            self.deq()
            for node in gr[self.start]:
                if node not in self.visited:
                    self.en(node)
                    self.visited.append(node)
                
            self.start = self.arr[self.head]
        else:
            return self.visited


test = graph()
test.start = "A"
print(test.breath())
