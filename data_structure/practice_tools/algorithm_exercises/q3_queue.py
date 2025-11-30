class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        # Note: Using (Rear + 1) % N == Front for Full condition
        # This wastes one slot but is the standard array-based implementation without extra count variable.
        
    def is_empty(self):
        return self.front == self.rear
    
    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    
    def insert(self, item):
        if self.is_full():
            print("Queue Is Full")
            return
        
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        print(f"Inserted {item}. Front={self.front}, Rear={self.rear}")
        
    def delete(self):
        if self.is_empty():
            print("Queue Is Empty")
            return None
        
        self.front = (self.front + 1) % self.size
        item = self.queue[self.front]
        print(f"Deleted {item}. Front={self.front}, Rear={self.rear}")
        return item

def solve_q3():
    print("=== Question 3: Queue Implementation ===")
    print("Problem with Linear Queue: 'False Overflow'. Space is available at the front but Rear reached end.")
    print("Solution: Circular Queue.")
    
    N = 5
    cq = CircularQueue(N)
    
    print(f"\nTesting Circular Queue (Size {N}):")
    cq.insert('A')
    cq.insert('B')
    cq.insert('C')
    cq.insert('D') # Should be full now (N-1 items)
    cq.insert('E') # Full
    
    cq.delete() # Remove A
    cq.insert('E') # Should work now (Circular)
    
    cq.delete()
    cq.delete()
    cq.delete()
    cq.delete() # Empty
    cq.delete() # Empty error

if __name__ == "__main__":
    solve_q3()
