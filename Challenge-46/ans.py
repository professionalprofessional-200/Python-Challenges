class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if not self.is_empty():
            removed = self.stack.pop()
            print(f"Popped: {removed}")
        else:
            print("Stack is empty. Cannot pop.")

    def peek(self):
        if not self.is_empty():
            print(f"Top element: {self.stack[-1]}")
        else:
            print("Stack is empty.")

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack contents:", self.stack)

# Example usage
s = Stack()
s.push(10)
s.push(20)
s.display()
s.peek()
s.pop()
s.display()
s.pop()
s.pop()  # Trying to pop from empty stack
