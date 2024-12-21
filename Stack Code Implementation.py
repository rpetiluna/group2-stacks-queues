class Stack:
    def __init__(self):
        self.items = []  # Initialize stack as an empty list

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item of the stack."""
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def peek(self):
        """Return the top item of the stack without removing it."""
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

# Main program for stack
stack = Stack()

while True:
    num = int(input("Enter an integer (999 to stop): "))  # User input loop
    if num == 999:
        break
    stack.push(num)

# Display the numbers in reverse order (LIFO)
print("Numbers in reverse order:")
while not stack.is_empty():
    print(stack.pop())
