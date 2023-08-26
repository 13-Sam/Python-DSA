class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        self.queue.pop(0)

    def display(self):
        print(self.queue)
    def size(self):
        return len(self.queue)
    

q = Queue()
print(q.size())

q.enqueue(2)
q.enqueue(4)
q.enqueue(6)
q.enqueue(7)
q.display()
q.dequeue()
q.display()
