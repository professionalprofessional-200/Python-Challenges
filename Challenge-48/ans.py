class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.is_empty():
            removed = self.queue.pop(0)
            print(f"Dequeued: {removed}")
        else:
            print("Queue is empty. Cannot dequeue.")

    def peek(self):
        if not self.is_empty():
            print(f"Front element: {self.queue[0]}")
        else:
            print("Queue is empty.")

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Queue contents:", self.queue)

# Example usage
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
q.peek()
q.dequeue()
q.display()
q.dequeue()
q.dequeue()
q.dequeue()  # Trying to dequeue from empty queue
